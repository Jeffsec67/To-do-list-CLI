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
        for task in tasks :
            print(task["task"] + " - " + task["status"])



filename = input("Enter filename: ")
tasks = load_tasks(filename)
newtask = input() #integrate sec
while True :
        


      
    






































