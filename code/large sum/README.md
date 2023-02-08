# Large Sum

O problema do Large Sum é pegar um int gigantesco de 150 mil digitos e mostrar a soma dos 10 primeiros digitos.

Para isso eu peguei o número e o transformei em String, criei um contador e fiz um for que rodasse o tamanho dessa String. O contador então ia somando 1 a cada for e se chegasse em 10 parava o for, mas enquanto isso ia somando os digitos do interador i. Depois do for tem um print da soma.

```
for i in str:
    print (":" + i)
    if cont == 10: 
        break
    else:
        sum+=int(i)
        cont+=1
```
