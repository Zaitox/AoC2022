import csv

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        parent.update_size(self.size)

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.c = []
        self.size = 0

    def update_size(self, s):
        self.size += s
        if self.parent:
            self.parent.update_size(s)

    def get_ch(self, name):
        for ch in self.c:
            if ch.name == name:
                return ch

    def add_ch(self, name, parent):
        self.c.append(Dir(name, parent))

    def add_f(self, name, size, parent):
        self.c.append(File(name, size, parent))

root = Dir('/', None)
cd = None

def do_cd(d):
    global cd
    match d:
        case "/":
            cd = root
        case "..":
            cd = cd.parent
        case _:
            cd = cd.get_ch(d)

def find_dir_with_size(dir, need_greater_than ,size, res_list):
    if need_greater_than and dir.size >= size or not need_greater_than and dir.size <= size:
        res_list.append(dir)
    for ch in dir.c:
        if isinstance(ch, Dir):
            res_list = find_dir_with_size(ch, need_greater_than, size, res_list)
    return res_list

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        line = row[0]
        if line.startswith('$ cd'):
            do_cd(line.split()[2])
        elif line.startswith('$ ls'):
            continue
        else:
            l = line.split()
            if l[0] == "dir":
                cd.add_ch(l[1], cd)
            else:
                cd.add_f(l[1], int(l[0]), cd)
    # PART ONE
    sum = 0
    for d in find_dir_with_size(root, False ,100000, []):
        sum += d.size
    print(f'total size: {sum}')
    # PART TWO
    total, needed = 70000000, 30000000
    free = total - root.size
    tobefreed = needed - free
    smol = 0
    for d in find_dir_with_size(root, True, tobefreed, []):
        if d.size < smol or smol == 0:
            smol = d.size
    print(f'smol: {smol}')
