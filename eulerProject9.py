import os
def generator():
    for a in range(1, 10000):
        for b in range(1, 10000):
            A = (1000-a-b)
            B = (a**2)+(b**2)
            if ((A**2) == B and A>a and A>b) :
                return (A*a*b)
os.system ('cls')                              
Ans = generator()
print ("There exists exactly one Pythagorean triplet for which :\n a+b+c=1000")
print ("the product abc is : {}".format(Ans))
# 31875000