class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.get_room_number()] = room

    def get_room(self, room_number):
        return self.rooms.get(room_number)


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.is_locked = False

    def get_room_number(self):
        return self.room_number

    def set_side(self, direction, site):
        if direction == "north":
            self.north = site
        elif direction == "south":
            self.south = site
        elif direction == "east":
            self.east = site
        elif direction == "west":
            self.west = site

    def get_side(self, direction):
        if direction == "north":
            return self.north
        elif direction == "south":
            return self.south
        elif direction == "east":
            return self.east
        elif direction == "west":
            return self.west

    def lock(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked


class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def is_door_open(self):
        return self.is_open


class Wall:
    pass

# we can make this design more flexible by using creational patterns
def CreateMaze():
    maze = Maze()
    room1 = Room(1)
    room2 = Room(2)
    door = Door(room1, room2)

    room1.set_side("east", door)
    room1.set_side("north", Wall())
    room1.set_side("south", Wall())
    room1.set_side("west", Wall())
    

    room2.set_side("west", door)
    room1.set_side("north", Wall())
    room1.set_side("south", Wall())
    room1.set_side("east", Wall())

    maze.add_room(room1)
    maze.add_room(room2)

    return maze


# Example usage
if __name__ == "__main__":
    maze = CreateMaze()

    current_room = maze.get_room(1)
    assert current_room.get_side("east").is_door_open() == True

    # Open the door and check again
    # door.open()
    # assert current_room.get_side("east").is_door_open() == True
