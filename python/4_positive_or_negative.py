def check_sign(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")

number = float(input("Enter a number: "))
check_sign(number)
