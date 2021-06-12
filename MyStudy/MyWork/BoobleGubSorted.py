def func(arrange):
    n = 0
    while n < len(arrange):
        for i in range(len(arrange) - 1):
            if arrange[i] > arrange[i + 1]:
                x = arrange[i]
                arrange[i] = arrange[i + 1]
                arrange [i + 1] = x
        n += 1
    return arrange
