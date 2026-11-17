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

def save_tasks(tasks, filename):
    try:
        with open(filename, "w") as f:
            json.dump(tasks, f)
    except OSError:
        print("File error- check path or permissions")

def add_tasks(tasks, newtask):
    newtask = {"task": newtask, "status": "incomplete"}
    tasks.append(newtask)

def display_tasks(tasks):
    for position, task in enumerate(tasks, start=1):
        print(str(position) + " - " + task["task"] + " - " + task["status"])

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