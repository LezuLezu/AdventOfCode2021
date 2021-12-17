def launchProbe(data):
    # print(data)
    velocityPairsCount = 0                  
    max_y = 0   
    for X in range(300):                    # X range of 300 for x coords
        for Y in range(-300, 1000):         # Y range of -300 to 1000 for y coords
            inRange = False                 # set vars to default
            posible_y = 0
            x = 0
            y = 0
            x_coord = X                     # coords are loop index
            y_coord = Y
            for step in range(1000):        # loop 1000 steps for velocity increase / decrease
                x += x_coord    
                y += y_coord
                posible_y = max(posible_y, y)
                if x_coord > 0:
                    x_coord -= 1
                elif x_coord < 0:
                    x_coord += 1
                y_coord -= 1
                if data[0] <= x <= data[1] and data[2] <= y <= data[3]:              
                    inRange = True                  # if coords are withing range of the wanted area
            if inRange:                               
                velocityPairsCount += 1             # increase pair counter for part 2
                if posible_y > max_y:               # check if current y coord is higher than current highest
                    max_y = posible_y
                    # print("added")
    # print("P1: %s"% (max_y))
    # print("P2: %s" %(velocityPairsCount))
    return max_y, velocityPairsCount                # return vallues of paircounter and highest y coord
  

if __name__ == '__main__':
    # Just hardcoded the coords as its not much
    # Test data : target area: x=20..30, y=-10..-5
    test_data = [20, 30, -10, -5]
    # Real data: target area: x=217..240, y=-126..-69
    data = [217, 240, -126, -69]

    # launchProbe(test_data)
    # launchProbe(data)

    print("\nTest Data\n")
    print("target area: x=20..30, y=-10..-5")
    max_y_coord, velocityPairCount = launchProbe(test_data)                         
    print("Part 1: maximum Y velocoty: %s" %( max_y_coord))                         #45
    print("Part 2: all posible velocity vallue count: %s" %(velocityPairCount))     # 112


    print("\nReal Data\n")
    print("target area: x=217..240, y=-126..-69")
    max_y_coord, velocityPairCount = launchProbe(data)
    print("Part 1: maximum Y velocoty: %s" %( max_y_coord))                         #7875
    print("Part 2: all posible velocity vallue count: %s" %(velocityPairCount))     #2321
