lines = iter([x.split()for x in open("input.txt")])
cycle, busy, x, add, s1 = 0, 0, 1, 0, 0
check_on_cycle = (20, 60, 100, 140, 180, 220)
for i in range(1,221):
    if not busy:
        x += add
        l = next(lines)
        if l[0] == 'addx':
            add = int(l[1])
            busy += 1
        else: add = 0
    else: busy -= 1
    if i in check_on_cycle: s1 += x * i
print(f'task1: {s1}')