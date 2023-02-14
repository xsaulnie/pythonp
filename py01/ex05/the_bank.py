class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    @staticmethod
    def check_corrupt(account):
        correct_starta = False
        correct_startz = False
        if not isinstance(account, Account):
            return False
        attr = dir(account)
        if len(attr) % 2 == 0:
            return False
        if (not "name" in attr or not "value" in attr or not "id" in attr):
            return False
        if ((not type(account.value) is float and not type(account.value)  is int) or not type(account.name) is str or not type(account.id) is int):
            return False
        for x in attr:
            if (x[0] == 'b'):
                return False
            if (x.startswith("zip")):
                correct_startz = True
            if (x.startswith("addr")):
                correct_starta = True
        
        return correct_starta and correct_startz

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        for acc in self.accounts:
            if (acc.name == new_account.name):
                return False

        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """

        ori = None
        des = None

        if (not type(amount) is float):
            return (False)
        if (not type(origin) is str or not type(dest) is str):
            return (False)

        for x in self.accounts:
            if x.name == origin:
                ori = x
            if x.name == dest:
                des = x
         
        check = self.check_corrupt(ori)
        if (check == False):
            return (False)
        check = self.check_corrupt(des)
        if (check == False):
            return False
        if (ori.value - amount < 0):
            return (False)
        if (origin == dest):
            return (True)

        ori.transfer(-amount)
        des.transfer(amount)
        return (True)

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if (not type(name) is str):
            return (False)
        acc = None
        for x in self.accounts:
            if x.name == name:
                acc = x
                break
        if acc == None:
            return (False)

        attr = dir(acc)
        if (not "name" in attr):
            acc.__dict__.update({"name" : "Unknown"})
        if (not "value" in attr):
            acc.__dict__.update({"value" : 0.0})
        if (not "id" in attr):
            acc.__dict__.update({"id" : -1})
        if (not type(acc.name) is str):
            acc.__dict__[name] = "Unknown"
        if (not type(acc.id) is int):
            acc.__dict__[id] = -1
        if (not type(acc.value) is float and not type(acc.value) is int):
            acc.__dict__[value] = 0.0
        

        addrstart = False
        zipstart = False
        for x in attr:
            if (x[0] == 'b'):
                newkey = x.replace("b", "B")
                acc.__dict__[newkey] = acc.__dict__[x]
                del acc.__dict__[x]
            if (x.startswith("zip")):
                zipstart=True
            if (x.startswith("addr")):
                addrstart=True

        if not zipstart:
            acc.__dict__.update({"zip" : '0-0'})
        if not addrstart:
            acc.__dict__.update({"addr" : '-1'})

        if (len(acc.__dict__) % 2 == 0):
            acc.__dict__.update({"sup" : "parity check"})

        print(acc.__dict__, len(acc.__dict__))
        
        return (True)
