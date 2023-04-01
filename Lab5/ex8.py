import re

def contains_digit(string):
    pattern = re.compile(r"\d")
    return pattern.search(string) is not None



    # Example strings
string1 = "The quick brown fox jumps over the lazy dog1"
string2 = "Hello world!"

    # Check if strings contain a digit
print(contains_digit(string1))  # True
print(contains_digit(string2))  # False


