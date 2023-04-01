import re

def ends_with_digit(string):
    pattern = re.compile(r"\d$")
    return pattern.search(string) is not None



    # Example strings
string1 = "The quick brown fox jumps over the lazy dog1"
string2 = "Hello world!"

    # Check if strings end with a digit
print(ends_with_digit(string1))  # True
print(ends_with_digit(string2))  # False
