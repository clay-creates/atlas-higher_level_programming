#!/usr/bin/python3
import sys

counter = 1

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("{} arguments.".format(len(sys.argv)), end="")
    else:
        print("{} arguments: ".format(len(sys.argv)))

    for arg in sys.argv:
        print("{}: {}".format(counter, sys.argv))
        counter += 1
