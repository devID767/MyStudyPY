import math

def GetX():
    number = input('Enter the x\n')
    if number == 'pi':
        operation = input('Enter the operation: / or * or press enter\n')
        if operation == '/':
            a = int(input('Enter the num\n'))
            number = math.pi / a
        elif operation == '*':
            a = int(input('Enter the num\n'))
            number = math.pi * a
        else:
            number = math.pi
    elif number == 'e':
        operation = input('Enter the operation: / or * or press enter\n')
        if operation == '/':
            a = int(input('Enter the num\n'))
            number = math.e / a
        elif operation == '*':
            a = int(input('Enter the num\n'))
            number = math.e * a
        else:
            number = math.e
    else:
        number = float(number)
    return number

result = 0
endsumm = 0

equation = int(input('which equation do you want see?\n'))
nround = int(input('Enter the round number of result\n'))
x = GetX()

for n in range (1, 101):
    if equation == 1:
        result = 1/math.factorial(n*int(x))
    elif equation == 2:
        if math.sin(n * x) == 0:
            continue
        else:
            result = 1 / math.sin(n * x)
    elif equation == 3:
        if math.cos(n * x) == 0:
            continue
        else:
            result = 1 / math.cos(n * x)
    elif equation == 4:
        if x == 0:
            continue
        else:
            result = (-1)**n * 1/x
    elif equation == 5:
        if n * x <= -1 or n * x >= 1:
            continue
        elif math.acos(n * x) == 0:
            continue
        else:
            result = 1/math.acos(n * x)
    elif equation == 6:
        if x == 0:
            continue
        else:
            result = math.sin(n * x)/x
    elif equation == 7:
        if x == 0:
            continue
        else:
            result = math.cos(n*x)/x
    elif equation == 8:
        if x <= 0:
            continue
        result = n / math.factorial(x)
    elif equation == 9:
        if n * x <= 0:
            continue
        else:
            result = math.log(n * x)
    elif equation == 10:
        if x <= 0:
            continue
        else:
            result = math.log(x)/n*x
    elif equation == 11:
        result = (-1)**n*((x**(2*n+1))/math.factorial(2*n + 1))
    elif equation == 12:
        result = (-1)**n*((math.factorial(math.factorial(2*n-1)))*x**(2*n+1))\
                        /((math.factorial(math.factorial(2*n)))*(2*n+1))
    elif equation == 13:
        result = (-1)**(n+1)*x**n/n
    else:
        print('error')

    endsumm += result

print(round(endsumm, nround))
