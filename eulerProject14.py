# product Collatz Sequence and return length of chain

def collatz_seq(start_number):
    seq = []
    while(True):
        if (start_number%2 == 0):
            seq.append(start_number/2)
        else:
            seq.append((3*start_number)+1)
        if (seq[-1]==1) :
            return len(seq)
        start_number = seq[-1]
        
for i in range(1, 1000000):
    chain_len = collatz_seq(i)