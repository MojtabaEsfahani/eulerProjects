from num2words import num2words

# counter = 0
# for i in range(359, 1001):
#     word = num2words(i)
#     for j in word:
#         if(j=='-' or j==' '):
#             continue
#         else:
#             counter +=1
            
# print(counter)

counter = 0
word = num2words(1000)
for j in word:
    if(j=='-' or j==' '):
        continue
    else:
        counter +=1
            
print(counter)