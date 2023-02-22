class GotCharacter:
    """A class for all Game of Thrones characters."""
    def __init__(self, first_name, is_alive = True):
        if (type(first_name) is not str):
            print("Your first name must be a string")
            return
        elif (type(is_alive) is not bool):
            print("is_alive must be boolean")
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name="Stark"
        self.house_words="Winter is Coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    """A class representing the Lannister family. Or how gold make people powerful."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name="Lannister"
        self.house_words="Hear me Roar"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False
    
if __name__ == "__main__":
    arya=Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    print(arya.__doc__)

    tywin=Lannister("Tywin")
    print(tywin.__dict__)
    tywin.print_house_words()
    print(tywin.is_alive)
    tywin.die()
    print(tywin.is_alive)
    print(tywin.__doc__)