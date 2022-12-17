lines = open("input.txt").read()
occupied = set()

def stream_dir(turn):
    return lines[turn % len(lines)]
    
rocks={ 0:[(0,0),(1,0),(2,0),(3,0)], 
        1:[(1,0),(0,1),(1,1),(2,1),(1,2)],
        2:[(0,0),(1,0),(2,0),(2,1),(2,2)], 
        3:[(0,0),(0,1),(0,2),(0,3)], 
        4:[(0,0),(1,0),(0,1),(1,1)]}

def add_tuples(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def move_x(turn, rock):
    mov = (-1,0) if lines[turn % len(lines)] == '<' else (1,0)
    new_rock = [add_tuples(x,mov) for x in rock ]
    if [x for x in new_rock if x in occupied or x[0]<0 or x[0]>6]: return rock
    else: return new_rock

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

def loop():
    no_of_rocks = 0
    turn = 0
    rock = []
    while no_of_rocks < 2023:
        if not rock:
            spawn = (2,max_height()+3)
            rock = [add_tuples(x,spawn) for x in rocks[no_of_rocks % len(rocks)]]
            no_of_rocks+=1 
        rock = move_x(turn, rock)
        new_rock = move_y(rock); turn+=1
        if not new_rock:
            for _ in range(len(rock)): occupied.add(rock.pop())
        else: rock = new_rock
    print(f'{max_height()}')

loop()
