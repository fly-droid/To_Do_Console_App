import os


lstToDo = []
lstCompleted = []
while True:
    print("Let's help with your TO DOs\n")
    print("Enter- Menu -to show menu")

    promt = input("What do you want to do:")
    if promt.__contains__("Menu"):
        print("""
            Enter= 'Menu' -to show menu.
            Enter- 'Show' -to show a task.
            Enter- 'Add' -to add a task.
            Enter- 'Edit' -to edit a task.
            Enter- 'Mark-Complete' -to mark task complete.
            Enter- 'Completed-Tasks' -to show completed a tasks.
            Enter- 'Delete' -to delete a task.
            Enter- 'Exit' -to exit the app.
            """)

    elif promt.__contains__("Add"):
        task = input("Enter your task: ")
        lstToDo.append(task)

    elif promt.__contains__("Show"):
        print("These a the tasks that are listed:")
        for index, task in enumerate(lstToDo):
            print(f"{index+1}- {task}.")

    elif promt.__contains__("Edit"):
        taskEditNo = int(input("Enter the task number to edit: "))
        edited = input("Enter the new edited task: ")
        lstToDo[taskEditNo-1] = edited

    elif promt.__contains__("Mark-Complete"):
        completdTaskNo = int(input("Enter the completed task number: "))
        completeTask = lstToDo.pop(completdTaskNo-1)
        lstCompleted.append(completeTask)
        print(f"This {completeTask} has been completed.")

    elif promt.__contains__("Completed-Tasks"):
        print("These are the completed tasks:")
        for index, task in enumerate(lstCompleted):
            print(f"{index}- {task}.")

    elif promt.__contains__("Delete"):
        taskDelete = int(input("Enter the task number to delete: "))
        deleteTask = lstToDo.pop(taskDelete-1)
        print(f"You deleted {deleteTask} task successfully.")

    elif promt.__contains__("Exit"):
        break




