# solved with math formulas

import os

def factorial(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    return mul

def math_formula(n):
    a_possible = factorial(2*n)
    limit = factorial(n)
    ans = a_possible/(limit**2)
    return int(ans)

grid_n = int(input("determine an n value for n*n : "))
os.system('cls')
ans = math_formula(grid_n)
print("\nthere is {} possible way for a {}*{} grid \n".format(ans, grid_n, grid_n))