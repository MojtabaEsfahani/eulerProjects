import os;

def dividend ():
    number=0;
    bul=True;
    while (bul or number==0):
        RANGE = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19];
        (bul)=False;
        number=number+20;
        for i in RANGE:
            if (number%i != 0):
                (bul)=True;
                break;
    print (number);
    
try:
    os.system('cls');
    # min = int(input("Enter an integer as min :"));
    # max = int(input("Enter an integer as max :"));
    dividend();    
except:
    print ("something went wrong !!!")