import os
# Generate factors of a Number
def factors(number, dividend):
    min = 2;
    for integer in range(min, number+1):
        if(dividend%integer==0):            
            dividend = dividend/integer;
            factors_list.append(integer);
            return integer, dividend;

try:
    factors_list = [];
    multiplication = 1;
    os.system('cls');
    number=input("\nEnter an Integer Number : ");
    number=int(number);
    print ("\nThe factors of", number, "are :");
    dividend = number;
    while(multiplication != number):
        last_factor, dividend = factors(number, dividend);
        multiplication *= last_factor
    print (factors_list);
    print ("\nand The largest Factor is :", last_factor, "\n");
except:
    print("Something Went Wrong !!!")