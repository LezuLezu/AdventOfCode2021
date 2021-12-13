
def solve(path):
    p1_complete = False                                                                 # part one not completed
    gridDict = {}                                                                       # empty dictionary for coords
    for line in open(path):                                                             # loop trough input  
        line = line.strip()         
        if line and line.startswith("f"):                                               # if the line starts with f -> fold at x
            gridDict_temporary = {}                                                     # empty temporary dict
            ins = line.split()[-1]                                                      # the fold instruction line
            text, coord = ins.split("=")                                                # split the instructions at = to get the x or y asis and coord
            coord = int(coord)                                                          # set string coord to integer
            if text == "x":                                                             # if the text from instruction x asis
                for (x,y) in gridDict:                                                  # loop trough coords in gridDict
                    if x < coord:                                                       # if the x coord from the dict is smaller than the coord given in instruction
                        gridDict_temporary[(x, y)] = True                               # add the coords to dict with value True
                    else:                                                               # the x coord from the dict is greater than given in instruction
                        gridDict_temporary[(coord-(x-coord), y)] = True                 # calculate new x coord  and add new x and y to dicht with value True
            else:
                assert text == "y"                                                      # axis from text instruction is y, or raise exception
                for (x,y) in gridDict:                                                  # loop trough dict
                    if y < coord:                                                       # if the y coord from the dict is smaller than the coord given in instruction
                        gridDict_temporary[(x, y)] = True                               # add the coords to dict with value True
                    else:                                                               # the y coord from the dict is greater than given in instruction
                        gridDict_temporary[(x, coord-(y-coord))] = True                 # calculate new x coord  and add new x and y to dicht with value True
            gridDict = gridDict_temporary                                               # gridDict becomes the tempDict
            if not p1_complete:                                                         # part one is now complete
                p1_complete = True                                                      # set to True so it doesnt start again
                print("\nPart 1: %s \n\nPart 2: \n" %(len(gridDict_temporary)))         # print the amount of dots (part 1)

        elif line:                                                                      # line does not start with f 
            x, y = [int(coord) for coord in line.strip().split(",")]                    # get x and y coords from input
            gridDict[(x,y)] = True                                                      # add them to dict with value True
    max_x = max([x for x,y in gridDict.keys()])                                         # get the highest coord of the x axis
    max_y = max([y for x,y in gridDict.keys()])                                         # get the highest coord of the y axis
    ans = ''                                                                            # ans is empty, to be filled
    for y in range(max_y + 1):                                                          # loop in the range of max y
        for x in range(max_x + 1):                                                      # loop in the range of max x
            ans += ("x" if (x,y) in gridDict else " ")                                  # add an x to ans if the coord is in the dict, of add an empty space
        print(ans)                                                                      # print the line (part 2)
        ans = ""                                                                        # reset ans
                                                                                        # printed x's will form capital letters



if __name__ == "__main__":  
    test_path = "Day_13/test_data.txt"
    path =  "Day_13/data.txt"

    print("\nTest data input")
    solve(test_path)


    print("\n\nReal data input")
    solve(path)
