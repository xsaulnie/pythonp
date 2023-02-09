import sys
import string

def exit_error():
    print("ERROR")
    sys.exit()

if (len(sys.argv) != 3):
    exit_error()

if (sys.argv[1].isdigit()):
    exit_error()
if (not sys.argv[2].isdigit()):
    exit_error()

num = int(sys.argv[2])
if (num == 0):
    print("[]")
    sys.exit()


line = sys.argv[1].translate({10 : ord(' ')})
line = line.translate({ord(i) : ord(' ') for i in string.punctuation})
res = line.split(' ')
res[:] = (val for val in res if len(val) > num)

print(res)


