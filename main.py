lstToDo =[]
while True:
    print("Let's help with your TO DOs")
    print("""
    Enter- Show -to show a task
    Enter- Add -to add a task
    Enter- Edit -to edit a task
    Enter- Complete TaskNo -to mark task complete
    Enter- Show Complete -to show completed a tasks
    Enter-  Delete TaskNo -to delete a task
    Enter- Exit -to exit the app\n""")
    promt = input("What do you want to do:")


    if promt.__contains__("Add"):
        task = input("Enter your task: ")
        lstToDo.append(task)

    elif promt.__contains__("Show"):
        print("These a the task that are listed:")
        for index in lstToDo:
            print(index)

    elif promt.__contains__("Exit"):
        break



