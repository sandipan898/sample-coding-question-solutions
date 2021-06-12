def is_prime(number):
    if number in [0, 1]:
        return False
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True

def check_sum_of_prime(number):
    first_num = 0 
    second_num = number
    numbers = list()
    while second_num > int(number/2)-1:
        if is_prime(first_num) and is_prime(second_num):
            numbers.append((first_num, second_num))
        first_num += 1
        second_num -= 1
    return numbers

# num = 36
# num = 20
num = 50
prime_numbers = check_sum_of_prime(num)
if not prime_numbers:
    print("No prime number pair")
else:
    for nums in prime_numbers:
        print(nums)
