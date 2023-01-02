import math

class Dir:
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        self.children = []
    def getChild(self, child):
        for check in self.children:
            if check.id == child:
                return check
    def getSize(self):
        size = 0
        for child in self.children:
            if isinstance(child, Dir):
                size += child.getSize()
            else:
                size += child.size
        return size

class File:
    def __init__(self, id, size, dir):
        self.id = id
        self.size = size
        self.dir = dir

with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

filesystem = Dir("/", None)
directory = filesystem

for line in data:
    words = line.split(" ")
    if line.startswith("$"):
        if words[1] == "cd":
            target = words[2]
            if target == "/":
                directory = filesystem
            elif target == "..":
                directory = directory.parent
            else:
                directory = directory.getChild(target)
    else:
        child = None
        if words[0] == "dir":
            child = Dir(words[1], directory)
        else:
            child = File(words[1], int(words[0]), directory)
        directory.children.append(child)
            
def printFileSystem(fileSystem, indent):
    for child in fileSystem.children:
        print(" " * indent * 2, child.id)
        if isinstance(child, Dir):
            printFileSystem(child, indent + 1)

def getAllDirectories(fileSystem):
    directories = []
    for child in fileSystem.children:
        if isinstance(child, Dir):
            directories.append(child)
            directories.extend(getAllDirectories(child))
    return directories

total = filesystem.getSize()

unused_space = 70000000 - total
required_to_delete = 30000000 - unused_space

optimal_size = 1000000000
for directory in getAllDirectories(filesystem):
    if directory.getSize() > required_to_delete and directory.getSize() < optimal_size:
        optimal_size = directory.getSize()

print(optimal_size)