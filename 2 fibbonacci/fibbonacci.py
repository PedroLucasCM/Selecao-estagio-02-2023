def sum_fibo(a, b):
    sum = 0
    while b<4000000:
        if b % 2 == 0 :
            sum+=b        
        a, b = b, b+a
    return sum

print (sum_fibo(1,1))
