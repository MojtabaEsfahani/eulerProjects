# Generate prime factors
def factors(number):
    factors = [];
    for integer in range(1, number):
        if(number%integer==0):
            factors.append(integer)
    print (factors);

factors = factors(10);
