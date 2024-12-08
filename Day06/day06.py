import copy

lines = open('../Inputs/Input06.txt').read().splitlines()

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
rotations = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
obstacle_rotations = {'^': 'down', '>': 'left', 'v': 'up', '<': 'right'}
current_direction = 'x'
player_position = (-1, -1)
loop_count = 0
player_map = []

def print_map():
    for l in player_map:
        print(l)
    print("\n")

def create_map(input_lines):
    new_map = [['O'] * (len(input_lines) + 2)]

    for l in input_lines:
        new_map.append(['O'])
        for character in l:
            if character in directions.keys():
                global current_direction
                current_direction = character
                global player_position
                player_position = (len(new_map) - 1, len(new_map[-1]))

            new_map[-1].append(character)
        new_map[-1].append('O')

    new_map.append(new_map[0])
    return new_map


def change_symbol_in_map(position, symbol):
    global player_map
    player_map[position[0]][position[1]] = symbol


def move_player(position, new_position):
    change_symbol_in_map(position, 'X')
    change_symbol_in_map(new_position, current_direction)
    global player_position
    player_position = new_position


def rotate_player(position, direction):
        new_direction = rotations[direction]
        change_symbol_in_map(position, new_direction)
        global current_direction
        current_direction = new_direction


def perform_next_move(position, direction):
    new_x_pos = position[0] + directions[direction][0]
    new_y_pos = position[1] + directions[direction][1]
    new_position = (new_x_pos, new_y_pos)
    next_position = player_map[new_x_pos][new_y_pos]

    # no obstacle
    if next_position in ['X', '.', 'O']:
        # print("Moved from: ", position, " to ", (new_x_pos, new_y_pos))
        move_player(position, new_position)

        # out of bound
        return next_position != 'O'

    # obstacle
    if next_position == '#':
        # print("Rotated 90 degree")
        change_symbol_in_map(new_position, [obstacle_rotations[current_direction]])
        rotate_player(position, direction)
        #print_map()
        return True

    # Loop
    # print_map()
    if obstacle_rotations[current_direction] in next_position:
        global loop_count
        loop_count += 1
        return False
    else:
        change_symbol_in_map(new_position, [obstacle_rotations[current_direction]] + next_position)
        rotate_player(position, direction)
        return True

# print("map: ", create_map(lines))
created_map = create_map(lines)
saved_player_position = player_position
saved_directions = current_direction

player_map = [row[:] for row in created_map]

while perform_next_move(player_position, current_direction):
    pass

count_of_X = 0
for line in player_map:
    for c in line:
        if c == 'X':
            count_of_X += 1

print(count_of_X)

part1_player_map = player_map

for y, line in enumerate(part1_player_map):
    print(y + 1, "/", len(part1_player_map))
    for x, char in enumerate(line):
        if char == 'X' and (y, x) != saved_player_position:
            player_map = [row[:] for row in created_map]
            player_position = saved_player_position
            current_direction = saved_directions
            player_map[y][x] = '#'
            while perform_next_move(player_position, current_direction):
                pass

print(loop_count)