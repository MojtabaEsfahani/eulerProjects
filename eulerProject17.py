from num2words import num2words

counter = 0
for i in range(1, 1001):
    word = num2words(i)
    for j in word:
        if(j=='-' or j==' '):
            continue
        else:
            counter +=1
            
print(counter, " letters would be used from one to one thousand", sep ='')