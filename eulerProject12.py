# generate triangle numbers

def tri_num(n):
    sequence = []
    for i in range(1, n+1):
        tri_number = (i*(i+1))/2
        tri_number = int(tri_number)
        sequence.append(tri_number)
    return sequence

def calc(sequence):
    for i in sequence:
        factors = []
        for j in range(min, i+1):
            if(i%j == 0):
                factors.append(j)
        if(len(factors) > 5):
            print (factors)
            return 
        
# for i in range(1, 10):
#     sequence.append(tri_num(i))
sequence = tri_num(5)
# calc(sequence)
print (sequence)