# Generate Fibonacci sequence

firstNumber = 1 ;
secondNumber = 1 ;
thirdNumber = 1 ;


while (thirdNumber<40):
    
        print(thirdNumber, " ,")
        thirdNumber = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = thirdNumber;
        
        