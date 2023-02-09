import sys

kata = (19, 21, 42)

str_t=""
len_k = len(kata)
for it in kata:
    str_t = str_t + str(it) + ", "

if (len_k == 0):
    print("No number on tuple")
    sys.exit()

if (len_k == 1):
    print(f"The number is: %s" % (str_t[:-2]))
else:
    print(f"The %d numbers are: %s" % (len_k,str_t[:-2]))