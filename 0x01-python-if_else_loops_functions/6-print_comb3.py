#!/usr/bin/python3
for num_a in range(0, 10):
    for num_b in range(num_a + 1, 10):
        if num_a == 8 and num_b == 9:
            print("{}{}".format(num_a, num_b))
        else:
            print("{}{}".format(num_a, num_b), end=", ")
