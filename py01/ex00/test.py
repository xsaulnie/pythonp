from recipe import Recipe
from book import Book
import datetime


w = Recipe(3, int(2), 15, ["egg", "flour"], "dessert")
w = Recipe("Cake", "truc", 15, ["egg", "flour"], "dessert")
w = Recipe("Cake", int(13), 15, ["egg", "flour", 15], "dessert")
w = Recipe("Cake", int(2), 15, "list", "dessert")
w = Recipe("Cake", int(2), 15, ["egg", "flour"], "soup")
w = Recipe("Cake", int(2), 15, ["egg", "flour", 15], "dessert")
n1 = Recipe("Cake", int(2), 15, ["egg", "flour"], "dessert")


print(n1)
n2 = Recipe("Salad", int(1), 5, ["tomatoes", "avocado"], "dessert", "very easy to do")
to_print = str(n1)
print(to_print)

w = Book("my_book")
print(w.creation_date)