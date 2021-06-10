def find_greatest_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

print(find_greatest_of_three(12, 54, 37))
print(find_greatest_of_three(15, 34, 28))
print(find_greatest_of_three(17, 36, 64))
