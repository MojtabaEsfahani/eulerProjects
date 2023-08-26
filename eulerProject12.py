import math


def hash_divisors(number):
    sqrt_number = int(math.sqrt(number))
    t = 0
    for i in range(1, sqrt_number+1):
        if number % i == 0:
            t += 1
            if i != number/i:
                t += 1
    if t >= 500:
        print(number, " is the Answer", sep="")
        return True
    else:
        return False


def create_numbers(number):
    number = (number*(number+1))/2
    return int(number)


# number = 1
# for i in range(2, 10000000000):
#     number +=i
#     con = hash_divisors(number)
#     if (con) :
#         break


counter = 1
while(True):
    Ans = create_numbers(counter)
    counter += 1
    if (hash_divisors(Ans)):
        break
