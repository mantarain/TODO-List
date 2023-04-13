"""returns help string to print out"""

def help():
    return """
        help            - prints out each command.
        clear           - clears the text out of the terminal.
        exit            - closes current session.
        archive         - shows the archive list
        todo            - shows the current todo list

        new item                            - creates a new task with name and details inpu.
        remove item                         - removes item with the given name.
        done item                           - archives item into an archive list (accessed with the "archive" command)
            """