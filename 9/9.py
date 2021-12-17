with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]
risk = 0
global rows
rows = len(lines)
global cols 
cols = len(lines[0])

def adjacent(row, col):
    down = [row+1, col]
    up = [row-1, col]
    right = [row, col+1]
    left = [row, col-1]
    neighbours = []
    if int(down[0]) < rows:
        neighbours.append(down)
    if int(up[0]) >= 0:
        neighbours.append(up)
    if int(right[1]) < cols:
        neighbours.append(right)
    if int(left[1]) >= 0:
        neighbours.append(left)
    return neighbours
    
for i in range(0, rows):
    for j in range(0, cols):
        to_check = []
        adj = adjacent(i, j)
        here = int(lines[i][j])
        to_check.append(here)
        for nbor in adj:
            to_check.append(int(lines[nbor[0]][nbor[1]]))
        if min(to_check) == here:
            count = 0
            for k in to_check:
                if k == here:
                    count += 1
            if count < 2:
                risk += here + 1 

print(risk)