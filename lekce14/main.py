# # ***Тестирование***
# def func(x):
#     return x + 1


# def test_answer():
#     assert func(4) == 5


def add_task(tasks, task):
    tasks.append(task)
    return tasks

def del_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks

def complate_task(tasks, task):
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = f"X {task}"
    return tasks


def test_add_task():
    assert add_task([], "chleb") == ["chleb"]
    assert add_task(["chleb"], "prodat chleb") == ["chleb", "prodat chleb"]

def test_remove():
    assert del_task(["chleb"], "chleb") == []
    assert del_task(["chleb", "prodat chleb"], "prodat chleb") == ["chleb"]

def test_complate():
    assert complate_task(["chleb", "prodat chleb"], "chleb") == ["X chleb", "prodat chleb"]

