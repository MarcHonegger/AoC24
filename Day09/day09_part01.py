import sys

inp = open('../Inputs/Input09.txt').read()

sys.setrecursionlimit(60000)

list_of_numbers = []
current_number = 0
id_char = 0
for idx, char in enumerate(inp):
    if idx % 2 == 0:
        for i in range(int(char)):
            list_of_numbers.append(id_char)
        id_char += 1
    else:
        for i in range(int(char)):
            list_of_numbers.append(-1)

def move_numbers_recursive(number_list, step):
    # print(number_list)
    # First Number is a "file"
    first = number_list[step]
    while first != -1:
        step += 1
        first = number_list[step]

    # Search for first Number from end of list forward
    for j in range(len(list_of_numbers)):
        second = list_of_numbers[-j-1]
        if second == -1:
            continue
        if step >= (len(number_list) - j - 1):
            return number_list
        number_list[step], number_list[-j-1] = second, -1
        return move_numbers_recursive(number_list, step + 1)



list_of_numbers = move_numbers_recursive(list_of_numbers, 0)

total = 0
for idx, n in enumerate(list_of_numbers):
    if n == -1:
        break
    total += n * idx
print(total)
# print("0099811188827773336446555566..............")