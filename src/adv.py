from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


rock = Item("Rock", "This is a rock.")
sword = Item("Sword", "This a sword")

sandwich = Item("Sandwich", "This is a tasty sandwich.")
apple = Item("Apple", "This is a delicious red apple.")

blanket = Item("Blanket", "A blanket to keep you warm.")
nugget = Item("Nugget", "A small shiny gold piece")


player = Player("Jarrad", room['outside'])

#make it so that the player can pick up items from a room instead of hard coding

room["outside"].items.append(rock)
room["foyer"].items.append(blanket)
room["overlook"].items.append(sword)
room["narrow"].items.append(sandwich)
room["treasure"].items.append(nugget)
room["outside"].items.append(apple)

player.items.append(sandwich)


current_room = player.current_room

print(current_room)


valid_inputs = ["n", "s", "e", "w", "q", "i", "get", "drop"]

while True:
    # Wait for user input
    cmd = input("-> ")
    # Parse user inputs (n, s, e, w, q, i, get, drop)
    if cmd in valid_inputs:
        # If input is valid, move the player and loop
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd == "q":
        print("Goodbye!")
        exit()

    elif cmd == "get":
        item = player.current_room.get_item(cmd)
        if item == None:
            print("That item is not in the room.")
        else:
            player.current_room.items.remove(item)
            player.items.append(item)
            item.on_take()

    elif cmd == "drop":
        item = player.get_item(cmd)
        if item == None:
            print("That item is not in your inventory.")
        else:
            player.current_room.items.append(item)
            player.items.remove(item)
            item.on_drop()

    else:
        print("I did not recognize that command") 