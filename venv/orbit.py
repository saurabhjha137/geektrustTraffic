# decrease in crater as per weather
PERCENT_CHANGE_IN_SUNNY = 10
PERCENT_CHANGE_IN_RAINY = -20
PERCENT_CHANGE_IN_WINDY = 0

# Orbit distance in megamiles
ORBIT1_DISTANCE = 18
ORBIT2_DISTANCE = 20

# no of craters in orbits
ORBIT1_CRATER = 20
ORBIT2_CRATER = 10


class Orbit:
    #initalizes orbit Distance
    def __init__(self, distance, numberOfCraters):
        self.orbit1Distance = ORBIT1_DISTANCE
        self.orbit2Distance = ORBIT2_DISTANCE


    # decrease/increase the pecentage of crater
    def percentage_change_in_crater(self, percentChange):
        change = (ORBIT1_CRATER * percentChange)/100
        self.orbit1Crater = ORBIT1_CRATER - change
        change = (ORBIT2_CRATER * percentChange) / 100
        self.orbit2Crater = ORBIT2_CRATER - change


    # depending upon the weather, changes crater in each orbit
    def change_in_crater(self, weather):
        if weather == 'SUNNY':
            self.percentage_change_in_crater(PERCENT_CHANGE_IN_SUNNY)
        elif weather == 'RAINY':
            self.percentage_change_in_crater(PERCENT_CHANGE_IN_RAINY)
        elif weather == 'WINDY' :
            self.percentage_change_in_crater(PERCENT_CHANGE_IN_WINDY)