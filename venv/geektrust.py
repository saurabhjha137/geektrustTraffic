import sys

if __name__ == '__main__':
    
    file = open('inputFile.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    for eachline in file.readlines():
        weather = eachline.split()[0]
        orbit1Speed = int(eachline.split()[1])
        orbit2Speed = int(eachline.split()[2])