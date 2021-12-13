import numpy as np

def getFlashingOctopi(path):
    flashes = 0                                                             # set flashes to 0
    step = 0                                                                # set steps to 0
    grid = np.genfromtxt(path, delimiter = 1)                               # create numpy grid from input file
    # print(grid)
    while np.any(grid):                                                     # keep looping untill all octopi flash
        step += 1                                                           # each loop add a step
        grid += 1                                                           # each loop octopi get new energy
        flash = np.argwhere(grid > 9)                                       # if octopi has 9 energy it flashes
        while len(flash):                                                   # loop for the amount of flashes
            for (x, y) in flash:                                            # get the coord of flashes
                neighbors = np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2] # get surrounding octopi 
                grid[neighbors] += grid[neighbors] > 0                      # give them energy
                grid[x,y] = 0                                               # reset octopus its energy
            flash = np.argwhere(grid > 9)                                   # check for new flashing octopie, this keeps going till no flash
        flashes += np.count_nonzero(grid == 0)                              # flash get added to counter
        if step == 100:                                                     # at step hundred
            print("Amount of flashes at step 100: %s" %(flashes))           # print the amount of flashes
    
    print("Step where all octopi flash: %s" %(step))                        # after ending the while loop (all octopi flash), print the step



if __name__ == "__main__":  
    print("\nTest Data")
    getFlashingOctopi("Day_11/test_data.txt")


    print("\nReal data\n")
    getFlashingOctopi("Day_11/data.txt")
    print("\n")

