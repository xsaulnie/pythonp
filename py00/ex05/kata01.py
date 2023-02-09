kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

#print("Python was created by {Python}\nRuby was created by {Ruby}\nPHP was created by {PHP}".format(**kata))
#print(len(kata))
print("".join("{} was created by {}\n".format(key, value) for key, value in kata.items()), end="")
