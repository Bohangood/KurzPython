# class Dog:
    # def bark(self):
        # print("gav, hav")
# 
# myDog = Dog()
# myDog.bark()

# class Dog:
    # def __init__(self, family: str, name:str, age:int) -> None:
        # self.type_of_dog = family
        # self.name_of_dog = name
        # self.age_of_dog = age
    # def bark(self):
        # print(f"")
        # print(f"Собака породи: {self.type_of_dog}, по кличке: {self.name_of_dog}, возраст: {self.age_of_dog}, говорит - gav, hav")
# 
# dog1 = Dog("Доберман", "Пио", 2)
# dog2 = Dog("Чихуа", "Вали", 4)
# dog3 = Dog("Пудель", "Марио", 3)
# dog4 = Dog("Пидбуль", "Дио", 7)
# 
# dog1.bark()

# class Book:
#     gener: str = "Fantastic"
    
#     def __init__(self, title:str , author:str , pages: int, gener=gener) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.gener = gener 
        
#     def info(self)-> str:
#         return f"name book: {self.title}, author: {self.author}, pages: {self.pages}, gener: {self.gener}"

    
#     def isLong(self) -> bool:
#         return self.pages > 300

# book1 = Book("451 градус по Фарингейту", "bredberry", 411 , gener="Antiutopie")
# book2 = Book("Karloson", "karlon", 134,)
# book3 = Book("Bojkov", "ksavje", 41, )

# books = [book1, book2, book3]

# for book in books:
#      print(book.info())
#      print(book.isLong())

# class Student:
#     school: str = "IT Step"
    
#     def __init__(self, name: str, age: int, raiting:float, school:str = school)-> None:
#         self.name = name
#         self.age = age
#         self.raiting = raiting
#         self.school = school
    
#     def average_score(self) -> float:
#         return sum(self.raiting) / len(self.raiting)
    
#     def add_score(self, score) -> None:
#         return self.raiting.append(score)
        
# student1 = Student("Denys",15 , [1, 2, 2 ,3, 1, 1], school="fs")

# print(student1.average_score())
# print(student1.add_score(3))
# print(student1.average_score())
# print(student1.school)

