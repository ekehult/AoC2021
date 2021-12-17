import math

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

a =[]
positions = lines[0].split(',')
for x in positions: 
    a.append(int(x))

max_pos = max(a)
diff = []

for pos in range(1, max_pos): 
    sum = 0
    for x in positions:
        fact = 0
        steps = abs(int(pos)-int(x))
        for i in range(1, steps+1):
            fact += + i
        sum += fact

    diff.append(sum)


print(min(diff))
