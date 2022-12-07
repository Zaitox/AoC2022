import csv

stack_line = []
stack = []
move = []
movement_indices = []

def find_movement_indices( index_line ):
    positions = index_line.split(" ")
    for p in positions:
        if p:
            movement_indices.append(index_line.find(p))

def fill_stack():

    for n in movement_indices:
        stack.append([])

    for sline in stack_line[::-1]:
        for i in range(len(movement_indices)):
            print(f'{int(movement_indices[i])}')
            text = sline[int(movement_indices[i])]
            print(f'{i}: {sline} {text}')
            if text != " ":
                stack[i].append(text)

def do_movements_cm9000():
    for m in move:
        for i in range(m[0]):
            stack[m[2]-1].append( stack[m[1]-1].pop())

def do_movements_cm9001():
    for m in move:
        temp_stack = []
        for i in range(m[0]):
            temp_stack.append(stack[m[1]-1].pop())
        for j in temp_stack[::-1]:
            stack[m[2]-1].append(j)

def print_top_of_stack():
    res = ''
    for s in stack:
        res+= s.pop()
    print(res)

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    movements_section_reached = False
    for row in csv_reader:
        print(f'new row')
        if not row:
            print(f'empty line')
            continue
        if movements_section_reached:
            move_parsed = row[0].split(" ")
            move.append([int(move_parsed[1]), int(move_parsed[3]), int(move_parsed[5])])
            continue
        else:
            if row[0].lstrip().startswith("1"):
                movements_section_reached = True
                find_movement_indices(row[0])
            else:
                stack_line.append(row[0])

    fill_stack()

    print(f'done: {stack_line}, {move}, {movement_indices}')

    print(f'stack: {stack}')
    
    do_movements_cm9001()

    
    print(f'stack: {stack}')
    
    print_top_of_stack()

