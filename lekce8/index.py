import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    #Завантажити задачі з файлу, або повернути пустий словник.
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_tasks(tasks):
    #Зберегти задачі у файл.
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def generate_id(tasks):
    #Зробити новий id. Він завжди на 1 більший за найбільший існуючий
    if tasks:
        return str(int(max(tasks.keys(), key=int)) + 1)
    return "1"

def print_task(task_id, task):
    #Вивести одну задачу.
    print(f"ID: {task_id} | Назва: {task['title']} | Опис: {task['desc']} | "
          f"Пріоритет: {task['priority']} | Статус: {task['status']}")


def create_task(tasks):
    title = input("Введіть назву: ")
    desc = input("Введіть опис: ")
    priority = input("Пріоритет (низ/сер/вис): ")
    status = input("Статус (новий/в проц/зав.): ")
    task_id = generate_id(tasks)
    tasks[task_id] = {"title": title, "desc": desc, "priority": priority, "status": status}
    save_tasks(tasks)
    print("Задачу створено!")

def view_tasks(tasks):
    if not tasks:
        print("Список задач пустий.")
        return

    print("1 – показати як є")
    print("2 – відсортувати по статусу")
    print("3 – відсортувати по пріоритету")
    print("4 – пошук")
    choice = input("Ваш вибір: ")

    items = list(tasks.items())
    if choice == "2":
        items.sort(key=lambda x: x[1]["status"])
    elif choice == "3":
        items.sort(key=lambda x: x[1]["priority"])
    elif choice == "4":
        word = input("Введіть слово для пошуку: ").lower()
        items = [(x, b) for x, b in tasks.items()
                 if word in b["title"].lower() or word in b["desc"].lower()]

    for x, b in items:
        print_task(x, b)

def update_task(tasks):
    task_id = input("Введіть id задачі: ")
    if task_id not in tasks:
        print("Такої задачі немає.")
        return

    print("1 – змінити назву")
    print("2 – змінити опис")
    print("3 – змінити пріоритет")
    print("4 – змінити статус")
    choice = input("Ваш вибір: ")

    if choice == "1":
        tasks[task_id]["title"] = input("Нова назва: ")
    elif choice == "2":
        tasks[task_id]["desc"] = input("Новий опис: ")
    elif choice == "3":
        tasks[task_id]["priority"] = input("Новий пріоритет: ")
    elif choice == "4":
        tasks[task_id]["status"] = input("Новий статус: ")

    save_tasks(tasks)
    print("Задачу оновлено!")

def delete_task(tasks):
    task_id = input("Введіть id задачі: ")
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print("Задачу видалено!")
    else:
        print("Такої задачі немає.")


def main():
    tasks = load_tasks()

    while True:
        print("\nГоловне меню:")
        print("1 – Створити задачу")
        print("2 – Подивитись задачі")
        print("3 – Оновити задачу")
        print("4 – Видалити задачу")
        print("0 – Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()