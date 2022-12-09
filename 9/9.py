lines =[x.split()for x in open("input.txt")]

mov_dict = { 'L':(-1,0), 'R':(1,0), 'D':(0,-1), 'U':(0,1)}   
mov_t_dict = {(2,0):(1,0),(-2,0):(-1,0),(0,2):(0,1),(0,-2):(0,-1),
(2,1):(1,1),(1,2):(1,1),(-1,2):(-1,1),(-2,1):(-1,1),
(-2,-1):(-1,-1),(-1,-2):(-1,-1),(1,-2):(1,-1),(2,-1):(1,-1)}

pos_h, pos_t = [0,0],[0,0]

pos=[[0,0] for x in range (2)]

def add_mov(pos, mov):
    for i in range(2):
        pos[i] += mov[i]
    return pos

def mov_h(dir):
    global pos_h,pos_t
    pos_h = add_mov( pos_h, mov_dict[dir])
    dist = (pos_h[0] - pos_t[0], pos_h[1] - pos_t[1])
    if dist in mov_t_dict:
        pos_t = add_mov(pos_t, mov_t_dict[dist])

#PART 1
visited = set([(0,0)])
for l in lines:
    for n in range (int(l[1])):
        mov_h(l[0])
        visited.add((pos_t[0],pos_t[1]))

print(f'visited {len(visited)} unique coordinates')