import os

# Create directory
os.mkdir("my_directory")

# Create file
with open("my_directory/a.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

# Read the first two lines
with open("my_directory/a.txt", "r") as f:
    lines = f.readlines()
    first_two_lines = lines[:2]
    print(first_two_lines)

# Overwrite the file
with open("my_directory/a.txt", "w") as f:
    f.write("New line 1\nNew line 2")
