kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}


print("".join("{} was created by {}\n".format(key, value) for key, value in kata.items()), end="")
