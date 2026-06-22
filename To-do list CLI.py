To-do list CLI
#Able to add tasks indefinately
#Able to change task from Done or not (dict)
#Store info in a file- essentially forever running
#the program runs until user quits, showing options
# and branching based on input
#Separate functions for adding, listing, completing, 
# and deleting. 

def load_tasks(filename="tasks.json") :
#the function has a default parameter if undefined, 
# retains user input for existing file option
#try to open file if breaks,
# except SomeError:do this if it breaks with this error    
    tlist = list()
    try :
        with open(filename, "r") as f :
            for line in f : 
                if "." in line and "-" in line : 
            #####if file is in "1. Task - Done" format#####
                    number, rest = line.split(".", 1) 
            #get number from rest of line, 
            # and 1 is how many splits you need
            # number gets the first half
            # rest gets the second half
            # "1." is now gone from the line
                    task, status = rest.split("-", 1)
            #split the REST of the line (no more "1.")
            # task gets first half, status the second
                    number, task, status = number.strip(), task.strip(), status.strip()
            #removes spaces from front and back " Hello "
                    fulltask = {"number_key": number, "task_key": task, "status_key": status}
                    tlist.append(fulltask)
            #all task contents go into their own dict
            #all dictionaries go into one list
    except FileNotFoundError : 
        tlist = list() 
    return tlist
    #make tlist accessable outside the function

def save_tasks() : 
#load file and append it
        





filename = input("Enter filename: ")
tasks = load_tasks(filename)
while True :
        


      
    






































