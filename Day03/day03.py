import re

text_input = open("Input03.txt", "r").read()

def multiplication(multiplier_list):
    return int(multiplier_list[0]) * int(multiplier_list[1])

total = 0
enabled = True
for mul in re.findall(r"(?<=mul\()\d+,\d+(?=\))|do\(\)|don't\(\)", text_input):
    print(mul)
    if mul == "do()":
        enabled = True
        continue
    if mul == "don't()" or enabled == False:
        enabled = False
        continue
    total += multiplication(mul.split(","))

print(total)
