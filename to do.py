tasks=[]
def addtask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"task '{task}'added to the list.")

def listtask():
    if not tasks:
        print("There are no tasks currently. ")
    else:
        print("current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
def deletetask():
    listtask()
    try:
        tasktodelete = int(input("enter the # to delete:"))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"task {tasktodelete} has been removed.")
        else:
            print(f"task # {tasktodelete}was not found.")
    except:
            print("invaild input.")
if __name__ == "__main__":
##createing a loop to run the app
    print("welcome to the to do list app :")
    while True:
         print("\n")
         print("please select one of the following option ")
         print("1. Add a new task ")
         print("2. Delete a task")
         print("3. List tasks")
         print("4. Quit ")
         choice = input("enter your choice: ")
         if (choice =="1"):
            addtask()
         elif(choice == "2"):
            deletetask()
         elif(choice == "3"):
            listtask()
         elif(choice == "4"):
          break
         else:
            print("Invaild input. please try again.")
            print("Tata👋👋")