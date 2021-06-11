def count_digit(number):
    count = 0
    while number > 0:
        number = int(number/10)
        count += 1
    return count 

def is_armstrong(number):
    num = number
    armstrong_number = 0
    length = count_digit(number)
    while number > 0:
        armstrong_number += (number % 10)**length
        number = int(number/10)
    print(armstrong_number)
    return armstrong_number == num
# num = 7
num = 153
# num = 1634
if(is_armstrong(num)):
    print("{} is an Armstrong Number".format(num))
else:
    print("{} is not an Armstrong Number".format(num))
