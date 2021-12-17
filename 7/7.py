

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

positions = lines[0].split(',')
diff = []

for pos in positions: 
    sum = 0
    for x in positions:
        sum += abs(int(pos)-int(x))
    diff.append(sum)

index_min = min(range(len(diff)), key=diff.__getitem__)

print(positions[index_min])
print(min(diff))