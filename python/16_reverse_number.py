"""
num = 134:
rev = 4, num = 13
4 * 10 + 3 = 43
43 * 10 + 1 = 431
"""

# def find_reverse_number(number):
#     reversed_number = 0
#     while number>0:
#         rem = number % 10
#         reversed_number = reversed_number * 10 + rem
#         number = int(number / 10)
#     return reversed_number

def find_reverse_number(number, rev = 0): 
    if number > 0:
        rem = number % 10 # rem = 4, 3, 1
        rev = rev * 10 + rem # rev = 4, 43, 431
        return find_reverse_number(int(number/10), rev) # frn(13, 4) ---> frn(1, 43) ---> frn(0, 431)
    return rev 
    
print(find_reverse_number(146))
print(find_reverse_number(99542))
