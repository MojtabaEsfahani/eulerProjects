import os            
def primes(max):    
    prime = []
    primes = [True] * max
    primes[0]=primes[1]=False
    for i in range(2, max):
        if primes[i] :
            for j in range(i**2, max, i):
                primes[j] = False;
            prime.append(i)
    print(prime)
    
os.system('cls')
max = int(input("Enter a number as max :"))        
primes(max)