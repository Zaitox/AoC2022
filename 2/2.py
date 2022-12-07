import csv

winmatrix=[[3, 6, 0], [0, 3, 6], [6, 0, 3]]
ineedtoplay=[[3, 1, 2],[1, 2, 3],[2, 3, 1]]

def val_of_letter(letter):
    match letter:
        case 'A' | 'X':
            return 1
        case 'B' | 'Y':
            return 2
        case 'C' | 'Z':
            return 3
    
def result(elf, me):
    return winmatrix[elf -1][me -1]

def what_i_should_play(elf, me):
    return ineedtoplay[elf-1][me-1]
    
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    highscore = 0
    for row in csv_reader:
        elf = val_of_letter(row[0])
        my_play = what_i_should_play(elf, val_of_letter(row[1]))
        
        myresult = result(elf, my_play)
        roundscore = my_play + myresult
        print(f'\telf: {elf}  me {my_play}.')
        print(f'my points this round: {roundscore}')
        highscore += roundscore
    print(f'highscore {highscore}')

