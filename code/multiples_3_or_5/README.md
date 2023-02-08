# Multiples of 3 or 5

O problema do Multiples of 3 or 5 é somar todos os múltiplos de 3 ou 5 menores que 1000.

Problemas simples e para isso criei uma variavel maximo que recebe 1000 e criei um for que vai de i á maximo, todos os i's múltiplos de 3 ou 5 era somado na variavel sum e quando acaba o for é printado essa soma.

```
maximo = 1000
sum = 0
for i in range(maximo):
    if (i%3 == 0 or i%5==0):
        sum += i
print (sum)
```
