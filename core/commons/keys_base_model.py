from datetime import datetime as dt

class KeysBaseModel:
    def __init__(self,
                 name: str, 
                 description: str = ""): 
        self.name = name
        self.description = description
        self.id = 1
        
    def __str__(self):
        return f"Type: {self.type}, name: {self.name}, description {self.description}"


