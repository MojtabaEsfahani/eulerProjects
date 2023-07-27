def generator():
    for a in range(1, 10000):
        for b in range(1, 10000):
            A = (1000-a-b)
            B = (a**2)+(b**2)
            if ((A**2) == B and A>a and A>b) :
                print ("okay")
                print (A, a, b, "\n")
                
                
generator()