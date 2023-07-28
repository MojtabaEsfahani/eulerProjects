import os            
def primes(max):    
    sum = 0
    primes = [True] * max
    primes[0]=primes[1]=False
    for i in range(2, max):
        if primes[i] :
            for j in range(i**2, max, i):
                primes[j] = False;
            sum += i
    print(sum)
    
os.system('cls')
max = int(input("Enter a number as max :"))        
primes(max)

# 142913828922