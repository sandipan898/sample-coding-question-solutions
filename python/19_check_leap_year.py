def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if is_leap_year(2000):
    print("Leap year")
else:
    print("Not a Leap year")
