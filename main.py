# Imports

from item import Item
from list import TODO
from help import help

import os

# Start up

print("TODO-list - v0.1")
print("\n\n\n")

# Lists

MainL = TODO("TODO-List", "Added")
Archive = TODO("Task Archive", "Archived")

# Main loop

while True:
    text = input("> ")
    if text.strip() == "": continue

    else:
        match text:
            # Help commands

            case "clear":
                os.system("clear")
            case "exit":
                exit()
            case "help":
                print(help())
            case "archive":
                for string in Archive.__repr__():
                    print(string)
            case "todo":
                for string in MainL.__repr__():
                    print(string)
            
            # List commands

            # Adds an item class to the MainL class dict
            case "new item":
                os.system("clear")
                name = input("Input name of task\n: ")
                os.system("clear")
                details = input("Input task details\n: ")
                os.system("clear")

                task = Item(name, details)
                MainL.addTask(task)
            
            # removes an item class from the MainL class dict
            case "remove item":
                os.system("clear")
                name = input("Input name of task\n: ")

                MainL.removeTask(name)
            
            case "done item":
                os.system("clear")
                name = input("Input name of task\n: ")

                task = MainL.getTask(name)
                MainL.removeTask(name)

                Archive.addTask(Item(task[0], task[1]))
            
            case _:
                print(f"'{text}' isn't a command")
    print("")
                
            

