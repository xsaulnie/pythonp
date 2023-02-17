import time
from random import randint
import os
#... your definition of log decorator...



class CoffeeMachine():
    water_level = 100

    @staticmethod
    def log_time_format(value):
        if int(value) >= 1000000000:
            return ("[ exec-time = %.3f s ]" % (int(value) / 1000000000))
        else:
            return ("[ exec-time = %.3f ms ]" % (int(value) / 1000000))

    def log(function):
        prog_name = {"start_machine" : "Start Machine", "make_coffee" : "Make Cofee", "boil_water" : "Boil Water", "add_water" : "Add Water"}
        def wrapper(*args, **kwargs):
            file = open("machine.log", "a")
            deb = time.clock_gettime_ns(time.CLOCK_REALTIME)
            ret = function(*args, **kwargs)
            elapsed = time.clock_gettime_ns(time.CLOCK_REALTIME) - deb
            file.write("(%s)Running: " % os.getenv("USER") + "%-15s" % prog_name[function.__name__] + CoffeeMachine.log_time_format(elapsed) + "\n")
            return ret
        return wrapper
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)