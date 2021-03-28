import sys
from orbit import Orbit
from calculateTime import CalculateTime


class InputOutputTask:
    def perform_input_task(self, inputFile):
        for eachLine in inputFile.readlines():
            weather = eachline.split()[0]
            orbit1Speed = int(eachline.split()[1])
            orbit2Speed = int(eachline.split()[2].replace('\n', ''))
            self.calcuate_time_to_travel(weather, orbit1Speed, orbit2Speed)

    def calcuate_time_to_travel(self, weather, orbit1Speed, orbit2Speed):
        calculateTime = CalculateTime()
        calculatedTime = calculateTime.find_total_time(weather, orbit1Speed, orbit2Speed)
        self.print_result(calculatedTime)

    def print_result(self, calculatedTime):
        output = list(calculatedTime.keys())[0]
        vehicle = output[0]
        orbit = output[1]
        if orbit == 1:
            print(vehicle, 'ORBIT1')
        else:
            print(vehicle, 'ORBIT2')
            


if __name__ == '__main__':
    
    inputFile = open('inputFile.txt', 'r+')
    # inputFile = open(sys.argv[1], 'r+')
    inputOutput = InputOutputTask()
    inputOutput.perform_input_task(inputFile)

    inputFile.close()
