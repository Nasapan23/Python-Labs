import re

def starts_with_digit(string):
    pattern = re.compile(r"^\d")
    return pattern.match(string) is not None


    # Example strings
string1 = "4 score and 7 years ago"
string2 = "Hello world!"

    # Check if strings start with a digit
print(starts_with_digit(string1))  # True
print(starts_with_digit(string2))  # False
