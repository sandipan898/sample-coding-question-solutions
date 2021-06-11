def find_factors(number):
    factors = list()
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            factors.append(i)
    factors.append(number)
    return factors

num = 100
# print("The factors of {} is {}".format(num, find_factors(num)))
print("The factors of {} are:".format(num), end=" ")
for factor in find_factors(num):
    print(factor, end=" ")
