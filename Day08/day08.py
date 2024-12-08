lines = open('../Inputs/Input08.txt').read().splitlines()

map_of_antennas = []
map_of_antinodes = []

max_x = len(lines[0])
max_y = len(lines)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            map_of_antennas.append((char, (x, y)))

sorted(map_of_antennas)


def add_antidotes_recursive(x_pos, y_pos, dis_x, dis_y):
    if x_pos < 0 or y_pos < 0:
        return False
    if x_pos >= max_x or y_pos >= max_y:
        return False

    map_of_antinodes.append((x_pos, y_pos))
    return add_antidotes_recursive(x_pos + dis_x, y_pos + dis_y, dis_x, dis_y)


def create_antinodes(current_antenna, all_antennas):
    first_antenna_symbol = current_antenna[0]
    first_x_pos = current_antenna[1][0]
    first_y_pos = current_antenna[1][1]

    for antenna in all_antennas:
        if antenna[0] == first_antenna_symbol and antenna is not current_antenna:
            second_x_pos = antenna[1][0]
            second_y_pos = antenna[1][1]

            add_antidotes_recursive(first_x_pos, first_y_pos, first_x_pos - second_x_pos, first_y_pos - second_y_pos)
            add_antidotes_recursive(first_x_pos, first_y_pos, second_x_pos - first_x_pos, second_y_pos - first_y_pos)


for a in map_of_antennas:
    create_antinodes(a, map_of_antennas)

for x in range(max_x):
    current_line = ''
    for y in range(max_y):
        if (x,y) in map_of_antinodes:
            current_line += '#'
            continue
        current_line += lines[x][y]
    print(current_line)

print(max_x, max_y)
print(map_of_antennas)
print(map_of_antinodes)
print(list(set(map_of_antinodes)))
print(len(list(set(map_of_antinodes))))