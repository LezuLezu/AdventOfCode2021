def getData(path):      # fetch and pase input file
    data = []
    with open(path) as file:
        data=file.read().splitlines()
        data=[[int(num) for num in line] for line in data]
    return data

def check(position, array):
    return position[0] in range(len(array)) and position[1] in range(len(array[0]))         # check if given positions are within the array

def expand(data):       # function to expand the data array 5 times in length and 5 times in width
    expand = [[0 for x in range(5 * len(data[0]))] for y in range(5 * len(data))]
    for x in range(len(expand)):
        for y in range(len(expand[x])):
                dist = x // len(data) + y // len(data[0])
                newval = data[x % len(data)][y % len(data[0])]
                for i in range(dist):                       # each exspansion gets a higher value
                    newval += 1
                    if newval == 10:                          # if the value reaches 10 it gets set to 1
                        newval = 1
                expand[x][y] = newval
    data = expand
    return data

def getRiskPath(data, partTwo = False):
    if partTwo:
        data = expand(data)                                                 # use expand function if its for part two
    queue = [(0, 0, 0)]                                                     # queue list, with starting risk and position
    coords = {}                                                             # coord dict
    while True:
        risk, x, y = queue[0]                                               # fetch risk, x and y coord from list
        if (x == len(data) - 1) and (y == len(data[0]) - 1):                # when data from list are the same lenght as input data loop is complete and final output is printed
            if partTwo:
                print("Part two: %s" %(risk))
            else:
                print("Part one: %s" %(risk))
            break
        queue=queue[1:]                                                     # current queue is queue wihtout starting position
        for xx, yy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:     # xx, yy are coords from data input
            if check((xx, yy), data):
                riskCalc = risk + data[xx][yy]                              # calculate the risk of the step
                # print(nc)
                if (xx, yy) in coords and coords[(xx, yy)] <= riskCalc:     # check if this is the smallest option
                    continue
                coords[(xx, yy)] = riskCalc                                 # risk added to coord dict as value
                queue.append((riskCalc, xx, yy))                            # risk and coords are added to the queue
        queue = sorted(queue)                                               # que is sorted 





if __name__ == "__main__":
    test_data = getData("Day_15/test_data.txt")
    # print(test_data)

    print("\nTest data")
    getRiskPath(test_data)
    getRiskPath(test_data, partTwo=True)

    print("\nReal data")
    data = getData("Day_15/data.txt")
    getRiskPath(data)
    getRiskPath(data, partTwo=True)
