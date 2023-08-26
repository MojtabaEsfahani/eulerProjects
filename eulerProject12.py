
def hash_divisors(n):
    sqrt_n = int(math.sqrt(n));
    t = 1;
    for i in range(1, sqrt_n+1):
        if n % i == 0:
            t += 1;
            if i != n/i:
                t += 1;
    
    if t >= 500:
        print(n);


number = 1;
for i in range(2, 10000000000):
    number +=i;
    hash_divisors(number);
    