character = input("Enter a Character: ")

def is_alphabate(char):
    assert len(char) == 1, "Input should contain only one Character"
    # if (ord(char) >= 65 and ord(char) <=90) or (ord(char) >= 97 and ord(char) <= 122):
    if ord(char) in range(65, 91) or ord(char) in range(97, 123):
        return True
    return False

if is_alphabate(character):    
    print("{} is an Alphabate".format(character))
else:
    print("{} is not an Alphabate".format(character))
    