#!/usr/bin/pyhton3

#c = input("enter a single ascii char: ")

def islower(c):
    for i in range(97, 123):
        if chr(i) == c:
            return True

        #else:
            #return False
#print("{} is {}".format(c, "lower" if islower(c) else "upper"))
