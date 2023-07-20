# Generate Fibonacci sequence
def fElements(max):

    firstNumber = 1 ;
    secondNumber = 1 ;
    thirdNumber = 1 ;

    while (thirdNumber<max):
        thirdNumber = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = thirdNumber;
        
    return secondNumber

print (fElements(40)) 