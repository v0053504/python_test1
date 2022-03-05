import sys

while True:
    try:
        x = int(input("x= "))
        y = int(input("y= "))
        break
    except ValueError:
        print("Error: invalid input")

try:
    result = x / y
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    sys.exit(1)

print(result)
