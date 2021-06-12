import random

while True:
    print('Проверка на совместимость')
    name1 = input('Введите первой имя\n')
    name2 = input('Введите второе имя\n')
    name_1 = name1.lower()
    name_2 = name2.lower()
    if name_1 == 'давид' and name_2 == 'даша' or name_1 == 'даша' and name_2 == 'давид':
        print(f'{name1} совместим с {name2} на 100%')
    elif name_1 == 'даша' or name_2 == 'даша':
        print(f'{name1} совместим с {name2} на 0%')
    else:
        print(f'{name1} совместим с {name2} на {random.randrange(0, 100)}%')
    input('Enter any key to continue')
