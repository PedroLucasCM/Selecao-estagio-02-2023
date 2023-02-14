# Largest Prime Factor
Para o problema de fatores primos é preciso saber o maior fator primo do número 600851475143.

Para isso, primeiro escrevi uma função para descobrir se um número 'n' é primo. Se 'n' for menor ou igual a 1 então a função retorna falso, já que 1 e número menores não são primos. Logo fiz um loop que vai de 2 (primeiro número primo) à raiz quadrada de 'n' + 1 já que um número não consegue ser dividido por números maiores que a própria raiz quadrada e continuar inteiro. Dentro do loop há uma condição if, se não sobrar resto em uma divisão de 'n' por i então ele é divisivel por i (diferente de 'n') tornando-o um não primo. Se todas as condições estiverem satisfeitas então a função retorna verdadeiro para o número 'n' ser primo.

```
def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False    
    return True
´´´

Depois criei uma função que verifica os fatores primos de 'x' ou no caso do problema 600851475143.
Na função se x for um ele ja retorna x. Caso contrário, entra em um loop de while (enquanto x for diferente de 1 e i for menor ou igual a raiz de x + 1) que verifica se i é primo e se a divisão de x por i não deixa resto. Se as condições estiverem cumpridas então x recebe x dividido por i, se não, soma-se 1 para i. No final retorna-se x. Na 'main' coloquei o print de x.

´´´
def prime_factor(x, i):
    if x==1:
        return x
    while (x!=1 and i<=int(x**0.5)+1):
        if (x%i==0 and isPrime(i)):
            x = x/i
        else:
            i+=1
    return int(x)
´´´