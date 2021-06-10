character = input("Enter a character: ")
    
def is_vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u'] or char in ['A', 'E', 'I', 'O', 'U']:
        return True
    return False

if is_vowel(character):
    print("{} is a Vowel".format(character))
else:
    print("{} is a Consonant".format(character))
    