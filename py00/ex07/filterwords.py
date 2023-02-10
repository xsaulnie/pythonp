import sys
import string

def exit_error():
    print("ERROR")
    sys.exit()

if (len(sys.argv) != 3):
    exit_error()

test = "test"
try:
    test = int(sys.argv[1])
except ValueError:
    pass

if (test != "test"):
    exit_error()

try:
    test2 =int(sys.argv[2])
except ValueError:
    exit_error()

if (test2 < 0):
    print("Error second parameter must be positiv")
    sys.exit()

num = int(sys.argv[2])

line = sys.argv[1].translate({10 : ord(' ')})
line = line.translate({ord(i) : ord(' ') for i in string.punctuation})
res = line.split(' ')
res = [val for val in res if len(val) > num]

print(res)


