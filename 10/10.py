lines = iter([x.split()for x in open("input.txt")])

cycle, busy, x, add, s1, buf = 0, 0, 1, 0, 0, ''
check_on_cycle = (20, 60, 100, 140, 180, 220)

def get_pixel(pos):
    if pos in range (x,x+3): return '#' 
    return '.'

for i in range(240):
    if not busy:
        x += add
        l = next(lines)
        if l[0] == 'addx':
            add = int(l[1])
            busy += 1
        else: add = 0
    else: busy -= 1
    if i+1 in check_on_cycle: s1 += x * (i+1)
    imod = i % 40 +1
    if imod == 1: buf+='\n'
    buf+=get_pixel(imod)

print(f'task1: {s1}')
print(f'task2: {buf}')