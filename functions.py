def addItem(task, path="To_Do.txt"):
    if isinstance(task, list):
        with open(path, 'w+') as file:
            file.writelines(task)
    else:
        with open(path, 'a') as file:
            file.write(task)
def getItem(path="To_Do.txt"):
    with open(path, 'r') as file:
        lstToDo = list(file.readlines())
    return lstToDo
def get_items():
    while True:
        task = input("Enter your task or Done to finish: ")
        if task == "Done":
            break
        addItem(f"{task}\n")
def show_items():
    print("These a the tasks that are listed: ")
    lstToDo = getItem()
    for index, task in enumerate(lstToDo):
        print(f"{index + 1}- {task.rstrip("\n")}")
def edit_items():
    lstToDo = getItem()
    while True:
        taskEditNo = int(input(
            "Enter the task number to edit & 0 to exit: "))
        if taskEditNo == 0:
            break
        else:
            edited = input("Enter the new edited task: ")
            lstToDo[taskEditNo - 1] = edited + "\n"
            addItem(lstToDo)
def mark_item():
    lstToDo = getItem()
    completedTaskNo = int(input(
        "Enter the completed task number: "))
    completeTask = lstToDo.pop(completedTaskNo - 1)
    if completedTaskNo >= 1:
        addItem(lstToDo)
        addItem(completeTask, "Completed_To_Do.txt")
        print(f"This {completeTask.strip("\n")} "
              f"task has been completed.")
    else:
        print("That not a valid task number please try again.")
def complete_tasks():
    print("These are the completed tasks:")
    lstCompleted = getItem("Completed_To_Do.txt")
    for index, task in enumerate(lstCompleted):
        print(f"{index + 1}- {task.strip("\n")}.")
    return lstCompleted
def delete_task():
    while True:
        lstToDo = getItem()
        taskDelete = int(input("Enter the task number to delete(0 to exit): "))
        if taskDelete == 0:
            break
        else:
            deleteTask = lstToDo.pop(taskDelete - 1)
            addItem(lstToDo)
            print(f"You deleted {deleteTask} task successfully.")