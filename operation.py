import sys

nb_arg = len(sys.argv)

if (nb_arg < 2):
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
assert nb_arg == 3, "more than two argument are provided"

number1 = sys.argv[1]
number2 = sys.argv[2]

assert number1.isdigit(), "argument 1 is not an integer"
assert number2.isdigit(), "argument 2 is not an integer"

number1 = int(number1)
number2 = int(number2)

if (number2 == 0):
    quot = "ERROR (division by zero)"
    rem =  "ERROR (modulo by zero)"
else:
    quot = number1 / number2
    rem = number1 % number2

print(f"Sum : {number1 + number2}\nDifference: {number1 - number2}\nProduct: {number1 * number2}\nQuotien: {quot}\nRemainder: {rem}\n")
