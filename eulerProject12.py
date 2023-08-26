import math
def hash_divisors(number):
    sqrt_number = int(math.sqrt(number));
    t = 1;
    for i in range(1, sqrt_number+1):
        if number % i == 0:
            t += 1;
            if i != number/i:
                t += 1;
    if t>=500 :
        print (number," is the Answer", sep="")
        return False;
    else :
        return True;


number =1;
while (hash_divisors(number)):
    number +=1;
    