f = open("./input.txt", "r")
def add_elf():
  elves.append(0)
  

elves=[]
i=0
add_elf()

while(True):
    # Read a line.
    line = f.readline()
    # When readline returns an empty string, the file is fully read.
    if line == "":
        print("::DONE::")
        break
    # When a newline is returned, the line is empty.
    if line == "\n":
        add_elf()
        i=i+1
        continue
        
    # Print other lines.
    stripped = line.strip()
    elves[i] = elves[i] + int(stripped)

print(sorted(elves,  reverse=True))

highest= max(elves)
print (highest)

sorted_elves_highest_first= sorted(elves,  reverse=True)
top_3_elves = sorted_elves_highest_first[0:3] 

print(top_3_elves)
print("sum of top 3 elves:")
print(sum(top_3_elves))
f.close()

