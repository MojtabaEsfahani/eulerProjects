def user() :

    result = 0;
    anzahl=0;
    for i in range (1, 1000):
        if((i%3)==0 or (i%5)==0):
            result+= i;
            anzahl+= 1;
        

    print("\n######### The First Euler Project #########\n");
    print("The Result :", result);
    print("The Number Of Numbers : ", anzahl);



user    ();