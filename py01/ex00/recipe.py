class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description="No description"):
        type_of_recipe = ["starter", "lunch", "dessert"]
        if type(name) is not str:
            print("Recipe constructor error : name is not a string")
            return
        elif (type(cooking_lvl) is not int):
            print("Recipe constructor error : cooking_lvl is not an int")
            return
        elif (cooking_lvl > 5 or cooking_lvl < 1):
            print("Recipe constructor error : cooking level must be beetween 1 and 5")
            return
        elif (type(cooking_time) is not int):
            print("Recipe constructor error : cooking_time is not an int")
            return
        elif (cooking_time < 0):
            print("Recipe constructor error : cooking time must be positiv")
            return
        elif (type(ingredients) is not list):
            print("Recipe constructor error : ingredients must be a list")
            return
        elif (self.list_of_str(ingredients) is False):
            print("Recipe constructor error : ingredients must be a list of string")
            return   
        elif type(recipe_type) is not str:
            print("Recipe constructor error : recipe_type is not a string")
            return
        elif (not recipe_type in type_of_recipe):
            print("Recipe constructor error : recipe_type must be 'starter' or 'lunch' or 'dessert' ")
            return
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        ing = ""
        for x in self.ingredients:
            ing = ing + x + ", "

        return f"Recipe description of {self.name} :\n\tDifficulty (from 1 to 5) : {self.cooking_lvl}\n\tCooking time {self.cooking_time} minutes\n\tIngredients : {ing[:-2]}\n\tType of recipe : {self.recipe_type}\n\tOther informations : {self.description}"

    def list_of_str(self, lst):
        for x in lst:
            if (type(x) is not str):
                return False
        return True
