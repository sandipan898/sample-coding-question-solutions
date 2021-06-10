def swap(num1, num2):
    num1 = num1 - num2
    num2 = num1 + num2
    num1 = num2 - num1
    return num1, num2

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
print("Before Swap: number1 = {}, number2 = {}".format(number1, number2))

number1, number2 = swap(number1, number2)
print("After Swap: number1 = {}, number2 = {}".format(number1, number2))
