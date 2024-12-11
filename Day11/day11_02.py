import math

inp = open('../Inputs/Input11.txt').read()

stones = [int(stone) for stone in inp.split()]

stones = sorted(stones)


def split_stone(stone):
    half_len = int(len(str(stone)) / 2)
    return int(str(stone)[:half_len]), int(str(stone)[half_len:])

stone_dict = {}
def blink(stone, steps_left):
    if steps_left <= 0:
        return 1

    if not (steps_left, stone) in stone_dict:
        if stone == 0:
            stone_dict[(steps_left, stone)] = blink(1, steps_left - 1)
        elif len(str(stone)) % 2 == 0:
            left, right = split_stone(stone)
            stone_dict[(steps_left, stone)] = blink(left, steps_left - 1) + blink(right, steps_left - 1)
        else:
            stone_dict[(steps_left, stone)] = blink(stone * 2024, steps_left - 1)
    return stone_dict[(steps_left, stone)]

print(sum(blink(stone, 75) for stone in stones))