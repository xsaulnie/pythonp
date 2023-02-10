import datetime

class Book:

    key_of_recipes_list = ["starter, lunch, dessert"]

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
    



