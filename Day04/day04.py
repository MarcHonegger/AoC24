test_text = open("TestInput04.txt", "r").read()
text = open("Input04.txt", "r").read()
texts = [test_text, text]


def check_character_for_xmas(array_to_search, coordinates):
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    count = 0

    for vector in vectors:
        x = coordinates[0]
        y = coordinates[1]
        word = ""
        temp_used_indexes = []

        for i in range(0, 4):
            temp_used_indexes.append((x, y))
            if 0 <= x < len(array_to_search) and 0 <= y < len(array_to_search[x]):
                word += array_to_search[x][y]
                if word == "XMAS":
                    count += 1
                    for temp in temp_used_indexes:
                        used_indexes.append(temp)

            if not word in ["X", "XM", "XMA"]:
                    break

            x += vector[0]
            y += vector[1]
    return count

def check_character_for_x_shaped_mas(array_to_search, coordinates):
    vectors = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    diagonal_characters = [c for c in [array_to_search[coordinates[0] + v[0]][coordinates[1] + v[1]] for v in vectors] if c in ["M", "S"]]
    if len(diagonal_characters) == 4:
        print(diagonal_characters)
        if diagonal_characters[0] != diagonal_characters[2] and diagonal_characters[1] != diagonal_characters[3]:
            return 1
    return 0

for t in texts:
    used_indexes = []
    result = 0
    result2 = 0
    string_with_used_characters = ""
    lines = t.splitlines()
    character_matrix = [[0 for y in range(len(lines))] for x in range(len(lines[0]))]
    for (y, line) in enumerate(lines):
        for (x, character) in enumerate(line):
            character_matrix[x][y] = character

    for (y, line) in enumerate(lines):
        for (x, character) in enumerate(line):
            if character == "X":
                result += check_character_for_xmas(character_matrix, (x, y))


    for (y, line) in enumerate(lines):
        for (x, character) in enumerate(line):
            if character == "A" and y != 0 and y != len(lines) - 1 and x != 0 and x < len(lines[0]) - 1:
                result2 += check_character_for_x_shaped_mas(character_matrix, (x, y))

    for (y, line) in enumerate(lines):
        string_with_used_characters += "\n"
        for (x, character) in enumerate(line):
            if (x, y) in used_indexes:
                string_with_used_characters += character
            else:
                string_with_used_characters += "."

    print(result)
    print(result2)
