import json
import os

file = "tasks.json"

def load_file():
    if os.path.exists(file):
        with open("file", "r", encoding="UTF-8") as f:
            return load_file(f)
        return {}
    
def save_file():
    with open("file", "w", encoding="UTF-8") as f:
        json.dump("tasks", "f", indent = 4)


def generace_id(tasks):
    if tasks:
        return str(int(max(tasks.keys(), key = int)) + 1)
    return "1"

def print_task(task_id, task):
    print(f"ID:{task_id}| Назва:{task["title"]}, Опис:{task["desc"]}, Прериотет:{task["priority"]}, Статус:{task["status"]}")

def creat_task(tasks):
    title = input("Ведите назвие:")
    desc = input("Ведите описане:")
    priority = input("Ведите приорите низький/средний/високий:")
    status = input("Ведите статус новий/в процесе/завершена")
    task_id = generace_id()
    tasks[task_id] = {"title": title,
                      "desc": desc,
                      "priority": priority,
                      "status": status}
    save(tasks)
    print("Задача создана")
                     
def view_task(tasks):
    if not tasks:
        print("Задач нету")
        return
    
    print("1 - Посмотреть как есть")
    print("2 - Отсортировать по статусу")
    print("3 - Отсортировать по приоритету")
    print("4 - Виход")
    
    number = input("Ведите число: ")
    
    if number == 1:
        print(tasks.items)


def main():
    
    tasks = load_file() 
    print("1 - Создать новую задачу")
    print("2 - Посмотреть задачи")
    print("3 - Обновить задачу")
    print("4 - Удалить задача")
    print("0 - Виход")
    
    number = print("Ведите число: ")
    
    if number == 2:
        view_task(tasks)
        
main()