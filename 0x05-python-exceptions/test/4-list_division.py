#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            div_num =  my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_num = 0
        except TypeError:
            print("wrong type")
            div_num = 0
        except IndexError:
            print("out of range")
            div_num = 0
        finally:
            new_list.append(div_num)

    return new_list
