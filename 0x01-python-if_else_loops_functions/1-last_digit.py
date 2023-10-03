#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
num_ld = num_str[-1]
ld_num = int(num_ld)
if number < 0 and ld_num > 0:
    ld_num = -1 * ld_num
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, ld_num))
elif number == 0 or ld_num == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif number > 0 and ld_num <= 5 and ld_num > 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, ld_num))
elif number > 0 and ld_num > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, ld_num))
