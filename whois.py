import sys

nb_arg = len(sys.argv)

if (nb_arg < 2):
    sys.exit()

assert nb_arg == 2, "more than one argument are provided"

number = sys.argv[1]

assert number.isdigit(), "argument is not an integer"

if (number.isdigit() == False):
    sys.exit()

true_number = int(sys.argv[1])

if (true_number == 0):
    print("I'm Zero")
    sys.exit()

if (true_number % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
