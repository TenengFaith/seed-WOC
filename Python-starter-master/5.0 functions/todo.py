# we need a list alias empty bucket
todo_list=[]
#       FIRST FUNCTION
#adding to the list
def add_task():
    item=input("enter a task: ")        # task to be added
    todo_list.append(item)      # add taks to the list
    print("task successfully added😊")
#       SECOND FUNCTION
#deleting a task
def delete_task():
    if len(todo_list)==0:
        print("there is no task in the list to be deleted😢")
    else:  # enumerate 
        print("    TASKS💀   \n")
        for index, item in enumerate(todo_list):
           print(f"{index+1}. {item}")
    item_index=int(input("enter the item number to be deleted💣: "))-1
    if item_index<0 or item_index>=len(todo_list):
        print("out of range❌")
    else:
        todo_list.remove(item_index) # or del todo_list[item_index]
        read_list()

#           THIRD FUNCTION
#updating list: changing item
def update_list():
    if len(todo_list)==0:
        print("there is no task in the list to be updated😢")
    else:  # enumerate 
        print("    TASKS💀   \n")
        for index, item in enumerate(todo_list):
           print(f"{index+1}. {item}")
    update_index=int(input("enter the item number to be updated⭕: "))-1
    if update_index<0 or update_index>=len(todo_list):
        print("out of range❌")
    else:
        new_item=input("enter the new task: ")
        read_list()


#           FOURTH FUNCTION

#view list
def read_list():
    if len(todo_list)==0:
        print("list is empty")
    else:    
        for index,item in enumerate(todo_list):
            print(f"{index+1}. {item}")





#                           WORKING PROGRAM!!!!
while True:
    print(" 🔥🔥🔥🔥MY TODO LIST APP🔥🔥🔥🔥 ")
    print("1. add task to list")
    print("2. remove task from list")
    print("3 update item in list")
    print("4. view list")
    print("5. quit")
    choice=input("enter the number of what you want to do")
    if choice=="1":
        add_task()
    elif choice=="2":
        delete_task()
    elif choice=="3":
        update_list()
    elif choice=="4":
        read_list()
    elif choice=="5":
        break
    else:
        print("stupid, try again. You do not have sense!😡")
