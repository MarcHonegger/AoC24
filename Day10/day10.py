inp = open('../Inputs/Input10.txt').read()
lines = inp.splitlines()

directions = [(-1,0), (0,1), (1,0), (0,-1)]

graph = {}
zeros_pos = []
max_x, max_y = len(lines[0]) - 1, len(lines) - 1
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '0':
            zeros_pos.append((y, x))
        if not (y, x) in graph:
            graph[(y, x)] = []
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                continue
            if int(lines[new_y][new_x]) == int(char) + 1:
                graph[(y, x)].append((new_y, new_x))

def count_part01(list_to_count):
    return len(set(list_to_count))

def count_part02(list_to_count):
    return len(list_to_count)

def calculate_count(count_func, find_all_distinct_paths=False):
    count = 0
    for zero_pos in zeros_pos:
        # print("\n", zero_pos)
        dots = graph[zero_pos]
        current_height = 1
        while current_height <= 9:
            # print(dots)
            current_height += 1
            new_dots = []
            for dot in dots:
                new_dots.extend(graph[dot])
            # print(new_dots)

            if current_height == 9:
                # print(new_dots, "Count: ", count_method(new_dots))
                count += count_func(new_dots)
                break
            if not new_dots:
                break
            dots = new_dots if find_all_distinct_paths else list(set(new_dots))
    return count


print("COUNT1: ", calculate_count(count_part01))
print("COUNT2: ", calculate_count(count_part02, True))