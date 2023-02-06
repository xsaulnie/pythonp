import sys

nb_arg = len(sys.argv)
if nb_arg <= 1:
    print("Error no argument")
    sys.exit()

all_string=""

for x in sys.argv[1:]:
    all_string = all_string + " "
    all_string = all_string + x.swapcase()

res="".join(reversed(all_string[1:]))

print(res)
