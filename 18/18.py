import csv
points = set()
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        points.add((int(row[0]),int(row[1]),int(row[2])))

surface = 0
for p in points:
    val = 6
    for x in [-1,1]:
        if (p[0]+x,p[1],p[2]) in points:
            val -= 1
    for y in [-1,1]:    
        if (p[0],p[1]+y,p[2]) in points:
            val -= 1
    for z in [-1,1]:    
        if (p[0],p[1],p[2]+z) in points:
            val -= 1
    surface += val

print(f'{surface}') 

