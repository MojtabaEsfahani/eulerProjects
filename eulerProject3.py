import os
# Generate prime factors
def factors(number, dividend):
    min = 2;
    for integer in range(min, number+1):
        if(dividend%integer==0):
        #     p=integer;
        # while(dividend%integer==0):
            
            dividend = dividend/integer;
            print (integer);
            af(number, dividend)
            
def af(number, dividend):
    if(int(dividend)==1):
                return ;
    factors(number, dividend);
    
try:
    os.system('cls')
    number=input("\nEnter an Integer Number : ");
    number=int(number);
    print ("The factors of", number, "are :\n\n");
    dividend = number;
    Max = factors(number, dividend);
    # print (Max)
except:
    print("Something Went Wrong !!!");
    
    
    # 600851475143
