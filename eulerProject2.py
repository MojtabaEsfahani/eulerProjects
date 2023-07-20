# Generate Fibonacci Sequence With Max-Value
import os;
def fElements(max):
    firstNumber = 1 ;
    secondNumber = 1 ;
    thirdNumber = 1 ;
    sumElement = 0;
    while (thirdNumber<max):
        thirdNumber = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = thirdNumber;
        if(firstNumber%2==0):
            sumElement += firstNumber;                
    return sumElement;

os.system('cls')
Max=input("\nchoice an Integer as Maximal-value : ");
try:
    Max=int(Max);
    ans = fElements(Max);
    print ("\n\n", ans, " is the sum of the even-valued terms.\n By considering in the Fibonacci sequence whose values do not exceed ", Max, ".\n\n")
except:
    print("Something Went Wrong !!!");
