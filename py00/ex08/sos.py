import sys

morse_table = {
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  " ": "/"
}


carac="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

word=""
for argu in sys.argv[1:]:
    word = word + " " + argu

word = word[1:].upper()

res = ""
for x in word:
    if (not x in carac):
        print("ERROR")
        sys.exit()
    res = res + " "
    res = res + morse_table[x]


print(res[1:])