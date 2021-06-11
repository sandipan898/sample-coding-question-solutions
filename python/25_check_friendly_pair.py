def find_perfect_divisors(number):
    divisors = list()
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def find_abundancy_index(number):
    sum_of_divisors = 0
    divisors = find_perfect_divisors(number)
    for divisor in divisors:
        sum_of_divisors += divisor
    return sum_of_divisors//number

def is_friendly_pair(n, m):
    abd_index_n = find_abundancy_index(n)
    abd_index_m = find_abundancy_index(m)
    return abd_index_n == abd_index_m

# number1 = 6
# number2 = 28

# number1 = 60
# number2 = 84

number1 = 220
number2 = 284

if is_friendly_pair(number1, number2):
    print("The numbers {} and {} form a Friendly Pair".format(number1, number2))
else:
    print("The numbers {} and {} cannot form a Friendly Pair".format(number1, number2))
