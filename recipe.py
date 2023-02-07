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

def delete_recipe(name):
    if (type(name) != str):
        return
    for key, value in cookbook.items():
        if (key == name):
            del cookbook[key]
            return
def add_recipe():
    name = input("Enter a name:\n")
    cur = "enter"
    cur_lst = []
    print("Enter ingredients:\n")
    while (cur != ""):
        cur = input()
        if (cur != ""):
            cur_lst.append(cur)

    typem = input("Enter a meal type:\n")


    prept = "36a"

    while True:
            prept = input("Enter a preparation time:\n")
            if (prept.isdigit() == True):
                break
            else:
                print("Your time is not a number !")

    cookbook[name] = {}
    cookbook[name]["ingredients"] = cur_lst
    cookbook[name]["meal"] = typem
    cookbook[name]["prep_time"] = int(prept)
    return

def print_menu():
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")

    while True:
        opt = input("Please select an option:")
        if (opt.isdigit() == True and (int(opt) <= 5 and int(opt) >= 1)):
            break
        else:
            print("Option incorrect.")

    return int(opt)

assert len(sys.argv) == 1, "error argument"
main_loop = True
print("Welcome to the Python Cookbook !")
while(main_loop):
    ret = print_menu()
    if ret == 1:
        add_recipe()
    if ret == 2:
        cur_arg = input("Please enter a recipe name to delete:")
        delete_recipe(cur_arg)
    if ret == 3:
        cur_arg = input("Please enter a recipe name to get its details:")
        display_recipe(cur_arg)
    if ret == 4:
        print("Current state of the cookbook :")
        print(cookbook)
    if ret == 5:
        main_loop = False
    if ret != 5:
        input("return menu...")
sys.exit()
