def get_vector(s):
    return [int(x) for x in s[0]]

m =[get_vector(x.split())for x in open("input.txt")]
mt=list( zip(*m))
xlen,ylen=len(m),len(m[0])

def invis(x,y):
    val = m[x][y]
    xl = val <= max(m[x][0:y])
    xr = val <= max(m[x][y+1:ylen])
    yu = val <= max(mt[y][0:x])
    yd = val <= max(mt[y][x+1:xlen])
    return xl and xr and yu and yd

def los(l,val):
    res = 0
    for i in range(len(l)): 
        if l[i] >= val: return res + 1
        else: res += 1 
    return res

def score(x,y):
    val = m[x][y]
    l = los( list(reversed(m[x][0:y])),val ) 
    r = los(m[x][y+1:ylen],val )
    u = los(list( reversed(mt[y][0:x])),val)
    d = los(mt[y][x+1:xlen],val)
    return l * r * u * d
#PART 1
sum = 0
for i in range(1, xlen-1):
    for j in range (1,ylen-1):
        if invis(i,j):
            sum +=1
print (f'vis trees: {xlen*ylen -sum}')    
#PART 2
sc = 0
for i in range(xlen):
    for j in range (ylen):
        s = score(i,j)
        if s > sc: 
            sc = s
print (f'max score: {sc}')    