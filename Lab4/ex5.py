import math

num1 = 12
num2 = 20

# calculate the greatest common divisor
gcd = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")

# calculate the least common multiple
lcm = (num1 * num2) // gcd
print(f"The LCM of {num1} and {num2} is {lcm}")
