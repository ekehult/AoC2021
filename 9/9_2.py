with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

global rows
rows = len(lines)
global cols 
cols = len(lines[0])
low_points = []
global checked
checked = [[False for i in range(cols)] for i in range(rows)]

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
        if min(to_check) == here: #Low point found
            low_points.append([i, j])



def check_basin(row, col, basin_list):
    adj = adjacent(row, col)
    for nbor in adj:
        to_check = checked[nbor[0]][nbor[1]]
        if to_check == False:
            if int(lines[nbor[0]][nbor[1]]) != 9:
                checked[nbor[0]][nbor[1]] = True
                basin_list.append(1)
                check_basin(int(nbor[0]),int(nbor[1]), basin_list)     
    return basin_list


basin_sizes = []

for point in low_points:
    basin_list = [1]
    row = point[0]
    col = point[1]
    checked[row][col] = True
    basin_sizes.append(sum(check_basin(row, col, basin_list)))

basin_sizes.sort()
largest = basin_sizes[-3:]
print(basin_sizes)
print(int(largest[0])*int(largest[1])*int(largest[2]))