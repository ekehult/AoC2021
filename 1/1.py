
with open('real_input.txt') as f:
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]

first_depth = lines[0]
count = 0
for line in lines[1:]:
    if first_depth < line:
        count +=1
    first_depth = line
print(count)
