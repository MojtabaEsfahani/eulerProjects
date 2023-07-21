import os
# Generate factors of a Number
def factors(number, dividend):
    min = 2;
    for integer in range(min, number+1):
        if(dividend%integer==0):            
            dividend = dividend/integer;
            print (integer, " ,", sep="");
            return integer, dividend;

try:
    Mal = 1;
    os.system('cls');
    number=input("\nEnter an Integer Number : ");
    number=int(number);
    print ("The factors of", number, "are :\n\n");
    dividend = number;
    while(Mal!=number):
        Max, dividend = factors(number, dividend);
        Mal *= Max
except:
    print("Something Went Wrong !!!");
    
    
    # 600851475143
