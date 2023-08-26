#  generate triangle numbers

# def tri_num(n):
#     sequence = []
#     for i in range(10000, n+1):
#         tri_number = (i*(i+1))/2
#         tri_number = int(tri_number)
#         sequence.append(tri_number)
#     return sequence

# def calc(sequence):
#     for i in sequence:
#          factors = []
#         t = 0
#         for j in range(1, i+1):
#             if(i%j == 0):
#                  factors.append(j)
#                 t += 1
#          if(len(factors) > 200):
#         if(t > 300):
#              print (factors)
#              print (len(factors))
#             print (i ,"\n", t)
#              return 
#          print (i ,"\n", t)
        
#  sequence = tri_num(11000)
#  calc(sequence)


#  print (sequence)


# import time

# st = time.time()
# def tri_num(i):
#     # tri_number = (i*(i+1))/2
#     # tri_number = int(tri_number)
#     # tri_number = int((i*(i+1))/2)
#     # return int((i*(i+1))/2)
    
    
# for i in range(1, 100000):
#     tri_number = tri_num(i)
#     print (tri_number)
# et = time.time()

# res = et - st
# print('CPU Execution time:', res, 'seconds')





# def lang():
#     p = 1
#     i = 2
#     while(calc(p)):
#         p +=i
#         i+=1
        
# def calc(num):
#     t = 0
#     for j in range(1, num+1):
#         if(num%j == 0):
#             t += 1
#     if(t > 40):
#         print (num ,"\n", t) 
#         return False
#     return True



# lang()

import math

# def calc (number):
#     for i in range(1, number+1):
#         if (number%i == 0):
#             print(i);        

def hash_divisors(n):
    sqrt_n = int(math.sqrt(n));
    t = 1;
    for i in range(1, sqrt_n+1):
        if n % i == 0:
            t += 1;
            if i != n/i:
                t += 1;
    
    if t >= 500:
        print(n);


number = 1;
for i in range(2, 10000000000):
    number +=i;
    hash_divisors(number);
    