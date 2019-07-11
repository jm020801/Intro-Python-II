class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __init__(self):
        return self.name
    
    def on_take(self):
        print(f"You picked up the: {self.name}")

    def on_drop(self):
        print(f"You drop the: {self.name}")