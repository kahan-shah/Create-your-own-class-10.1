# Kahan Shah
# Assignment 10.1 Your Own Class
# This program implement classes representing different rooms.It also allows you to add furniture to the rooms
# Acknowledgements: https://www.geeksforgeeks.org/python-classes-and-objects/ , https://www.programiz.com/python-programming/class , my roomie Arin Gadre for point out the breakpoint I accidently left and forgot to delete.

# This fuction  stops the user from adding things that are not on the furniture list using the init function.
class NotBedroomFurnitureError(TypeError):
    def __init__(self, message, bedroom_furniture, list_of_bedroom_furniture):
        self.message = message
        self.not_bedroom_furniture = bedroom_furniture
        self.acceptable_bedroom_furniture = list_of_bedroom_furniture
        super().__init__(self.message)
    def __str__(self):
        return (f"{self.message} :: {self.not_bedroom_furniture} are not furniture. Acceptable furniture are: {self.acceptable_bedroom_furniture}")
    pass

# The main class is the Room class; it sets up the whole rest of the program. 
class Room:
    # The Room class sets up the dictionary
    def __init__(self, furniture_dict=None):
        if furniture_dict is None:
            self.__room = {}
        else:
            self.__room = {}
            for furniture, count in furniture_dict.items():
                self.__room[furniture.lower()] = count
        self.set_total()
    # The  str function makes the self.__room a string and call it Room.
    def __str__(self):
        return (f"Room ({self.total}): {str(self.__room)}.")
    # The set_total function calculates the amount of furniture is being added and how much of each furniture is being added to the room.
    def set_total(self):
        self.total = sum(list(self.__room.values()))
    # The add_furniture adds pieces of furniture and allows the user to add different types of furniture at the same time.
    def add_furniture(self, furniture_name, count):
        if furniture_name in self.__room.keys():
            self.__room[furniture_name.lower()] += count
            self.set_total()
        else:
            self.__room[furniture_name.lower()] = count
    # The remove_furniture function removes furniture and can be used to remove different types of furniture at the same time
    def remove_furniture(self, furniture_name, count):
        if furniture_name in self.__room.keys():
            self.__room[furniture_name] -= count
            if self.__room[furniture_name] <= 0:
                del self.__room[furniture_name]
            self.set_total()
class Bedroom(Room):
    bedroom_furniture = ["bed", "nightstand", "dresser", "closet", "table", "rug", "framed posters", "mirror", "lamp", "mattress", "TV stand", "chair", "sofa", "TV", "coffe table", "footstool"] 
    def __init__(self, furniture_dict=None):
        # Clean dict so it's only furniture
        only_bedroom_furniture = {}
        for furniture, count in furniture_dict.items():
            if furniture in self.bedroom_furniture:
                only_bedroom_furniture[furniture] = count
        super().__init__(only_bedroom_furniture)
    def add_furniture(self, furniture_name, count):
        # Only add furniture if it is for the bedroom
        if furniture_name in self.bedroom_furniture:
            super().add_furniture(furniture_name, count)
        else:
            raise NotBedroomFurnitureError("This is not a piece of furniture", furniture_name, self.bedroom_furniture)
# The demo code.
def main():
    sample_room = Room({"sofa":2, "chair":5, "table":1})
    print(sample_room)
    sample_room.remove_furniture("chair", 3)
    print(sample_room)
    sample_room.remove_furniture("sofa", 2)
    print(sample_room)
    empty_room = Room()
    print(empty_room)
    empty_room.add_furniture("sofa", 3)
    print(empty_room)
    sample_bedroom = Bedroom({"nightstand":2, "bed":1, "mattress":1, "rug":1})
    print(sample_bedroom)
    sample_bedroom.add_furniture("framed posters", 3)
    print(sample_bedroom)
    try:
        sample_bedroom.add_furniture("massage chair", 2)
    except NotBedroomFurnitureError as e:
        print(e)
        print("Relaunch program and try again :(")
if __name__ == "__main__":
    main()