# Generate Fibonacci sequence
def fElements(max):

    firstNumber = 1 ;
    secondNumber = 1 ;
    thirdNumber = 1 ;

    while (thirdNumber<max):
    
        print(thirdNumber, " ,")
        thirdNumber = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = thirdNumber;

fElements(40)        
        