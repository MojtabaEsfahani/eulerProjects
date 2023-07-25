def plus(el):
    sum = 0
    if (el):
        for i in range(1, 101):
            sum += i
        return (sum**2)
    else:
        for i in range(1, 101):
            sum += (i**2)
        return (sum)

B = plus(False)
A = plus(True)

print (A-B);