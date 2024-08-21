def display_menu(tasks):
        print("TO-DO LIST MENU")
        print("1.view to-do list")
        print("2.add a task")
        print("3.remove a task")
        print("4.exit")
def view_to_do(tasks):
    if len(tasks)==0:
        print("SORRY! YOUR TO-DO LIST IS EMPTY")
    else:
        print("YOUR TO-DO LIST")
        i=1
        for task in tasks:
            print(f"{i}.{task}") 
            i+=1
def add_task(tasks):
    task=input("ENTER THE TASK YOU WANT ADD:")
    tasks.append(task)
    print(f"{task} is inserted successfully")
def remove_task(tasks):
    view_to_do(tasks)
    if len(tasks)==0:
        print("TO-DO LIST IS EMPTY")
    else:
        task_num=int(input("ENTER THE NUMBER OF THE TASK YOU WANT TO REMOVE:"))
        if 1<=task_num<=len(tasks):
            removed_task=tasks.pop(task_num-1)
            print(f"{removed_task} is removed successfully")
tasks=[]
while True:
    display_menu(tasks) 
    choice=input("ENTER YOUR CHOICE:")
    if choice=='1':
        view_to_do(tasks)
    elif choice=='2':
        add_task(tasks)
    elif choice=='3':
        remove_task(tasks)
    elif choice=='4':
        print("GOODBYE!H@VE @ NICE D@Y")
        break
    else:
        print("invalid option please try again")
           