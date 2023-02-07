import sys

morse_table = {
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  " ": "/"
}



word=""
for argu in sys.argv[1:]:
    word = word + argu

res = ""
for x in word:
    res = res + " "
    res = res + morse_table[x]

print(res[1:])