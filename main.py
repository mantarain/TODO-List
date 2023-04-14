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

                content = ["Main:\n", MainL, "\n", "Archive:\n", Archive, "\n"]
                sting = ""

                for cont in content:
                    if isinstance(cont, TODO):
                        string = str(cont.tasks)
                        sting += string
                    else:
                        sting += cont

                with open("TodoSave.txt", "w") as file:
                    file.write(sting)
                    file.close()
                
                exit()


            case "help":
                print(help())
            case "archive":
                for string in Archive.__repr__():
                    print(string)
            case "todo":
                for string in MainL.__repr__():
                    print(string)
            
            case "open":
                os.system("clear")
                path = input("Input name/path of file\n:")
                section = None
                main = {}
                arch = {}

                try:
                    with open(path, "r") as file:
                        fileStrs = file.read()
                        fileStrs = fileStrs.split("\n")
                        for string in fileStrs:

                            # Check for Main TODO list
                            if string == "Main:":
                                section = "Main"
                                continue
                            elif section == "Main":
                                main = eval(string)
                                section = None
                                continue
                            
                            # Check for Archived Tasks
                            if string == "Archive:":
                                section = "Archive"
                                continue
                            elif section == "Archive":
                                arch = eval(string)
                                section = None
                        
                        MainL.tasks = main
                        Archive.tasks = arch

                        print("downloaded tasks succefully!")
                
                except FileNotFoundError:
                    print(f"'{path}' was not found")

            
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
            
            # archives an item from MainL class into Archive dict
            case "done item":
                os.system("clear")
                name = input("Input name of task\n: ")

                task = MainL.getTask(name)
                MainL.removeTask(name)

                Archive.addTask(Item(task[0], task[1]))
            
            case _:
                print(f"'{text}' isn't a command")
    print("")
                
            

