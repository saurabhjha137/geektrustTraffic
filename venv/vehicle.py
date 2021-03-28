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

class Vehicle:
    # initializes vehicle time to cross a crater
    def __init__(self):
        self.carCraterTime = CAR_CRATER_TIME
        self.bikeCraterTime = BIKE_CRATER_TIME
        self.tuktukCraterTime = TUKTUK_CRATER_TIME
        
    # checks if car can travel in input weather
    def if_car_can_travel(self, weather):
        if weather not in CAR_WEATHER:
            return False
    
    # checks if bike can travel in input weather
    def if_bike_can_travel(self, weather):
        if weather not in BIKE_WEATHER:
            return False
    
    # checks if tuktuk can travel in input weather
    def if_tuktuk_can_travel(self, weather):
        if weather not in TUKTUK_WEATHER:
            return False
            
    # update car speed
    def update_car_speed(self, orbitTrafficSpeed, CAR_SPEED):
        if (int(orbitTrafficSpeed) <= CAR_SPEED):
            self.carSpeed = orbitTrafficSpeed
        else:
            self.carSpeed = CAR_SPEED

    # update bike speed
    def update_bike_speed(self, orbitTrafficSpeed, BIKE_SPEED):
        if (int(orbitTrafficSpeed) <= BIKE_SPEED):
            self.bikeSpeed = orbitTrafficSpeed
        else:
            self.bikeSpeed = BIKE_SPEED

    # update tuktuk speed
    def update_tuktuk_speed(self, orbitTrafficSpeed, TUKTUK_SPEED):
        if (int(orbitTrafficSpeed) <= TUKTUK_SPEED):
            self.tuktukSpeed = orbitTrafficSpeed
        else:
            self.tuktukSpeed = TUKTUK_SPEED

    # updates the speed of Vehicles according to orbitTrafficSpeed
    def update_vehicles_speed(self, orbitTrafficSpeed):
        self.update_car_speed(orbitTrafficSpeed,CAR_SPEED)
        self.update_bike_speed(orbitTrafficSpeed,BIKE_SPEED)
        self.update_tuktuk_speed(orbitTrafficSpeed,TUKTUK_SPEED)


