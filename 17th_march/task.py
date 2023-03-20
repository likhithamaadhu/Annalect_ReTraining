class Task():
    def __init__(self,taskName,description,priority):
        self.taskName=taskName
        self.description=description
        self.priority=priority

    def __repr__(self):
        return f"Name: {self.taskName}\nDescrption: {self.description}\nPriority: {self.priority}"