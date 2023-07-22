import os
#generate palindromic numbers
def pali_numbers (min, max):
    max_pali = 0;
    return_packet =""
    for first_number in range (min, max):
        for second_number in range (min, max):
            multiple = first_number*second_number;
            if (multiple==reverse(multiple) and multiple>max_pali):
                max_pali = multiple;
                return_packet = "{}*{}*{}".format(str(first_number), str(second_number), str(max_pali));
    return return_packet;

#return reverse of number
def reverse (int_number):
    String = str (int_number);
    re_String = String [::-1];
    return int (re_String);


os.system ('cls');
try:
    min = int(input("Enter an integer min range :"));
    max = int(input("Enter an integer max range (greater than {}) :".format(min)));
    answer = pali_numbers (min, max).split('*');
    if (answer[0] == ""):
        print ("There is no palindromic number between {} and {} is :".format(min, max))
    else:
        print ("The maximum palindromic number between {} and {} is :".format(min, max))
        print ("{} * {} = {}".format(answer[0], answer[1], answer[2]));
except:
    print ("something went wrong !!!")