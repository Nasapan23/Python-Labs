import random

def random_ints():
    ints = []
    for i in range(5):
        ints.append(random.randint(40, 70))
    print(ints)

# example usage
random_ints()
