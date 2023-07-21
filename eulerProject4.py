#generate palindromic numbers
def pali_numbers():
    for x in range(min_x, 100):
        for y in range(min_y + 1, 100):
            mul = x*y;
            String = str(mul);
            re_String = String[::-1];
            if (String==re_String):
                return String, x, y;
    loop = False;
            
loop = True;
min_x = 10;
min_y = 10;
while (loop):
    pali_number, min_x, min_y = pali_numbers();
    print ("{} * {} = ".format(min_x, min_y), pali_number);