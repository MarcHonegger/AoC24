inp = open('../Inputs/Input12.txt').read()
lines = inp.splitlines()

# print(lines)

plant_dict = {}
for y, line in enumerate(lines):
    for x, plant in enumerate(line):
        if plant in plant_dict.keys():
            plant_dict[plant].append((x, y))
        else:
            plant_dict[plant] = [(x, y)]

groups = []
def part1():
    total = 0
    for plant in plant_dict.keys():
        while len(plant_dict[plant]) > 0:
            fences = 4
            area = 1
            x, y = plant_dict[plant][0]
            group = [(x, y)]
            plants_to_check = [(x, y)]
            while len(plants_to_check) > 0:
                # print(plants_to_check)
                new_plants = []
                for x_pos, y_pos in plants_to_check:
                    for other_x, other_y in plant_dict[plant]:
                        # Don't check self
                        if other_x == x_pos and other_y == y_pos:
                            continue
                        # Search for new neighbors
                        dist_x, dist_y = abs(other_x - x_pos), abs(other_y - y_pos)
                        if 0 <= dist_x <= 1 and 0 <= dist_y <= 1 and dist_x != dist_y:
                            # If already in group, remove fence
                            if (other_x, other_y) in group:
                                # print(f"x: {other_x}, y: {other_y} in group: {group}")
                                fences -= 2
                                continue

                            if not (other_x, other_y) in new_plants:
                                new_plants.append((other_x, other_y))
                                area += 1
                                fences += 4

                    # fences -= 2 * len(new_plants) - len(set(new_plants))
                group.extend(new_plants)
                group = list(set(group))
                plants_to_check = new_plants
            groups.append((plant, group))

            # print(plant_dict[plant])
            # print(group)
            plant_dict[plant] = [pos for pos in plant_dict[plant] if pos not in group]
            # print(f"A region of \033[95m {plant} \033[0m plants with price \033[95m {area} * {fences} = {area * fences}\033[0m")
            total += area * fences
    return total

def turn_left(direction):
    turn_left_dir = {(1, 0): (0, -1),
                     (0, -1): (-1, 0),
                     (-1, 0): (0, 1),
                     (0, 1): (1, 0)}
    return turn_left_dir[direction]

group_cache = {}

def is_surrounded(outer_group, surrounded_group):
    outer_set = set(outer_group)
    surrounded_set = set(surrounded_group)

    for x, y in surrounded_group:
        # Check all four adjacent cells (up, down, left, right)
        adjacent_cells = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for adj_x, adj_y in adjacent_cells:
            # If any adjacent cell is not part of the outer_group, it's not surrounded
            if (adj_x, adj_y) not in outer_set and (adj_x, adj_y) not in surrounded_set:
                return False

    return True

def calculate_group(group):
    # print(group)
    name, g = group
    direction = (1, 0)
    # print(name, g, 4)
    walls = 0
    start_pos = g[0][0], g[0][1] - 1
    x_pos, y_pos = start_pos
    start = True
    while ((x_pos, y_pos) != start_pos) or start:
        # print(x_pos, y_pos)
        next_x, next_y = x_pos + direction[0], y_pos + direction[1]

        if (next_x, next_y) in g:
            walls += 1
            direction = turn_left(direction)
            next_x, next_y = x_pos + direction[0], y_pos + direction[1]
            if (next_x, next_y) in g:
                walls += 1
                direction = turn_left(direction)
            next_x, next_y = x_pos, y_pos
        else:
            right_turn = turn_left(turn_left(turn_left(direction)))
            pot_x, pot_y = next_x + right_turn[0], next_y + right_turn[1]
            if (pot_x, pot_y) not in g:
                walls += 1
                direction = right_turn
                next_x, next_y = pot_x, pot_y


        if start and x_pos != next_x and y_pos != next_y:
            start = False

        x_pos, y_pos = next_x, next_y

    if direction != (1, 0):
        walls += 1

    last_x, last_y = g[0]
    used_coordinates = []
    for x, y in g:
        if x - last_x == 1:
            last_x = x
            last_y = y
        # print(f"last_x: {last_x}, last_y: {last_y}, x: {x}, y: {y} ")
        if (y - last_y) > 1:
            for i in range(last_y + 1, y):
                last_y += 1
                other_group = []
                print(f"Looking for \033[95m {last_x},{last_y} \033[0m to add to \033[95m {name}\033[0m")
                if not (last_x, last_y) in used_coordinates:
                    for other_g in group_cache.keys():
                        if (last_x, last_y) in other_g:
                            other_group = other_g
                            break
                    if not other_group:
                        for new_name, new_g in groups:
                            if (last_x, last_y) in new_g:
                                other_group = new_g
                                if not is_surrounded(g, other_group):
                                    continue
                                calculate_group((new_name, new_g))
                    if not is_surrounded(g, other_group):
                        continue
                        # print(" \033[95m adding:", group_cache[tuple(other_group)], "\033[0m")
                    walls += group_cache[tuple(other_group)]
                    used_coordinates.extend(other_group)
        last_x, last_y = x, y

    group_cache[tuple(g)] = walls
    print(
        f"A region of \033[95m {name} \033[0m plants with price \033[95m {len(g)} * {walls} = {len(g) * walls}\033[0m")

def part2():
    total = 0
    for n, group in groups:
        if tuple(group) in group_cache.keys():
            continue
        calculate_group((n, group))
    for g in group_cache.keys():
        total += len(g) * group_cache[g]

    return total

print("Part1:", part1())
print("\n")
groups = [(name, sorted(group)) for name, group in groups]
# print(groups)
print("Part2:", part2())
# print(group_cache)