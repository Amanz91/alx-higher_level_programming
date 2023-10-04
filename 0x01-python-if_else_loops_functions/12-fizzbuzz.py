#!/usr/bin/python3
for num in range(1, 101):
    if num == 100:
        print("{}".format("Buzz"))
    elif num % 3 == 0 and num % 5 == 0:
        print("{}".format("FizzBuzz"), end=" ")
    elif num % 3 == 0:
        print("{}".format("Fizz"), end=" ")
    elif num % 5 == 0:
        print("{}".format("Buzz"), end=" ")
    else:
        print("{}".format(num), end=" ")
