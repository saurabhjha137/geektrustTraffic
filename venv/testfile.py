# vehicle speed, in megamiles/hour
CAR_SPEED = 20
BIKE_SPEED = 10
TUKTUK_SPEED = 12

# vehicle time, to cross each crater in minutes
CAR_CRATER_TIME = 3
BIKE_CRATER_TIME = 2
TUKTUK_CRATER_TIME = 1

# weather in which vehicle can travel
CAR_WEATHER = ['RAINY', 'SUNNY', 'WINDY']
BIKE_WEATHER = ['SUNNY', 'WINDY']
TUKTUK_WEATHER = ['SUNNY', 'RAINY']

class Car:
    # initializes car time to cross a crater
    def __init__(self):
        self.carCraterTime = CAR_CRATER_TIME

    # checks if car can travel in input weather
    def if_car_can_travel(self, weather):
        if weather not in CAR_WEATHER:
            return False

    # update car speed
    def update_speed(self, orbitTrafficSpeed):
        if (int(orbitTrafficSpeed) <= CAR_SPEED):
            self.carSpeed = orbitTrafficSpeed
            print(self.carSpeed)
        else:
            self.carSpeed = CAR_SPEED
            print(self.carSpeed)


class Bike:
    #initializes bike time to cross a crater
    def __init__(self):
        self.bikeCraterTime = BIKE_CRATER_TIME

    # checks if bike can travel in input weather
    def if_bike_can_travel(self, weather):
        if weather not in BIKE_WEATHER:
            return False

    # update bike speed
    def update_speed(self, orbitTrafficSpeed):
        if (int(orbitTrafficSpeed) <= BIKE_SPEED):
            self.bikeSpeed = orbitTrafficSpeed
            print(self.bikeSpeed)
        else:
            self.bikeSpeed = BIKE_SPEED
            print(self.bikeSpeed)


class Tuktuk:
    # initializes tuktuk time to cross a crater
    def __init__(self):
        self.tuktukCraterTime = TUKTUK_CRATER_TIME

    # checks if tuktuk can travel in input weather
    def if_tuktuk_can_travel(self, weather):
        if weather not in TUKTUK_WEATHER:
            return False

    # update tuktuk speed
    def update_speed(self, orbitTrafficSpeed):
        if (int(orbitTrafficSpeed) <= TUKTUK_SPEED):
            self.tuktukSpeed = orbitTrafficSpeed
            print(self.tuktukSpeed)
        else:
            self.tuktukSpeed = TUKTUK_SPEED
            print(self.tuktukSpeed)

class Vehicle(Bike,Car,Tuktuk):
    # updates the speed of Vehicles according to orbitTrafficSpeed
    def update_vehicles_speed(self, orbitTrafficSpeed):
        Car.update_speed(self, orbitTrafficSpeed)
        Bike.update_speed(self, orbitTrafficSpeed)
        Tuktuk.update_speed(self, orbitTrafficSpeed)

    

if __name__ == '__main__':
    demo = Vehicle()
    demo.update_vehicles_speed(25)