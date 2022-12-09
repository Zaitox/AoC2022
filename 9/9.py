lines =[x.split()for x in open("input.txt")]
mov_dict = { 'L':(-1,0), 'R':(1,0), 'D':(0,-1), 'U':(0,1)}   

def mov_t(dist):
    if dist[0] in [-1,0,1] and dist[1] in [-1,0,1]: return (0,0)
    if dist[0] > 1 and dist[1]==0: return (1,0)
    if dist[0] < -1 and dist[1]==0: return (-1,0)
    if dist[1] > 1 and dist[0]==0: return (0,1)
    if dist[1] <-1 and dist[0]==0: return (0,-1)
    if dist[0] > 0 and dist[1] > 0: return (1,1)
    if dist[0] < 0 and dist[1] > 0: return (-1,1)
    if dist[0] > 0 and dist[1] < 0: return (1,-1)
    if dist[0] <0 and dist[1] < 0: return (-1,-1)
 
pos=[[0,0] for x in range (10)]

def add_mov(pos, mov):
    for i in range(len(pos)): pos[i] += mov[i]
    return pos

def mov_h(dir):
    pos[0] = add_mov( pos[0], mov_dict[dir])
    for i in range (1, len(pos)):
        dist = (pos[i-1][0] - pos[i][0], pos[i-1][1] - pos[i][1])
        pos[i] = add_mov(pos[i], mov_t(dist))

visited = [set([(0,0)]), set([(0,0)])]
for l in lines:
    for n in range (int(l[1])):
        mov_h(l[0])
        visited[0].add((pos[1][0],pos[1][1]))
        visited[1].add((pos[9][0],pos[9][1]))
print(f'tasl 1: {len(visited[0])}, task 2: {len(visited[1])}')