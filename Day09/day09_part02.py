inp = open('../Inputs/Input09.txt').read()

def print_res(spaces_list):
    result = ''
    for file in files:
        for n in range(file[1]):
            result += str(file[0])

        if len(spaces_list) >= 1:
            next_space = spaces_list[0]
            spaces_list = spaces_list[1:]
            for i in range(next_space):
                result += str(".")
    print(result)

files = []
spaces = []
current_number = 0
id_char = 0
for idx, char in enumerate(inp):
    if idx % 2 == 0:
        files.append((id_char, int(char)))
        id_char += 1
    else:
        spaces.append(int(char))
spaces.append(0)


reversed_files = []
for n in files:
    reversed_files.insert(0, n)

# print(files)
# print(reversed_files)
# print(spaces)

for f in reversed_files:
    for idx, space in enumerate(spaces):
        if f[1] <= space:
            old_index = files.index(f)
            if old_index <= idx:
                continue
            new_index = idx + 1

            # move file
            files.pop(old_index)
            files.insert(new_index, f)

            # space right of inserted number = 0
            spaces[idx] = 0

            # space right of inserted number
            spaces.insert(new_index, space - f[1])

            # merge space of old position into one + size of moved number
            new_spaces = spaces[old_index-1] + spaces[old_index] + f[1]
            spaces[old_index] = new_spaces
            del spaces[old_index+1]

            break

# 6183632723350
# print("00992111777.44.333....5555.6666.....8888.. (SOLUTION)")


total = 0
pos = 0
for idx, file in enumerate(files):
    # print(file)
    current_value = file[0]
    for i in range(file[1]):
        # print(pos, current_value)
        total += current_value * pos
        pos += 1

    for j in range(spaces[idx]):
        pos += 1

# print(spaces)
# print_res(spaces[:])
print(total)