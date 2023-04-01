import re

a = "rectangle"
b = "square"
c = "sphere"
d = "triangle"
e = "cone"
f = "cube"
g = "cylinder"
pattern = re.compile(r'^(c|s).+e$')


for string in [a, b, c, d, e, f, g]:
    if pattern.match(string):
        print(string)