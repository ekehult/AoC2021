
pos = (0, 0, 0) #hz, d, aim


with open('real_input.txt') as f:
    lines = f.readlines()
    lines = [x.strip().split(' ') for x in lines]

for line in lines:
    if line[0] == 'forward':
        pos = (pos[0] + int(line[1]), pos[1] + pos[2]*int(line[1]), pos[2])

    if line[0] == 'down': 
        pos = (pos[0], pos[1], pos[2] + int(line[1]))

    if line[0] == 'up': 
        pos = (pos[0], pos[1], pos[2] - int(line[1]))
    
result = pos[0]*pos[1]
print(result)