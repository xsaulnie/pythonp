import datetime
from recipe import Recipe
class Book:

    key_of_recipes_list = ["starter", "lunch", "dessert"]

    def __init__(self, name):
        if (type(name) is not str):
            print("Book constructor error : name is not a string")
            return
        creation = datetime.datetime.now()
        self.name = name
        self.creation_date = creation
        self.last_update = creation
        self.recipes_list = {
            "starter" : [],
            "lunch" : [],
            "dessert" : [],
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        for key, value in self.recipes_list.items():
            for rec_in_recipes_list in value:
                if (name == rec_in_recipes_list.name):
                    print(rec_in_recipes_list)
                    return rec_in_recipes_list
        print(f"No recipe {name} on the book {self.name}")
        
    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type not in Book.key_of_recipes_list):
            print(f"{recipe_type} is not a valid recipe_type")
            return
        return(self.recipes_list[recipe_type])

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("add_recipe : Invalid recipe type")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()

        

