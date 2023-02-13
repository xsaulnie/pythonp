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

    def add(self, new_account):

        print(len(dir(new_account)))
        print(len(new_account.__dict__))
        print(vars(new_account))
        if (len(dir(new_account)) %2 == 1):
            return False

        if not isinstance(new_account, Account):
            return False
    
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        self.accounts.append(new_account)
        return True



b = Bank()
b.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))

