lines = [x.split()for x in open("input.txt")]
field = set()

def draw_line(start_p, end_p):
    shape = list(zip([int(x) for x in start_p],[int(x) for x in end_p]))
    x_sorted = sorted([shape[0][0],shape[0][1]])
    y_sorted = sorted([shape[1][0],shape[1][1]])

    for x in range(x_sorted[0], x_sorted[1]+1):
        for y in range(y_sorted[0], y_sorted[1]+1):
            field.add((x,y))

for l in lines:
    points = [x for x in l if x != '->']
    for i in range(1, len(points)):
        p1,p2 = points[i-1].split(','),points[i].split(',')
        draw_line(p1, p2)

def test_collision_down(point):
    obstacles = [x for x in field if x[0] == point[0] and x[1]>point[1]]
    nearest = sorted(obstacles, key=lambda a: a[1])
    return nearest[0] if nearest else [] 

def test_collision_point(point):
    return point in field

def simulate_sand(s):
    rest = False
    while not rest:
        obst_d = test_collision_down(s)
        if obst_d: s = (s[0], obst_d[1]-1)
        else: return (-1,-1)
        attempt_l, attempt_r = (s[0]-1,s[1]+1),(s[0]+1,s[1]+1)
        if not attempt_l in field:
            s = attempt_l
            continue
        elif not attempt_r in field:
            s = attempt_r
            continue
        else: return s

start = (500,0)
sand_count=0
while True:
    res = simulate_sand(start)
    if res == (-1,-1):
        print(f'part1: {sand_count}')
        break
    else:
        field.add(res)
        sand_count+=1
