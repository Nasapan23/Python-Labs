import re

words = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", "rectangle", "parallelogram", "trapezoid"]
geo = "A square has four sides, a triangle has three, a pentagon has five, a hexagon has six. While a square has four equal sides, a triangle can have zero, two or three equal sides."

digits_pattern = re.compile(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b', re.IGNORECASE)
non_digits_pattern = re.compile(r'\b(?!zero|one|two|three|four|five|six|seven|eight|nine)\w+\b')

digits = digits_pattern.findall(geo)
non_digits = non_digits_pattern.findall(geo)

print("Digits:", digits)
print("Non-digits:", non_digits)
