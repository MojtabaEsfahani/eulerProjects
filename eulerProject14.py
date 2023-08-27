# product Collatz Sequence and return length of chain

def collatz_seq(start_number):
    seq = [start_number]
    while(True):
        if (seq[-1]==1) :
            return len(seq)
        if (start_number%2 == 0):
            seq.append(start_number/2)
        else:
            seq.append((3*start_number)+1)
        start_number = seq[-1]
    
max = 0    
for i in range(1, 14):
    chain_len = collatz_seq(i)
    if (chain_len > max):
        max = chain_len
print (max)