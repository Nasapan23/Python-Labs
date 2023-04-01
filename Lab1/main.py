def divisible_by_3():
    for num in range(40, 71):
        if num % 3 == 0:
            print(num)
def sum_of_numbers():
    num = int(input("Enter an integer: "))
    total = sum(range(1, num+1))
    print("The sum of all numbers from 1 to {} is {}".format(num, total))
def sum_of_numbers():
    num = int(input("Enter an integer: "))
    total = sum(range(1, num+1))
    print("The sum of all numbers from 1 to {} is {}".format(num, total))
def loop_success():
    num = 5
    count = 1
    while count <= 10:
        print("Success")
        num += 1
        count += 1
def count_letters():
    string = "Welcome to the lab!"
    count = string.count("m") + string.count("l") + string.count("c") + string.count("a") + string.count("e")
    print("The letters m, l, c, a, and e appear {} times in the string".format(count))
def even_or_odd():
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
def operations_on_number():
    num = int(input("Enter an integer: "))
    if num > 100:
        result = num / 2 + 20
        print("The result is {}".format(result))
    elif num < 100:
        result = num * 3 - 200
        print("The result is {}".format(result))
    else:
        print("The number is 100")
def factorial():
    num = int(input("Enter a non-negative integer: "))
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("The factorial of {} is {}".format(num, fact))

def main():
    divisible_by_3()
    reverse_names()
    sum_of_numbers()
    loop_success()
    count_letters()
    even_or_odd()
    operations_on_number()
    factorial()
