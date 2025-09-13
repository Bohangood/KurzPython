# def Welcome(name):
#     print(f"{name} welcome to our team")

# Welcome("alex")

# def Welcome(name):
    # print(f"{name} welcome to our team")
    # return f"{name} welcome to our team"
# 
# result = Welcome("alex")
# print(result)

# result = 0 # global peremena
# 
# def multiply(a, b):
    # res = a + b + result # local peremena
    # return res
# 
# result = multiply(5, 5)
# print(result)

# def pow(a, b=2):
    # result = a ** b
    # return result
# print(pow(3))# 9
# print(pow(3, 4)) #81

# def add(a: int, b: int) -> int: # ! типизация
#     return a + b
# print(add(3, 4))   #7
# print(add("Hi", "Alex")) # HiAlex
# ? анотация - 

#! Better Comments - изменения цвета комент

def orders(costumer: str,table: int, *items: str, drink: str="water", **extra) -> None:
    print(f"клиент: {costumer}" )
    print(f"Застолом номер {table}")
    for item in items:
        print(f"список - {item}")
    print(f"drin {drink}")
    
    if extra:
        print("dopolnitelna")
        for key, value in extra.items():
            print(f" - {key}:{value}")

orders("Ivan", 4, "pizza", "cheese", drink="bear", sleve="Isic", platba="Credit karta")

