with open('real_input.txt') as f:
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]

first_depth = sum(lines[0:2])
count = 0
for line in lines[1:-2]:
    first_elem = lines.pop(0)
    second_depth = first_elem + lines[0] + lines[1]
    if first_depth < second_depth:
        count +=1
    first_depth = second_depth
print(count)
