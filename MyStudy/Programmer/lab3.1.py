def GetNumbers():
    arrange = []
    while True:
        number = input('Enter the num\n')
        if number == 'exit':
            break
        else:
            try:
                arrange.append(int(number))
            except ValueError:
                print("Incorrect value")
    return arrange

def Nnumber(args):
    arrange = []
    for i in args:
        if i >= 0:
            arrange.append(i)
    return arrange

def GetSomeNumbers(arrange, count):
    n = 0
    result = []
    if count == 0:
        return arrange
    for i in arrange:
        if n == count:
            break
        else:
            result.append(i)
            n += 1
    return result

def fsort(args, count = 0):
    arrange = Nnumber(args)
    for i in range(len(arrange)):
        lowest = i
        for a in range(i+1, len(arrange)):
            if arrange[a] < arrange[lowest]:
                lowest = a
        arrange[i], arrange[lowest] = arrange[lowest], arrange[i]
        print(arrange)
    return GetSomeNumbers(arrange, count)

#numlist = [6, -5, 3, 8, -3, -20, 40, 15, 22, 12, 5]
numlist = GetNumbers()
count = int(input('Enter count numbers of list\n'))
print(fsort(numlist, count))
