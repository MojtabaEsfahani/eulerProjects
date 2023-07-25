def prime_number(numbers):
    pList = [2, 3]
    number=4
    while(len(pList)<numbers):
        (bul)=True;
        for i in pList:
            if (number%i==0):
                (bul)=False;
                break;
        if(bul):
            pList.append(number)
        number+=1
    print (pList[-1], "\n", len(pList))

    
prime_number(10001)