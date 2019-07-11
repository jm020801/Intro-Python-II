# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! There's no room this way...", "\n")
    def _get_item_string(self):
        if len(self.items) > 0:
            return "\n" + ", ".join([item.name for item in self.items]) + "\n"
        else:
            return ""
    def print_inventory(self):
        print("You are carrying:\n " + ", ".join([item.name for item in self.items]) + "\n")
