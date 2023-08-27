from num2words import num2words

counter = 0
for i in range(359, 1000):
    word = num2words(i)
    for j in word:
        if(j=='-' or j==' '):
            continue
        else:
            counter +=1
            
