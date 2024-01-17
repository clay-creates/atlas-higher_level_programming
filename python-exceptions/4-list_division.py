#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):
        try:
            item_1 = my_list_1[i]
            item_2 = my_list_2[i]
            if not isinstance(item_1, (float, int)) or not isinstance(item_2, (float, int)):
                raise TypeError("wrong type")
            try:
                result = item_1 / item_2
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        finally:
            return new_list
