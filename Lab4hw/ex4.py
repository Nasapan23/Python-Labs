import os
import random

# Select random element from a list
my_list = [1, 2, 3, 4, 5]
rand_list_elem = random.choice(my_list)
print(f"Random element from list: {rand_list_elem}")

# Select random element from a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
rand_dict_elem = random.choice(list(my_dict.keys()))
print(f"Random element from dictionary: {rand_dict_elem}")

# Select random file from directory
files = os.listdir(".")
rand_file = random.choice(files)
print(f"Random file from directory: {rand_file}")
