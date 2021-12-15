def getData(path):          # fetch and parse data input
    data = []
    with open(path) as f:
        data=f.read().splitlines()
        data=[[int(num) for num in line] for line in data]
    return data

def getBasins(data):
    caves = []                                              # list to keep track of caves
    smallBasins = []                                        # list to keep track of small caves
    for row in range(len(data)):                            # loop trough rows in data
        for collumn in range(len(data[0])):                 # loop trough collumns in data
            basins = []                                     # list to keep track of basins 
            if row - 1 >= 0:                                # check if row index is 0 or greater
                basins.append(data[row - 1][collumn])       # add coords to basins list
            if row + 1 < len(data):                         # check if row index is smaller then lenght of data 
                basins.append(data[row + 1][collumn])       # add coords to basins list
            if collumn - 1 >= 0:                            # check if collumn index is 0 or greater
                basins.append(data[row][collumn -1])        # add coords to basins list
            if collumn + 1 < len(data[0]):                  # check if collumn index is smaller then lenght of data
                basins.append(data[row][collumn + 1])
            # Part one                
            if data[row][collumn] < min(basins):            # check if current coord position is smaller than smallest value in basins list
                smallBasins.append(data[row][collumn])      # current basins added to small basin list

                # Part two
                basins_part2 = [[row, collumn]]             # basin is current position in data
                for row_p2, collumn_p2 in basins_part2:     # loop trough coords from basins list part 2
                    if row_p2-1 >= 0 and data[row_p2-1][collumn_p2] != 9 and [row_p2-1,collumn_p2] not in basins_part2:                 # check if row is 0 or greater, check if coord doesnt equal 9, check if coord not already in part 2 list
                        basins_part2.append([row_p2-1,collumn_p2])                                                                      # add basin to part 2 list
                    if row_p2+1 < len(data) and data[row_p2+1][collumn_p2] != 9 and [row_p2+1,collumn_p2] not in basins_part2:          # check if row is 0 or greater, check if coord doesnt equal 9, check if coord not already in part 2 list
                        basins_part2.append([row_p2+1,collumn_p2])                                                                      # add basin to part 2 list
                    if collumn_p2-1 >= 0 and data[row_p2][collumn_p2-1] != 9 and [row_p2,collumn_p2-1] not in basins_part2:             # check if collumn is 0 or greater, check if coord doesnt equal 9, check if coord not already in part 2 list
                        basins_part2.append([row_p2,collumn_p2-1])                                                                      # add basin to part 2 list
                    if collumn_p2+1 < len(data[0]) and data[row_p2][collumn_p2+1] != 9 and [row_p2,collumn_p2+1] not in basins_part2:   # check if collums is 0 or greater, check if coord doesnt equal 9, check if coord not already in part 2 list
                        basins_part2.append([row_p2,collumn_p2+1])                                                                      # add basin to part 2 list
        
                caves.append(len(basins_part2))             # add lenght of part two list to cave list
    

    smallRisk = (sum(smallBasins)) + (len(smallBasins))     # calculate sum of part one, sum of coords + amount of small caves
    caves.sort()                                            # sort caves list, increasing
    # print(caves)
    bigCaves = caves[-1] * caves[-2] * caves[-3]            # multiplie the trhee largest caves (last three in list) with eachother
    return smallRisk, bigCaves                              # return values



if __name__ == "__main__":  
    test_data = getData("Day_09/test_data.txt")
    # print(test_data)
    data = getData("Day_09/data.txt")

    test_part_1, test_part_2 = getBasins(test_data)
    part_1, part_2 = getBasins(data)

    print("\nPart 1\n")
    print("Test data smallest cave risk calc: %s" %(test_part_1))
    print("Real data smallest cave risk calc: %s" %(part_1))


    print("\nPart 2\n")
    print("Test data biggest cave calc: %s" %(test_part_2))
    print("Real data biggest cave calc: %s" %(part_2))

    



