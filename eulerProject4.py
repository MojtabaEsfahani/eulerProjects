import os
#generate palindromic numbers
def pali_numbers (min, max):
    com = 0;
    return_packet =""
    for first_number in range (min, max):
        for second_number in range (min, max):
            mul = first_number*second_number;
            if (mul == reverse(mul) and mul > com):
                com = mul;
                
    return ;


def reverse (int_number):
    String = str (int_number);
    re_String = String [::-1];
    return int (re_String);


os.system ('cls');
min = int(input("Enter a min range"));
max = int(input("Enter a max range"));
first_number, second_number, com = pali_numbers (min, max);
print ("{} * {} = {}".format(first_number, second_number, com));