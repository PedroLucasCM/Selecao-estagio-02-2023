# Largest Palindrome Product

Para esse problema deve-se buscar o maior palindrome obtido a partir de uma multiplicação com número de 3 digitos.

Para isso criei a função pali_prod com 2 loops de 100 a 999 onde se multiplica os iteradores de cada loop e verifica se é palindromo e se o produto é maior que o maior pali (inicialmente 0) e se for pali recebe o valor de y. No final é printado a resposta, sendo ela: 906609.

```
def pali_prod():
    pali = 0
    for n in range(100,999):
        for m in range(100, 999):
            y = n * m
            aux = str(y)
            if (aux == aux[::-1] and y>pali):
                pali = y
    return pali
```