def Contain(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    letters = []
    for i in word2:
        letters.append(i)
    for i in word1:
        if i in letters and len(word1) == len(word2):
            x = f'{word1} contain {word2}'
        else:
            x = f"{word1} don't contain {word2}"
    print(x)
Contain("Worlds", "Sorldw")