import csv

def in_range(number, start, end ):
    return start <= number <= end

def check_assignment_overlap_single_direction(a1, a2):
    for n in range(int(a1[0]) , int(a1[1])+1 ):
        if not in_range(n ,int(a2[0]) , int(a2[1])  ):
            return False
    return True    
    
def check_assignment_overlap(a1, a2):
    if check_assignment_overlap_single_direction(a1, a2) or check_assignment_overlap_single_direction(a2, a1):
        return True
    return False


def check_assignment_overlap2(a1, a2):
    for n in range(int(a1[0]) , int(a1[1])+1 ):
        if in_range(n ,int(a2[0]) , int(a2[1])  ):
            return True
    return False    


with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    overlap_sum = 0
    for row in csv_reader:
        elf1 = row[0].split("-")
        elf2 = row[1].split("-")
        overlap = check_assignment_overlap(elf1,elf2)
        if overlap:
            overlap_sum+=1
    print(f'done: overlaps: {overlap_sum}')


with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    overlap_sum = 0
    for row in csv_reader:
        elf1 = row[0].split("-")
        elf2 = row[1].split("-")
        overlap = check_assignment_overlap2(elf1,elf2)
        if overlap:
            overlap_sum+=1
    print(f'done: overlaps: {overlap_sum}')

