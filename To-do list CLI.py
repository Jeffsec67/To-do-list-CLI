To-do list CLI
#Able to add tasks indefinately
#Able to change task from Done or not (dict)
#Store info in a file- essentially forever running
#the program runs until user quits, showing options
# and branching based on input
#Separate functions for adding, listing, completing, 
# and deleting. 
import json
def load_tasks(filename="tasks.json") : 
    tlist = list()
    try :
        with open(filename, "r") as f : 
            tlist = json.load(f)
            #json.load() gives every line as a dictionary
    except FileNotFoundError : 
        tlist = list() 
    except json.JSONDecodeError :
        tlist = list()
    return tlist       

def save_tasks(tasks, filename="tasks.json") : 
     with open(filename, "w") as f :
         json.dump(tasks, f)

def add_tasks(tasks, newtask) : 
#create custom task, assume not completed
    newtask = {"task" : newtask, "status" : "incomplete"}
    tasks.append(newtask)

def display_tasks(tasks) :
    for position, task in enumerate(tasks) :
        print(str(position) + " - " + task["task"] + " - " + task["status"])

def complete_task(tasks, index) : 
    try : 
        tasks[index]["status"] = "complete"
    except IndexError :
        print("Invalid position within current list of tasks")
    except TypeError :
        print("Requires numerical input")        

def delete_task(tasks, index) :
    try :
        tasks.pop(index)
    except IndexError :
        print("Invalid position within current list of tasks")
    except TypeError : 
        print("Requires numerical input")


#need user input for inqex queries
filename = input("Enter filename: ")
tasks = load_tasks(filename)
newtask = input() #integrate sec
while True :
        
#Options : 
#"load" Lets you load tasks from your file or if left
#                     blank generates a fresh file to add tasks to.

#"list" Lists current tasks, their number, and completion status 
#                     in order. Note that unsaved tasks will appear as well. 

#"add" Adds a custom task and assumes it incomplete.
#                          Tasks added this way will require them to be saved to persist.

#"save" Adds tasks made with add_tasks to the file.
#                            Call this at the end of each session.

#"complete" Changes tasks to being complete. 
#                            Requires you enter task number.

#"delete" Removes a task. Requires you enter task number.
#

      
    






































