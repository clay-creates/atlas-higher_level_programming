#!/usr/bin/python3
import sys

counter = 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} arguments.".format(len(sys.argv)-1))
    elif len(sys.argv) == 2:
        print("{} argument: ".format(len(sys.argv)-1))
    else:
        print("{} arguments: ".format(len(sys.argv)-1))

    for arg in sys.argv[1:]:
        print("{}: {}".format(counter, arg))
        counter += 1
