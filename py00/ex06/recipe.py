import sys

cookbook={
    "Sandwich" : 
    {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "Cake" :
    {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
    },
    "Salad" :
    {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def print_recipe_names():
    if (len(cookbook) == 0):
        print("No recipe on the cookbook")
        return 
    print("Recipes in the cookbook : ")
    for key, value in cookbook.items():
            print(key, end=" ")
    print()

def display_recipe(name):
    if (type(name) != str):
        return
    for key, value in cookbook.items():
        if (key == name):
            print(f"Recipe for {name}:")
            print("\tIngredients list: " , value["ingredients"])
            print("\tTo be eaten for %s." % (value["meal"]))
            print("\tTakes %d minutes of cooking." % (value["prep_time"]))
            return
    print(f"No recipe {name} was found")

def delete_recipe(name):
    if (type(name) != str):
        return
    for key, value in cookbook.items():
        if (key == name):
            del cookbook[key]
            print(f"{name} deleted")
            return
    print(f"No recipe {name} was found")
def add_recipe():
    name = input(">>> Enter a name:\n")
    cur = "enter"
    cur_lst = []
    print(">>> Enter ingredients:")
    while (cur != ""):
        cur = input()
        if (cur != ""):
            cur_lst.append(cur)

    typem = input(">>> Enter a meal type:\n")

    prept = "36a"

    while True:
            prept = input(">>> Enter a preparation time\n")
            if (prept.isdigit() == True):
                break
            else:
                print("Your time is not a number !")

    cookbook[name] = {}
    cookbook[name]["ingredients"] = cur_lst
    cookbook[name]["meal"] = typem
    cookbook[name]["prep_time"] = int(prept)
    print(f"{name} added")
    return

def print_menu():


    while True:
        print("List of available options:")
        print("\t1: Add a recipe")
        print("\t2: Delete a recipe")
        print("\t3: Print a recipe")
        print("\t4: Print the cookbook")
        print("\t5: Quit")
        opt = input("Please select an option:\n>>")
        if (opt.isdigit() == True and (int(opt) <= 5 and int(opt) >= 1)):
            break
        else:
            print("Sorry, this option does not exist.")

    return int(opt)

assert len(sys.argv) == 1, "error argument"
main_loop = True
print("Welcome to the Python Cookbook !")
while(main_loop):
    ret = print_menu()
    if ret == 1:
        add_recipe()
    if ret == 2:
        cur_arg = input("Please enter a recipe name to delete:\n>>")
        delete_recipe(cur_arg)
    if ret == 3:
        cur_arg = input("Please enter a recipe name to get its details:\n>>")
        display_recipe(cur_arg)
    if ret == 4:
        print_recipe_names()
        print("Current state of the cookbook :")
        print(cookbook)
    if ret == 5:
        main_loop = False
    if ret != 5:
        input("return menu...")
sys.exit()
