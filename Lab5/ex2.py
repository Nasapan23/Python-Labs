import re

words = "car, cat, dog, pool, bath, cone, cube, ring, int"

pattern = re.compile(r'\b\w{4}\b')

for match in pattern.finditer(words):
    print(match.group())