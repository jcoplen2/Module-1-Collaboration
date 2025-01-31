#module 3 case study. Working with classes
#author - jessi coplen
#last updated 1/231/2025
#description

#create parent class and add attribute
class Vehicle():
    def __init__(self, type):
        self.type = type

#create subclass and attributes 
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#function to get user input
def create_vehicle():

    #validate vehicle type input
    type = input("Please enter the vehicle type: ")
    while not type.strip():
        print("Vehicle type cannot be empty.")
        type = input("Please enter the vehicle type: ")

    #validate year input
    year = input("Please enter the year for the vehicle: ")
    while not year.isdigit() or not (1880 <= int(year) <= 2025):
        print("Year must be a number between 1880 and 2025.")
        year = input("Please enter the year for the vehicle: ")
    year = int(year)
    
    #validate make input
    make = input("Please enter the make for the vehicle: ")
    while not make.strip():
        print("Vehicle make cannot be empty.")
        make = input("Please enter the make for the vehicle: ")

    #validate model input
    model = input("Please enter the model for the vehicle: ")
    while not model.strip():
        print("Vehicle model cannot be empty.")
        model = input("Please enter the model for the vehicle: ")

    #validate number of doors
    doors = input("Does the vehicle have 2 or 4 doors? ")
    while doors not in ['2','4']:
        print("Please enter either 2 or 4 for the number of doors.")
        doors = input("Does the vehicle have 2 or 4 doors? ")
    doors = int(doors)

    #validate the rood input
    roof = input("Does the vehicle have a solid roof or sunroof? ")
    while roof.lower() not in ['solid', 'sunroof']:
        print("Please enter either 'solid' or 'sunroof' for the roof type.")
        roof = input("Does the vehicle have a solid roof or sunroof? ")


#create object
    vehicle = Vehicle(type)
    car = Automobile(type, year, make, model, doors, roof)

#print output
    print("\nVehicle type: ", car.type)
    print("Year: ", car.year)
    print("Make: ", car.make)
    print("Model: ", car.model)
    print("Number of doors: ", car.doors)
    print("Type of roof: ", car.roof)

def main():
    vehicle = create_vehicle()

main()
