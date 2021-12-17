

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

class Point(object):
    def __init__(self, cords):
        self.X_start = cords[0]
        self.Y_start = cords[1]
        self.X_end = cords[2]
        self.Y_end = cords[3]

    def check_hz(self):
        if self.X_start == self.X_end or self.Y_start == self.Y_end:
            return True
        else:
            return False

    def get_points_cov(self):
        if self.X_start == self.X_end:
            start = min(int(self.Y_start), int(self.Y_end))
            end = max(int(self.Y_start), int(self.Y_end))
            covered = []
            covered.append([int(self.X_start), start])
            for x in range(start, end):
                covered.append([int(self.X_start), x + 1])
            return covered
        if self.Y_start == self.Y_end:
            start = min(int(self.X_start), int(self.X_end))
            end = max(int(self.X_start), int(self.X_end))
            covered = []
            covered.append([start, int(self.Y_start)])
            for x in range(start, end):
                covered.append([int(x + 1), int(self.Y_start)])
            return covered

    def __str__(self):
        return "%s,%s -> %s, %s" % (self.X_start, self.Y_start, self.X_end, self.Y_end)
a = 0
b = 0
points = [x.replace(' -> ', ',') for x in lines]
for x in points:
    for j in x.split(','):
        if int(j) > b:
            b = int(j)
    
    if b > a:
        a = b

hits = [[False for i in range(a+1)] for i in range(a+1)]

filtered_points = []
covered_points = []
no_doubles = 0
i = 0

doubles = []
for point in points:
    line = Point(point.split(','))
    if Point.check_hz(line):
        filtered_points.append(line)

for point in filtered_points:
    line = Point.get_points_cov(point)
    for x in line:
        if hits[int(x[0])][int(x[1])] and x not in doubles:
            no_doubles += 1
            doubles.append(x) 
        else:
            hits[x[0]][x[1]] = True

print(no_doubles)