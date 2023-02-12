# Even Fibonacci numbers

Para o problema do fibonacci precisa-se somar todos os números pares da sequência menores que 4 milhões. Para isso criei uma função que recebe a e b, e enquanto b for menor que 4 milhoes a função faz: se B for par então soma-se o b na variável 'sum'. Fora, então, do while a recebe b e b recebe a soma de a + b. A função retorna então essa soma. Chamo então a função em um print mostrando na tela a soma total.

```
def sum_fibo(a, b):
    sum = 0
    while b<4000000:
        if b % 2 == 0 :
            sum+=b        
        a, b = b, b+a
    return sum

print (sum_fibo(1,1))
```