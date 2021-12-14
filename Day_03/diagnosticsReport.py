from collections import Counter

def getData():
    # put data from txt file (data coppied from web input) into a list
    data = []
    with open('Day_03/data.txt', 'r') as f:
        dataF = f.read().split('\n')
        for i in dataF:
            data.append(i)   
    # print(data)
    return data

def getPowerCons(data):   
    # finding most common bits on indexes using Counter 
    num_1 = ""
    num_2 = ""
    for index in range(len(data[0])):
        tempNum = Counter()
        # put data to Counter list/dict
        for line in data:
            tempNum[line[index]] += 1
        # print(tempNum)
        # Check for each index which amount of byte is larger and add that to new number
        if tempNum["1"] > tempNum["0"]:
            num_1 += "1"
            num_2 += "0"
        else: 
            num_1 += "0"
            num_2 += "1"
    # print(num_1)
    # print(num_2)
    # Calculate final number
    return(int(num_1, 2) * int(num_2, 2)) # num_1 and num_2 are binary, ($,2) converts it to decimal

def getCO2(data):
    # main part two function
    num_1 = getNum1(data)
    num_2 = getNum2(data)
    # print(num_1)
    # print(num_2)
    return(int(num_1, 2) * int(num_2, 2)) # num_1 and num_2 are binary, ($,2) converts it to decimal

def getNum1(data):
    # find first number part two
    for index in range(len(data[0])):
        tempNum = Counter()
        for number in data:
            # make counter list for each index counting how many 0 and 1 are in each index
            tempNum[number[index]] += 1
        # print(tempNum)
        if tempNum["1"] >= tempNum["0"]:
            # see if amount of 1 is greater or equal to amount of 0 each index
            data = [j for j in data if j[index] == "1"]
        else:
            data = [j for j in data if j[index] == "0"]
        # print(data[0])
        if len(data) == 1:
            return data[0]
    # print(data[0])
    return data[0] 

def getNum2(data):
    # Find second number part two
    for index in range(len(data[0])):
        tempNum = Counter()
        for number in data:
            # make counter list for each index counting how many 0 and 1 are in each index
            tempNum[number[index]] += 1
        # print(tempNum)
        if tempNum["0"] <= tempNum["1"]:
            # see if amount of 1 is smaller or equal to amount of 0 each index
            data = [j for j in data if j[index] == "0"]
        else:
            data = [j for j in data if j[index] == "1"]
        # print(data[0])
        if len(data) == 1:
            return data[0]
    # print(data[0])
    return data[0]


if __name__ == "__main__":  #lets do it the way it should be done
    # Put data from txt file into a var
    data = getData()

    print("\n")

    powerConsumtion = getPowerCons(data)
    print("Power consumption: %s" %(powerConsumtion))

    print("\n")

    lifeSupport = getCO2(data)
    print("Life support rating: %s" %(lifeSupport))

    print("\n")

