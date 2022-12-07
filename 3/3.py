import csv

def findCommonItem(l,r):
    for item in l:
        if (item in r):
            print (f'common item: {item}')
            return item

def find_common_item_in_group(r1,r2,r3):
    for item in r1:
        if (item in r2 and item in r3):
            print (f'common item: {item}')
            return item


    
def val_of_item(item):
    prio = ord(item)
    if(str.islower(item)):
        prio = prio - 96
    else:
        prio = prio - 38
    print (f'prio {prio}')
    return prio

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    prio_sum = 0
    for row in csv_reader:
        halflength = int(len(row[0]) /2)
        l,r = row[0][:halflength], row[0][halflength:] 
        common_item = findCommonItem(l,r)
        prio_sum = prio_sum + val_of_item(common_item)
    print(f'done - sum: {prio_sum}')

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    rucks = [[],[],[]]
    prio_sum = 0
    i = 0
    for row in csv_reader:
        ruck_to_investigate = i % 3
        rucks[i%3].append(row[0])
        i+=1
    no_of_teams = len(rucks[0])
    for i in range(no_of_teams):
        r1,r2,r3 = rucks[0][i],rucks[1][i],rucks[2][i]
        item = find_common_item_in_group(r1,r2,r3)
        prio_sum += val_of_item(item)
    print(f'done - sum: {prio_sum}')
  

