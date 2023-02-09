import sys
import string

def text_analyzer(str_arg=None):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if str_arg is None:
        str_arg=input("What is the text to analyze?\n")
    assert isinstance(str_arg, str), "argument is not a string"
    upperCase = 0
    ponc = 0
    lowerCase = 0

    for x in str_arg:
        if (x.isupper()):
            upperCase = upperCase + 1
        elif (x.islower()):
            lowerCase = lowerCase + 1
        if x in string.punctuation:
            ponc = ponc + 1

    spacenb = str_arg.count(' ')
    nbCarac = len(str_arg)
    print (f"The text contains {nbCarac} character(s):\n- {upperCase} upper letters(s)\n- {lowerCase} lower letters(s)\n- {ponc} punctuation mark(s)\n- {spacenb} space(s)")

if __name__ == "__main__":
    len_arg = len(sys.argv)
    assert len_arg == 2 or len_arg == 1, "more than one argument are provided"

    if (len_arg == 1):
        texto_analyze = input()
        text_analyzer(texto_analyze)
        sys.exit()

    text_analyzer(sys.argv[1])

