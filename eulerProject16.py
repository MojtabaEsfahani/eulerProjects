import os

def n_power(base, power):
    mul = base
    for i in range(1, power):
        mul *= base
    return mul

def add_digits(string):
    sum = 0
    for i in string:
        sum += int(i)
    return sum

base = int(input("Enter an integer as base :\n"))
power = int(input("Enter an integer as power :\n"))
os.system('cls')
ans = n_power(2, 1000)
ans = add_digits(str(ans))
print("The sum of the digits of {} to the power of {} is {}".format(base, power, ans))