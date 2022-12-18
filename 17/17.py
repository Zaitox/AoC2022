lines = open("test.txt").read()
occupied = set()
max_y=0

def stream_dir(turn):
    return lines[turn % len(lines)]
    
rocks={ 0:[(0,0),(1,0),(2,0),(3,0)], 
        1:[(1,0),(0,1),(1,1),(2,1),(1,2)],
        2:[(0,0),(1,0),(2,0),(2,1),(2,2)], 
        3:[(0,0),(0,1),(0,2),(0,3)], 
        4:[(0,0),(1,0),(0,1),(1,1)]}

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def move_x(turn, rock):
    mov = (-1,0) if lines[turn % len(lines)] == '<' else (1,0)
    new_rock = [add_tuples(x,mov) for x in rock ]
    for x in new_rock:
        nx = x[0]
        if nx<0 or nx>6: 
            return rock
        elif x in occupied: 
            return rock
    return new_rock

def vis():
    for y in reversed(range(20)):
        line = ''
        for x in range (7):
            if (x,y) in occupied: line+='#'
            else: line+='.'
        print(line)

def move_y(rock):
    mov = (0,-1)
    new_rock = [add_tuples(x,mov) for x in rock ]
    if [x for x in new_rock if x in occupied or x[1]<0]: 
        return []
    return new_rock

def max_height():
    if occupied: return max([x[1] for x in occupied])+1
    else: return 0

def loop(rmax):
    global max_y
    no_of_rocks = 0
    turn = 0
    rock = []
    while no_of_rocks < rmax+1:
        if not rock:
            if (no_of_rocks % 100000 == 0): print(f'{no_of_rocks}')
            spawn = (2,max_y+3)
            rock = [add_tuples(x,spawn) for x in rocks[no_of_rocks % len(rocks)]]
            no_of_rocks+=1 
        rock = move_x(turn, rock)
        new_rock = move_y(rock); turn+=1
        if not new_rock:
            for _ in range(len(rock)): 
                r=rock.pop()
                occupied.add(r)
                if r[1]+1 > max_y: max_y = r[1]+1            
        else: rock = new_rock
    print(f'{max_y}')

loop(2022)
vis()
loop(1000000000000)
