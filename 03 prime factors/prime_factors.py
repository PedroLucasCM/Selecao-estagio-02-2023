def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False    
    return True

def prime_factor(x, i):
    if x==1:
        return x
#    print()
#    aux = str(x)
#    print ("auxiliar = ", aux)
#    tam = len(aux)
#     y = int(aux[tam-1])
    # print("ESSE È O Y: ",y)
    # print("ESSE È O X: ",x)
    
    while (x!=1 and i<=int(x**0.5)+1):
        if (x%i==0 and isPrime(i)):
         #   print ("valor inteiro de x: ", x) #verificar x
           # print ("fator primo: ", i) #verificar qual o modulo i
            x = x/i
        #    print (x) #verificar x
        else:
            i+=1
    return int(x)
    
print("o maior fator primo é", prime_factor(600851475143,1)) 