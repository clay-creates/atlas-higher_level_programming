#!/usr/bin/python3
import sys

counter = 1

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("{} arguments.".format(len(sys.argv)), end="")
    elif len(sys.argv) == 1:
        print("{} argument: ".format(len(sys.argv)))
    else:
        print("{} arguments: ".format(len(sys.argv)))

    for arg in sys.argv:
        print("{}: {}".format(counter, arg))
        counter += 1
