import os
while True:
    print("Let's help with your TO DOs\n")
    print("Enter- Menu -to show menu")

    prompt = input("What do you want to do: ")
    if prompt.__contains__("Menu"):
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

    elif prompt.__contains__("Add"):
        finish = 1
        while True:
            task = input("Enter your task or Done to finish: ")
            if task == "Done":
                break
            with open("To_Do.txt", 'a') as file:
                file.write(f"{task}\n")

    elif prompt.__contains__("Show"):
        print("These a the tasks that are listed: ")
        with open("To_Do.txt", 'r') as file:
            lstToDo = list(file.readlines())
        for index, task in enumerate(lstToDo):
            print(f"{index+1}- {task.rstrip("\n")}")

    elif prompt.__contains__("Edit"):
        with open("To_Do.txt", 'r') as file:
            lstToDo = list(file.readlines())
        while True:
            taskEditNo = int(input(
                "Enter the task number to edit & 0 to exit: "))
            if taskEditNo == 0:
                break
            else:
                edited = input("Enter the new edited task: ")
                lstToDo[taskEditNo-1] = edited+"\n"
                with open("To_Do.txt", 'w+' ) as file:
                    file.writelines(lstToDo)

    elif prompt.__contains__("Mark-Complete"):
        with open("To_Do.txt", 'r') as file:
            lstToDo = list(file.readlines())
        completedTaskNo   = int(input(
                "Enter the completed task number: "))
        completeTask = lstToDo.pop(completedTaskNo - 1)
        if completedTaskNo >= 1:
            with open("To_Do.txt", 'w+' ) as file:
                 file.writelines(lstToDo)

            with open("Completed_To_Do.txt", 'a' ) as file:
                file.write(f"{completeTask}")
                print(f"This {completeTask.strip("\n")} "
                      f"task has been completed.")
        else:
            print("That not a valid task number please try again.")

    elif prompt.__contains__("Completed-Tasks"):
        print("These are the completed tasks:")
        with open("Completed_To_Do.txt", 'r') as file:
            lstCompleted = list(file.readlines())
        for index, task in enumerate(lstCompleted):
            print(f"{index+1}- {task.strip("\n")}.")
        action = input("Enter- Clear - to clean tasks, "
                       "- Restore - to restore task or- "
                       "Exit -to exit: ")
        if action.__contains__("Clear"):
            with open("Completed_To_Do.txt", 'w') as file:
               print("Successfully cleared")
        elif action.__contains__("Restore"):
            restore = input("Enter the numbers of tasks to "
                            "restore with nothing between them: ")
            for index in restore:
                restore_task = lstCompleted.pop(int(index)-1)
                with open("To_Do.txt", 'a') as file:
                    file.write(f"{restore_task}")
                print(f"{index}- {restore_task}")
            print("Restoration successfully!")
        elif action.__contains__("Exit"):
            continue

    elif prompt.__contains__("Delete"):
        while True:
            with open("To_Do.txt", 'r') as file:
                lstToDo = list(file.readlines())
            taskDelete = int(input("Enter the task number to delete: "))
            if taskDelete == 0:
                break
            else:
                deleteTask = lstToDo.pop(taskDelete-1)
                for task in lstToDo:
                    with open("To_Do.txt", 'w+' ) as file:
                        file.write(f"{task}")
                print(f"You deleted {deleteTask} task successfully.")

    elif prompt.__contains__("Exit"):
        break




