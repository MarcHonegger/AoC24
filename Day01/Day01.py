

text = open("../Inputs/input01.txt", "r").read().splitlines()
print(text)

left_side = []
right_side = []

for n in text:
    left_side.append(int(n.split()[0]))
    right_side.append(int(n.split()[1]))
left_side.sort()
right_side.sort()

sum = 0
for i in left_side:
    for j in right_side:
        sum += i if i == j else 0
print(sum)
