class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
print(p1.x)
print(p1.y)

#-------------------------------------------------------------#


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Add passengers to flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


f1 = Flight(3)

people = ["Harry", "Hermione", "Ginny", "Ron"]
for person in people:
    success = f1.add_passenger(person)
    if success:
        print(f'Added {person} to flight')
    else:
        print(f'Flight at capacity, {person} could not be added')
