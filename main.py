import os
import functions as fn

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
        fn.get_items()
    elif prompt.__contains__("Show"):
        fn.show_items()
    elif prompt.__contains__("Edit"):
        fn.edit_items()
    elif prompt.__contains__("Mark-Complete"):
        fn.mark_item()
    elif prompt.__contains__("Completed-Tasks"):
        lstCompleted = fn.complete_tasks()
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
                fn.addItem(restore_task)
                print(f"{index}- {restore_task}")
            print("Restoration successfully!")
        elif action.__contains__("Exit"):
            continue

    elif prompt.__contains__("Delete"):
        fn.delete_task()

    elif prompt.__contains__("Exit"):
        break




