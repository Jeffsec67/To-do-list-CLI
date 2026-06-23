To-do list CLI General functions
-Allows loading a preexisting list or file of tasks, listing/presenting tasks, changing completion status, and adding or removing tasks.
-Runs until quit, showing options and branching based on user input 
-Able to add tasks indefinitely 
-Stores tasks and completion status in json file 


load_tasks function
-Has a default parameter for file opening if user
doesnt select one themselves
-So we try to open a file in read mode and assign all the tasks to a variable via the json.load() function. 
-The except contains the specific expected error in this situation and instead of sending that error it assigns an empty list as the variable.
-json.load() converts all text within any file that is in json format to dictionaries, i.e. converting every task into its own dictionary. 
