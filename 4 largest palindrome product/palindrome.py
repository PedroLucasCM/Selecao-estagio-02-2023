def pali_prod():
    pali = 0
    for n in range(100,999):
        for m in range(100, 999):
            y = n * m
            aux = str(y)
            if (aux == aux[::-1] and y>pali):
                pali = y
    return pali

print(pali_prod())