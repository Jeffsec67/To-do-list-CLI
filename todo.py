import json


def load_tasks(filename="tasks.json"):
    tlist = list()
    try:
        with open(filename, "r") as f:
            tlist = json.load(f)
    except FileNotFoundError:
        tlist = list()
    except json.JSONDecodeError:
        tlist = list()
    if not isinstance(tlist, list):
        tlist = list()
    return tlist
#Creates a load tasks function which lets you import your own existing file by name or if lef blank 
# will generate a fresh one, opens the file in read mode and makes a list in json format of the files
# content, and each line is a dictionary, and if the file couldnt be found or couldnt be converted 
# into json format it will return an empty list.

def save_tasks(tasks, filename):
    try:
        with open(filename, "w") as f:
            json.dump(tasks, f)
    except OSError:
        print("File error- check path or permissions")
#Appends the file with contents of the dynamic list of tasks with write mode of json and using the 
# 'dump' functionality

def add_tasks(tasks, newtask):
    newtask = {"task": newtask, "status": "incomplete"}
    tasks.append(newtask)
#This function just creates the add a task in general framework, configuration and 
# customization of the task is from another function. It also makes the task template.

def display_tasks(tasks):
    for position, task in enumerate(tasks):
        print(str(position) + " - " + task["task"] + " - " + task["status"])
#Puts current task list into a numbered list, then prints position or number for each task
# as well as what the task is and its status.

def complete_task(tasks, index):
    try:
        tasks[index]["status"] = "complete"
        success = True
        return success
    except IndexError:
        print("Invalid position within current list of tasks")
        success = False
        return success
    except TypeError:
        print("Requires numerical input")
        success = False
        return success
#Dont remember the index syntax much but I believe its how you parse and interact with
# specific objects of a dictionary, but this function just changes a tasks status to 
# complete, it accounts for trying to index over a task that doesnt exist and
# trying to enter a task number with something other than a number.

def delete_task(tasks, index):
    try:
        tasks.pop(index)
        success = True
        return success
    except IndexError:
        print("Invalid position within current list of tasks")
        success = False
        return success
    except TypeError:
        print("Requires numerical input")
        success = False
        return success
#Deletes a task completely by using pop. the list of tasks where you enter the task number, it 
# accounts for the same errors as the previous function.

unsaved_changes = False

filename = input("Enter filename: ")
if "/" in filename or "\\" in filename : 
    print("Warning: Invalid characters detected. Defaulting to tasks.json")
    filename = "tasks.json"
elif not filename:
    filename = "tasks.json"

tasks = load_tasks(filename)

while True:
    print("\nOptions :")
    print("'load'     - Lets you load tasks from your file or if left blank generates a fresh file to add tasks to.")
    print("'list'     - Lists current tasks, task number, and completion status in order. Note that unsaved tasks will appear as well.")
    print("'add'      - Adds a custom task and assumes it incomplete. Tasks added this way will require them to be saved to persist.")
    print("'save'     - Adds tasks made with add_tasks to the file. Call this at the end of each session.")
    print("'complete' - Changes tasks to being complete. Requires you enter task number.")
    print("'delete'   - Removes a task. Requires you enter task number.")
    print("'quit'     - Quits the program.")

    command = input("\nEnter command: ")

    if command == "quit":
        if unsaved_changes : 
            force = input("Warning - Unsaved changes detected. Are you sure you want to quit? (y/n): ")
            if force.lower() != 'y' :
                continue
        break

    elif command == "load":
        filename = input("Enter new filename: ")
        if "/" in filename or "\\" in filename :
            print("Warning: Invalid characters detected Defaulting to tasks.json")
            filename = "tasks.json"
        tasks = load_tasks(filename)
    

    elif command == "list":
        display_tasks(tasks)

    elif command == "add":
        newtask = input("Enter new task name: ")
        if len(newtask) <= 75 and newtask.strip():
            add_tasks(tasks, newtask)
            unsaved_changes = True
        else:
            print("75 character limit")

    elif command == "save":
        save_tasks(tasks, filename)
        unsaved_changes = False

    elif command == "complete":
        index = input("Enter Task number: ")
        if index.isdigit() and 0 < int(index) <= len(tasks):
            success = complete_task(tasks, int(index))
            if success:
                unsaved_changes = True
        else:
            print("Must be task number")

    elif command == "delete":
        index = input("Enter task number: ")
        if index.isdigit() and 0 < int(index) <= len(tasks):
            success = delete_task(tasks, int(index))
            if success:
                unsaved_changes = True
        else:
            print("Must be task number")

    else:
        print("Select option")