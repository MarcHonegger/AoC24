from sipbuild.generator.parser.annotations import string

lines = open('../Inputs/Input07.txt').read().splitlines()

valid_operators = ['+', '*', '||']

data = []
for line in lines:
    split_line = line.split(":")
    result = int(split_line[0])
    numbers = [int(n) for n in split_line[1].split()]
    data.append([result, numbers])

def calculate_next_step_recursive(rest_numbers, operators_to_use, interim_result, step, total_steps, goal):
    if step == 0:
        return calculate_next_step_recursive(rest_numbers, operators, rest_numbers[0], step + 1, total_steps, goal)
    current_operator = operators_to_use[step - 1]
    first, second = interim_result, rest_numbers[step]
    current_result = int(str(first) + str(second)) if current_operator == '||' else first + second if current_operator == '+' else first * second
    # print(first, second, current_result)
    if step == total_steps:
        return current_result
    elif goal <= current_result:
        return 0
    return calculate_next_step_recursive(rest_numbers, operators, current_result, step + 1, total_steps, goal)

possible_operators = {}
def add_operator_recursive(current_operators, amount_left, current_level):
    new_operators = []
    for operator_list in current_operators:
        for o in valid_operators:
            new_operator = operator_list + [o]
            new_operators.append(new_operator)

    global possible_operators
    possible_operators[current_level] = new_operators

    if amount_left == 1:
        return

    return add_operator_recursive(new_operators, amount_left - 1, current_level + 1)

longest_list = 0
for list_of_numbers in data:
    if len(list_of_numbers[1]) > longest_list:
        longest_list = len(list_of_numbers[1])

add_operator_recursive([[]], longest_list - 1, 0)
print(possible_operators)
total = 0
for l in data:
    result = l[0]
    numbers = l[1]
    for operators in possible_operators[len(numbers) - 2]:
        # print("Calculating: ", numbers, " to get ", result, " with ", operators)
        # print(calculate_next_step_recursive(numbers, operators))
        if result == calculate_next_step_recursive(numbers, operators, 0, 0, len(numbers)-1, result):
            total += result
            break
print ("TOTAL: ", total)