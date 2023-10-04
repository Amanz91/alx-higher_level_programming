#!/usr/bin/python3
def print_last_digit(number):
    ld_num = abs(number) % 10
    print("{}".format(ld_num), end="")
