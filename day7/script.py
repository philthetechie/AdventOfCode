current_dir = ['/']

filesystem = {
    '/':{'size': 0}
}

below100 = []
allsizes = []

def cd(path):
    global current_dir
    global filesystem
    if path == '..':
        current_dir.pop()
    elif path == '/':
        current_dir = ['/']
    else:
        current_dir.append(path)
        

def process_ls_line(line):
    global current_dir
    global filesystem
    cfs = filesystem
    for x in current_dir:
        if x not in cfs.keys():
            cfs[x] = {'size': 0}
        cfs = cfs[x]

    s, fn = line.split(' ')
    if s == 'dir':
        cfs[fn] = {'size': 0}
    else:
        cfs['size'] += int(s)

def get_sizes(d, p):
    global below100
    global allsizes
    size = d[p]['size']
    for x in [y for y in d[p].keys() if y != 'size']:
        try:
            size += get_sizes(d[p], x)
        except:
            pass
    allsizes.append(size)
    if size <= 100000:
        below100.append(size)
    return size


in_ls = False
with open('input.txt', 'r') as input:
    # part 1
    commands = input.read().split('\n')
    for command in commands:
        if in_ls:
            if command.find('$') == 0:
                in_ls = False
            else:
                process_ls_line(command)
                continue
        if command .find('$ ls') == 0:
            in_ls = True
            continue
        if command.find('$ cd ') == 0:
            cd(command.replace('$ cd ', ''))
    
    fs_size = get_sizes(filesystem, '/')

    # part 1
    print(sum(below100))

    # part 2:
    needed = 30000000 - (70000000 - fs_size)
    print([x for x in sorted(allsizes) if x >= needed][0])
