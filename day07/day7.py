class Directory:
    def __init__(self, name, directories=None, files=None, parent=None):
        self.name = name
        self.directories = directories if directories else dict()
        self.files = files if files else list()
        self.parent = parent
        self.size = None

    def update_size(self):
        self.size = sum(i.get_size() for i in self.directories.values()) + sum(i.size for i in self.files) 

    def get_size(self):
        self.update_size()
        return self.size

    def add_directory(self, directory):
        self.directories[directory.name] = directory
        self.update_size()

    def add_file(self, file):
        self.files.append(file)
        self.update_size()

    def __repr__(self) -> str:
        return f'dir {self.name}: {list(self.directories.keys())}, {self.files}'

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f'file {self.name} {self.size}'

with open('input.txt', 'r') as f:
    raw_input = f.read()

root = Directory('')
current_path = '/'
current_dir = root

for line in raw_input.splitlines():
    if line.startswith('$'):
        line = line.split()
        cmd = line[1]
        if cmd == 'cd':
            dst = line[2]
            if dst == '..':
                sep_idx = current_path[:-1].rindex('/')
                current_path = current_path[:sep_idx+1]
                current_dir = current_dir.parent 
            elif dst == '/':
                current_path = '/'
            else:
                current_path += dst + '/'
                current_dir = current_dir.directories[dst]
        elif cmd == 'ls':
            continue
    else:
        if line.startswith('dir'):
            name = line.split()[1]
            current_dir.add_directory(Directory(name, parent=current_dir))
        else:
            size, name = line.split()
            current_dir.add_file(File(name, int(size)))


# Part 1

to_search = [root]

dir_sizes = []
total = 0

total_size = 70000000

while to_search:
    current_dir = to_search[0]
    to_search = to_search[1:]
    cur_size = current_dir.get_size()
    dir_sizes.append(cur_size)
    if cur_size <= 100000:
        total += cur_size
    
    to_search.extend(current_dir.directories.values())

used_size = root.get_size()

print(total)
dir_sizes.sort()
print(used_size)
print(dir_sizes)
print([i for i in dir_sizes if (total_size - used_size + i) >= 30_000_000])

# Part 2



