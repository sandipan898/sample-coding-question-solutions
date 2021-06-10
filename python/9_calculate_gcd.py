def calculate_gcd(num1, num2):
    if num1 == 0:
        return num2
    return calculate_gcd(num2%num1, num1)

numbers = input("Enter two numbers (separated by a space): ").split(" ")
print(calculate_gcd(int(numbers[0]), int(numbers[1])))
