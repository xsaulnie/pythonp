import random
import sys
def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded."""
    res = text.split(sep)

    valid_option = ["shuffle", "unique", "ordered", None]

    if (option not in valid_option):
        print("ERROR")
        return
    if (type(sep) is not str or type(text) is not str):
        print("ERROR")
        return


    if (option == "shuffle"):
        random.shuffle(res)
        res2 = res
    elif(option == "unique"):
        res2 = []
        for x in res:
            if x not in res2:
                res2.append(x)
    elif (option == "ordered"):
        res.sort()
        res2 = res
    else:
        res2 = res

    for i in res2:
        yield(i)


txt="This is a simple string for a basic test. Very simple."
for elem in generator(txt, sep=' '):
    print(elem)

for elem in generator(txt, sep='.'):
    print(elem)

for elem in generator(txt, sep='i'):
    print(elem)

for elem in generator(txt, sep='si'):
    print(elem)
sys.exit()
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print()
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print()
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print()
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)


