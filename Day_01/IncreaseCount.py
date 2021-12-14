def getData():
    data = []
    with open('Day_01/data.txt', 'r') as f:
        dataF = f.read().split('\n')
        for i in dataF:
            data.append(int(i))   
    # print(data)
    return data

def getCount(data):
    counter = 0
    # print(len(data))
    for dept in range(len(data)):
        dept_1 = data[dept]
        dept_2 = data[dept - 1]
        # print(data[dept])
        # print(data[dept-1])
        if dept_1 > dept_2 :
            counter += 1
        # print(counter)
    return counter


def getTrippleCount(data):
    counter = 0
    try:
        for dept in range(len(data)):
            dept_1 = data[dept]
            dept_2 = data[dept + 1]
            dept_3 = data[dept + 2]
            dept_4 = data[dept + 3]
            deptA = dept_1 + dept_2 + dept_3
            deptB = dept_2 + dept_3 + dept_4
            if deptB > deptA :
                counter += 1
    except IndexError:
        return counter    
    return counter

def main():
    data = getData()
    # print(data)
    count = getCount(data)
    print(count)
    trippleCount = getTrippleCount(data)
    print(trippleCount)

main()