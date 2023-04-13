""" Item class for each item in the TODO list"""

class Item:
    def __init__(self, name, details):
        self.name = name
        self.details = details
    
    def __repr__(self):
        return f"Task - {self.name}\nTask Details:\n{self.details}"