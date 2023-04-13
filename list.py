"""List class to store Item instances for TODO-list"""

class TODO:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.tasks = {}
    
    def addTask(self, item):
        "Adds an item to class dict"
        self.tasks[item.name] = item.details
        print(f"{self.message} '{item.name}'")
    
    def removeTask(self, taskName):
        "Removes an item from class dict"
        if self.tasks[taskName]:
            del self.tasks[taskName]
            print(f"Removed '{taskName}'")
        else:
            return f"'{taskName}' is not a task"
    
    def getTask(self, taskName):
        "Gets an item from class dict"
        if self.tasks[taskName]:
            return taskName, self.tasks[taskName]
        else:
            return f"'{taskName}' is not a task"
    
    def __repr__(self):
        strList = []

        for k, v in self.tasks.items():
            string = f"Task: {k}\nDetails: {v}\n"
            strList.append(string)
        
        return strList

