#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    try:
        r = my_list1 / my_list2
    except (ZeroDivisionError):
        print("division by 0")
        r = 0
    except (TypeError):
        print("wrong type")
        r = 0
    except (IndexError):
        print("out of range")
        r = 0
    finally:
        new_l.append(r)
    return new_l
