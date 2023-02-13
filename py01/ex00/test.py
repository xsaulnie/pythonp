from recipe import Recipe
from book import Book
import datetime
import time


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

recb = Book("my_book")
print(f"{recb.name} was created {recb.creation_date}")

recb.add_recipe("string")

time.sleep(1)
recb.add_recipe(n1)
print(f"recipe cake added at : {recb.last_update}")
recb.get_recipe_by_name("Cake")

n2 = Recipe("Ice Cream", int(3), 20, ["Cream", "Chocolate", "Ice"], "dessert", "succulous")
time.sleep(1)
recb.add_recipe(n2)
print(f"recipe ice cream added at : {recb.last_update}")
recb.get_recipe_by_name("Ice")
listb = recb.get_recipes_by_type("dessert")
print("all recipes of type dessert :")
print(", ".join("{}".format(k.name) for k in listb))
print(listb[1])