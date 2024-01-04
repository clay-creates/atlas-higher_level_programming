#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1

a = 10
b = 5

def add(a, b):
    return (a + b)

print("{}".format(add(a, b)))
print("{}".format(sub(a, b)))
print("{}".format(mul(a, b)))
print("{}".format(div(a, b)))
