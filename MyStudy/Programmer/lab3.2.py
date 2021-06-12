def IsLetterUK(letter = ''):
    letter = letter.lower()
    if letter == 'а':
        return True
    elif letter == 'б':
        return True
    elif letter == 'в':
        return True
    elif letter == 'г':
        return True
    elif letter == 'д':
        return True
    elif letter == 'е':
        return True
    elif letter == 'є':
        return True
    elif letter == 'ж':
        return True
    elif letter == 'з':
        return True
    elif letter == 'и':
        return True
    elif letter == 'і':
        return True
    elif letter == 'й':
        return True
    elif letter == 'ї':
        return True
    elif letter == 'к':
        return True
    elif letter == 'л':
        return True
    elif letter == 'м':
        return True
    elif letter == 'н':
        return True
    elif letter == 'о':
        return True
    elif letter == 'п':
        return True
    elif letter == 'р':
        return True
    elif letter == 'с':
        return True
    elif letter == 'т':
        return True
    elif letter == 'у':
        return True
    elif letter == 'ф':
        return True
    elif letter == 'х':
        return True
    elif letter == 'ц':
        return True
    elif letter == 'ч':
        return True
    elif letter == 'ш':
        return True
    elif letter == 'щ':
        return True
    elif letter == 'ь':
        return True
    elif letter == 'ю':
        return True
    elif letter == 'я':
        return True
    else:
        return False

def longestWord(args):
    longest = ''
    for i in args:
        a = ''
        for simv in i:
            a += simv
        if len(a) > len(longest):
            longest = i
    return longest

def MoreCommonWord(args):
    repeatcommon = {}
    for i in range(0, len(args)):
        count = 1
        if args[i] in repeatcommon.values():
            continue
        for j in range(i + 1, len(args)):
            if args[i].lower() == args[j].lower():
                count += 1
        repeatcommon[count] = args[i]
    x = 0
    for i in repeatcommon:
        x = i
        if i > x:
            x = i
    return repeatcommon[x]

def WorkText(text, also = 'none'):
    words = 0
    characters = 0
    word = ''
    flag = 'out'
    listWords = []

    for letter in text:
        characters += len(letter)
        if letter != ' ' and flag == 'out' and IsLetterUK(letter):
            words += 1
            flag = 'in'
        elif IsLetterUK(letter) == False:
            flag = 'out'

        if flag == 'in':
            word += letter
        else:
            if word != '':
                listWords.append(word)
                word = ''
    if also == 'words':
        print(f'words = {words}')
    elif also == 'characters':
        print(f'characters = {characters}')
    elif also == 'all':
        print(f'characters = {characters}\n'
              f'words = {words}')
    else:
        print('Uncorrect command')
    return listWords

f = open('text1.txt', 'r', encoding= 'UTF-8')
text = f.read()
print(text)

listWords = WorkText(text, also= 'all')
print(f'longest word = {longestWord(listWords)}')
print(f'More common word = {MoreCommonWord(listWords)}')
