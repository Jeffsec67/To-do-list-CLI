import json
import shutil

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
    for position, task in enumerate(tasks, start=1):
        print(str(position) + " - " + task["task"] + " - " + task["status"])
#Puts current task list into a numbered list, then prints position or number for each task
# as well as what the task is and its status.

def complete_task(tasks, index):
    try:
        if tasks[index]["status"] == "complete":
            print("Task already complete")
            return False
        tasks[index]["status"] = "complete"
        return True
    except IndexError:
        print("Invalid position within current list of tasks")
        return False
    except TypeError:
        print("Requires numerical input")
        return False

#Dont remember the index syntax much but I believe its how you parse and interact with
# specific objects of a dictionary, but this function just changes a tasks status to 
# complete, it accounts for trying to index over a task that doesnt exist and
# trying to enter a task number with something other than a number.

def delete_task(tasks, index):
    try:
        tasks.pop(index)
        return True
    except IndexError:
        print("Invalid position within current list of tasks")
        return False
    except TypeError:
        print("Requires numerical input")
        return False
#Deletes a task completely by using pop. the list of tasks where you enter the task number, it 
# accounts for the same errors as the previous function.

unsaved_changes = False

def handle_add(tasks) :
    newtask = input("Enter new task name: ").replace("\n"," ").replace("\r", " ")
    if len(newtask) <= 75 and newtask.strip():
        add_tasks(tasks, newtask)
        return True
    else :
        print("75 Character limit")
        return False

def handle_complete(tasks) :
    index = input("Enter Task number: ")
    if index.isdigit() and 0 < int(index) <= len(tasks):
        return complete_task(tasks, int(index) - 1)
    else:
        print("Must be task number")
        return False

def handle_delete(tasks) :
    index = input("Enter task number: ")
    if index.isdigit() and 0 < int(index) <= len(tasks):
        return delete_task(tasks, int(index) - 1)
    else :
        print("Must be task number")
        return False
    
def handle_load() :
    filename = input("Enter new filename: ").strip()
    if not filename : 
        filename = "tasks.json"
        print("No filename entered, Defaulting to tasks.json")
    elif len(filename) > 75 : 
        print("75 character limit, Defaulting to tasks.json")
        filename = "tasks.json"
    elif "/" in filename or "\\" in filename :
        print("Warning: Invalid characters detected Defaulting to tasks.json")
        filename = "tasks.json"
    tasks = load_tasks(filename)
    return tasks, filename

def handle_backup(filename) :
    backup_name = "backup_" + filename 
    shutil.copy(filename, backup_name)
    print("Backup successful") 

print("Booting CLI...")
tasks, filename = handle_load() 

while True:
    print("\nOptions :")
    print("'load'     - Lets you load tasks from your file or if left blank generates a fresh file to add tasks to.")
    print("'list'     - Lists current tasks, task number, and completion status in order. Note that unsaved tasks will appear as well.")
    print("'add'      - Adds a custom task and assumes it incomplete. Tasks added this way will require them to be saved to persist.")
    print("'save'     - Adds tasks made with add_tasks to the file. Call this at the end of each session.")
    print("'complete' - Changes tasks to being complete. Requires you enter task number.")
    print("'delete'   - Removes a task. Requires you enter task number.")
    print("'backup'   - Makes a backup copy of current saved changes")
    print("'quit'     - Quits the program.")

    command = input("\nEnter command: ")

    if command == "quit":
        if unsaved_changes : 
            force = input("Warning - Unsaved changes detected. Are you sure you want to quit? (y/n): ")
            if force.lower() != 'y' :
                continue
        break

    elif command == "load":
        tasks, filename = handle_load()
    

    elif command == "list":
        display_tasks(tasks)

    elif command == "add":
        if handle_add(tasks) :
            unsaved_changes = True

    elif command == "save":
        save_tasks(tasks, filename)
        unsaved_changes = False

    elif command == "complete":
        if handle_complete(tasks) :
            unsaved_changes = True

    elif command == "delete":
        if handle_delete(tasks) :
            unsaved_changes = True

    elif command == "backup":
        handle_backup(filename)

    else:
        print("Select option")