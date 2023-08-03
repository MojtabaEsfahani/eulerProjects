# generate triangle numbers

def tri_num(n):
    sequence = []
    for i in range(10000, n+1):
        tri_number = (i*(i+1))/2
        tri_number = int(tri_number)
        sequence.append(tri_number)
    return sequence

def calc(sequence):
    for i in sequence:
        # factors = []
        t = 0
        for j in range(1, i+1):
            if(i%j == 0):
                # factors.append(j)
                t += 1
        # if(len(factors) > 200):
        if(t > 300):
            # print (factors)
            # print (len(factors))
            print (i ,"\n", t)
            # return 
        # print (i ,"\n", t)
        
sequence = tri_num(11000)
calc(sequence)


# print (sequence)