#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    list_len = 0
    for i in my_list:
        list_len += 1

    printed = 0

    try: 
        for i in range(x):
            print("{}".format(my_list[i]), end=' ')
            printed += 1
    except IndexError:
        for i in range(list_len):
            print("{}".format(my_list[i]), end=' ')
            printed += 1

    print ()

    return printed
