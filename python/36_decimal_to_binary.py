def decimal_to_binary(number): # 8
    power = 0
    sum = 0
    while number > 0: # 8, 4, 2, 1, 0 
        rem = (number%2) # 0, 0, 0, 1 
        sum += (10**power)*rem # 0, 0, 0, 0 + 10^3*1 = 1000
        number = number // 2 # 4, 2, 1, 0
        power += 1 # 1, 2, 3, 4
    return sum # 1000

# num = 7
# num = 8
# num = 23
num = 15
print("Binary representtion of {} is: {}".format(num, decimal_to_binary(num)))
