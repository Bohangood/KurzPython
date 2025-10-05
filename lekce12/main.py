# множ. наследование 

# class Car:
    # def ride(self):
        # print("car ride on road")
        # 
# class Boat:
    # def swim(self):
        # print("boat swim on water")
# 
# class Other(Car, Boat):
    # pass
# 
# a = Other()
# a.ride()
# a.swim()

# from abc import ABC, abstractmethod
# class Transport(ABC):
    # @abstractmethod
    # def move(self):
        # pass
    # 
# class Car(Transport):
    # def move(self):
        # print("car ride on road")
    # 
    # def __hidden(self):
        # print("Hidden type")
    # 
    # def ride(self):
        # print("Voditel love ride on car")    
        # 
# class Boat(Transport):
    # def move(self):
        # print("boat swim on water")
        # 
    # def __hidden(self):
        # print("Hidden type")
        # 
    # def swim(self):
        # print("Any love ride on boat") 
# 
# class Other(Car, Boat):
    # pass        
# a = Other()
# a.move()
# a.ride()
# a.swim()

# class Car:
#     def ride(self):
#         print("car ride on road")
        
#     def music(self, song):
#         print(f"Now play {song}")

# c = Car()
# c.music("Queen")

# class MusicMixin:
#        def music(self, song):
#         print(f"Now play {song}")

# class Smartphone(MusicMixin):
#     pass

# class Radio(MusicMixin):
#     pass

# class Car(Smartphone, Radio, MusicMixin):
#     pass

# c = Car()
# c.music("Queen")

# import json
# from datetime import datetime

# class SerialMixin:
#     def to_dict(self):
#         result = {}
#         for key, value in self.__dict__.items():
#             if isinstance(value, SerialMixin):
#                 result[key] = value.to_dict()
#             else:
#                 result[key] = value
#         return result
    
#     def to_json(self):
#         return json.dumps(self.to_dict(), default=str)


# class TimeMixin:
#     def __init__(self, *args, **kwargs):
#         self.created = datetime.now()
#         super().__init__(*args, **kwargs)
        

# class LogMixin:
#     def log(self, message):
#         print(f"[LOG] {datetime.now()}, {message}")
        

# class User(SerialMixin, TimeMixin, LogMixin):
#     def __init__(self, username, email):
#         super().__init__()
#         self.username = username
#         self.email = email
        

# class Product(SerialMixin, LogMixin):
#     def __init__(self, name, price):
#         super().__init__()
#         self.name = name
#         self.price = price
        

# class Order(SerialMixin, TimeMixin):
#     def __init__(self, user, product):
#         super().__init__()
#         self.user = user
#         self.product = product



# u1 = User("Alice", "email@email.com")
# u1.log("User registered")

# p1 = Product("laptop", 1444)
# p1.log("Product added")

# print(p1.to_json())

# o1 = Order(u1, p1)
# print(o1.to_json())





# class Pre:
#     Read = 1 << 0
#     Write = 1 << 1
#     Delete = 1 << 2
#     Admin = 1 << 3
    
#     NANES = {
#         Read: "Read",
#         Write: "Write",
#         Delete: "Delete",
#         Admin: "Admin"
#     }
    
#     def __init__(self):
#         self.flags = 0
        
#     def add(self, pre):
#         self.flags |= pre
        
#     def remove(self, pre):
#         self.flags &= ~pre
        
#     def has(self, pre):
#         return self.flags & pre
    
#     def __str__(self):
#         active = [name for pre, name in self.NANES.items() if self.has(pre)]
#         return ", ".join(active) if active else "ne"
    
# class LogMixin:
#     def log(self, message):
#         print(f"[LOG] {message}")

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.pre = Pre

# class AdminUser(User, LogMixin):
#     def __init__(self, name):
#         super().__init__(name)
        
#         self.pre.add(Pre.Read | Pre.Write | Pre.Delete | Pre.Admin)
        
#     def add(self, pre):
#         self.log(f"delete op: {Pre.NANES[pre]}")
        
#     def remove(self, pre)
        