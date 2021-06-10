def is_even(num):
    return True if num % 2 == 0 else False

number = float(input("Enter a number: "))
if is_even(number):
    print("Even Number")
else:
    print("Odd Number")
