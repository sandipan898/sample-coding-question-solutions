def calculate_gcd(num1, num2):
    if num1 == 0:
        return num2
    return calculate_gcd(num2%num1, num1)

def calculate_lcm(num1, num2):
    return (num1 * num2) / calculate_gcd(num1, num2)

numbers = input("Enter two numbers (separated by a space): ").split(" ")
print(calculate_lcm(int(numbers[0]), int(numbers[1])))
