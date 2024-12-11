import math

inp = open('../Inputs/TestInput11.txt').read()

stones = [int(stone) for stone in inp.split()]

def split_stone(stone):
    half_len = int(len(str(stone)) / 2)
    return int(str(stone)[:half_len]), int(str(stone)[half_len:])

stone_dict = {}
def blink():
    new_stones = []
        #print(old_stones)
    for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone * 2024)
    return new_stones

for i in range(25):
    print(stones)
    stones = blink()
print(len(stones))