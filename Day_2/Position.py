
from os import popen


def getData():
    data = []
    for line in open('Day_2/data.txt', 'r'):
        items = line.rstrip('\n').split(' ')
        items = [item.strip() for item in items]
        items[1] = int(items[1])
        data.append(items)
    # print(data)
    return data

def getPosition(data):
    position = [0, 0] 
    #[horizontal, dept]
    for index in range(len(data)):
        if data[index][0] == "down":
            position[1] += data[index][1]
        elif data[index][0] == "up":
            position[1] -= data[index][1]
        elif data[index][0] == "forward":
            # print("forward %s"%(data[index][1]))
            position[0] += data[index][1]
        # print(position)
    return position

def getNewPosition(data):
    position = [0, 0]
    #[horizontal, dept]
    aim = 0
    for i in range(len(data)):
        if data[i][0] == "down":
            aim += data[i][1]
        if data[i][0] == "up":
            aim -= data[i][1]
        if data[i][0] == "forward":
            position[0] += data[i][1]
            position[1] += aim * data[i][1]
    return position

def main():
    data = getData()
    print("part one")
    position = getPosition(data)
    print("final position: %s " %(position))
    print(position[0] * position[1])
    print("\n\npart two")
    newPosition = getNewPosition(data)
    print("New position: %s" %(newPosition))
    print(newPosition[0] * newPosition[1])

main()