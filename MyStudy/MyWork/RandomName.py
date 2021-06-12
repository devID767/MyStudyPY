import random

def AddName(namelist):
    member = ''
    while True:
        namelist = input('Enter the name\n')
        if member == 'exit':
            break
        namelist.append(member)
    return namelist

def AddName(directory):
    file = open(f'{directory}', 'r', encoding='UTF-8')
    text = file.read()
    names = text.split()
    newNames = []
    for i in names:
        i = i.replace(',', '')
        newNames.append(i)
    return newNames

def CheckName(namelist):
    wasmembers = []
    for i in namelist:
        while True:
            randnum = random.randrange(0, len(namelist))
            if i != members[randnum] and randnum not in wasmembers:
                wasmembers.append(randnum)
                break
        print(f'The {i} and {namelist[randnum]}')


members = ['david', 'dasha', 'andriy', 'sofa', 'seriy', 'kiril', 'nastya', 'timur']
#namelist = AddName(r'C:\Users\david\Desktop\Names.txt')
CheckName(members)
