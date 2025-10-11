# def sumNu(a, b):
#     return a+b

# a = sumNu
# print(a(4, 9))

# def sum(*arg):
#     return sumNu(*arg)

# print(sum(2,4))
# def simp(func):
#     def wrapper():
#         print("что то до визова функций")
#         func()
#         print("что то после функций")
#     return wrapper

# @simp
# def great():
#     print("hello")

# great()

# def make(user):
#     if not user["isLogin"]:
#         print("ne zaregrestrirovany")
#         return
#     print("zakaz oformen")
# def make_pay(user):
#     if not user["isLogin"]:
#         print("ne zaregrestrirovany")
#         return
#     print("zakaz oplachen")

# user1 = {
#     "name": "alex",
#     "isLogin": True
# }
# make(user1)

# def isClient(func):
#     def wrapper(name):
#         if name == "Jan":
#             print(f"polzevatek {name} jest")
#             return func(name)
#         print("taky polzivatek netu")
#     return wrapper

# @isClient
# def make_ord(name):
#     print(f"pol {name} zdelal zakaz")

# @isClient
# def make_pay(name):
#     print(f"pol {name} oplatil zakaz")

# make_ord("Jan")
def check_balance(min_balance):
    def decaration(func):
        def wrapper(self, amount):
            if self.balance - amount < min_balance:
                print(f"Баланс не может бить менше {min_balance}")
                return
            return func(self, amount)
        return wrapper
    return decaration

class BackAccount:
    creat_owners = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        BackAccount.creat_owners += 1

    @check_balance(50)
    def withdraw(self, amount):
        self._balance -= amount
        print(f"Сума в {amount} крон снята, ващ балас{self._balance}")

    @classmethod
    def total_accounts(cls):
        return cls.creat_owners
    
    @staticmethod
    def isValid(amount):
        return amount > 0
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("баланс не может бить отрицательным")
        self._balance = value

    @property
    def inf(self):
        return f"владелец: {self.owner} баланс {self._balance} крон"
    
a1 = BackAccount("alex", 100)
a2 = BackAccount("flex", 100134)
a3 = BackAccount("Flesh", 2134)

print(BackAccount.total_accounts())
# print(BackAccount.isValid(54))
