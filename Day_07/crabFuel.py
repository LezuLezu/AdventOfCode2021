from collections import defaultdict

def getData():      
    #read data from file into list
    with open("Day_07/data.txt", "r") as file:
        data = [int(x) for x in file.read().strip().split(',')]
    return data

#test data list
test_data = [16,1,2,0,4,2,7,1,2,14]         

def getFuel(data):      #part one
    totalFuel = float('inf')        #unbound upper vallue
    for pos in range(min(data), max(data) +1):      #loop trough data lists in range in min and max data 
        current_fuel = 0        #fuel use set to zero   
        for num in data:        #loop trough numbers in data list   
            current_fuel += abs(num - pos)      #calculate difference in number and position in data list to get used fuel
        totalFuel = min(totalFuel, current_fuel)    #redefine totalFuel to the least amount of fuel in current fuel -> is current or total fuel smaller?
    # print(totalFuel)
    return totalFuel        #return smalles amount of fuel used

def getFuel_part2(data):        #part two
    totalFuel = float('inf')        #unbound upper vallue
    for pos in range(min(data), max(data) +1): #loop trough data lists in range in min and max data 
        current_fuel = 0        #fuel use set to zero   
        for num in data:        #loop trough numbers in data list 
            multiplier = abs(pos - num)     #calculate the multiplier, by getting the difference between number and position, to calculate fuel in next step
            current_fuel += multiplier * (multiplier + 1) // 2      #calculate the fuel use witht the multiplier -> fuel = n * (n+1) // 2
        totalFuel = min(totalFuel, current_fuel)        #redefine totalFuel to the least amount of fuel in current fuel -> is current or total fuel smaller?
    return totalFuel

if __name__ == "__main__":  
    data = getData()
    # print(data)
    print("\nPart 1")
    print("Test Data: %s"%(getFuel(test_data)))
    print("CrabFuel: %s" %(getFuel(data)))

    print("\nPart 2")
    print("Test Data: %s"%(getFuel_part2(test_data)))
    print("CrabFuel: %s" %(getFuel_part2(data)))

