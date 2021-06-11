def reverse_number(number, prev_rev=0):
    if number > 0:
        rem = number % 10
        rev = prev_rev*10 + rem
        return reverse_number(int(number/10), rev)
    return prev_rev

def is_palindrome(number):
    return number == reverse_number(number)

# num = 1234
# num = 2552
num = 5227225
if is_palindrome(num):
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")
