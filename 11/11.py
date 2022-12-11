lines = [x.split()for x in open("input.txt")]
mon = [[]]

items = [''.join(x[2:]).split(',') for x in lines[1::7]]
op = [''.join(x[1:]) for x in lines[2::7]]
div = [int(x[-1:][0]) for x in lines[3::7]]
t = [int(x[-1:][0]) for x in lines[4::7]]
f = [int(x[-1:][0]) for x in lines[5::7]]
mon = [[items[i],op[i],div[i],t[i],f[i],0] for i in range(len(f))] 

old,new=0,0
for round in range(20):
    for m in mon:
        while m[0]:
            m[5]+=1
            old = int(m[0].pop(0))
            exec(m[1])
            new=new//3
            if new % m[2] == 0:
                mon[m[3]][0].append(str(new))
            else:
                mon[m[4]][0].append(str(new))

smon = sorted(mon, key = lambda x: x[5])
print(f'monbiz: {smon[-1][5] * smon[-2][5]}')

