import re
from collections import defaultdict
def getData():
    # put data from txt file (data coppied from web input) into a list
    data = []
    for line in open('Day_5/data.txt', 'r'):
        items = line.rstrip()
        items = re.split("\n | ->", items)      
        items = [item.strip().split(",") for item in items]       
        data.append(items)
    # print(data)
    return data

def getFogOverlap(data):
    grid = defaultdict(int)     # Default dict to use as grid
    for line in data:
        (x1, y1), (x2, y2) = line[0], line[1]       # set coords to xy from datalist
        #convert to ints (smh..)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2) 
        # print(x1, y1)
        if (x1 == x2):      #check if x's are equal 
            y1, y2 = min(y1, y2), max(y1, y2)       #get both ends of length of the fog
            for yAxis in range(y1, y2+1):
                grid[(x1, yAxis)] += 1      # add lenght to dict
        if(y1 == y2):       #check if y's are equal
            x1, x2 = min(x1, x2), max(x1, x2)   #get both ends of length of the fog
            for xAxis in range(x1, x2+1):
                grid[(xAxis, y1)] += 1    # add lenght to dict
    overlap = 0
    for y in grid.values():     #loop trough the dict grid
        if y > 1:       # if y is greater then on one y theres an overlap
            overlap += 1
    return overlap

def getFogOverlapDiag(data):
    grid = defaultdict(int)     # Default dict to use as grid
    for line in data:
        (x1, y1), (x2, y2) = line[0], line[1]       # set coords to xy from datalist
        #convert to ints (smh..)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)  
        # print(x1, y1)
        if (x1 == x2):      #check if x's are equal 
            y1, y2 = min(y1, y2), max(y1, y2)       #get both ends of length of the fog
            for y in range(y1, y2+1):
                grid[(x1, y)] += 1      # add lenght to dict
        elif (y1 == y2):        #check if y's are equal
            x1, x2 = min(x1, x2), max(x1, x2)       #get both ends of length of the fog
            for x in range(x1, x2+1):
                grid[(x, y1)] += 1      # add lenght to dict
        else:       #Diagnal Fog!
            x1_dia, x2_dia = min(x1, x2), max(x1, x2)       #get both ends of length of the fog
            y1_dia, y2_dia = min(y1, y2), max(y1, y2)       #get both ends of length of the fog
            diaRange = (x2_dia - x1_dia) + 1        #find the horizontal lenght 
            if (x1 < x2) and (y1 < y2):         # second coords are smaller than first 
                for diagnal in range(diaRange):
                    grid[(x1_dia + diagnal, y1_dia + diagnal)] += 1     #add lenght diagnal to dict
            elif (x1 > x2) and (y1 < y2):       # x2 is greater than x1, y2 is smaller than y1 
                for diagnal in range(diaRange):
                    grid[(x2_dia - diagnal, y1_dia + diagnal)] += 1     #add lenght diagnal to dict
            elif (x1 < x2) and (y1 > y2):       # x2 is smaller than x1, y2 is greater then y1
                for diagnal in range(diaRange):
                    grid[(x1_dia + diagnal, y2_dia - diagnal)] += 1     #add lenght diagnal to dict
            else:                               #both second coords are greater then first
                for diagnal in range(diaRange):     
                    grid[(x2_dia - diagnal, y2_dia - diagnal)] += 1     #add lenght diagnal to dict
    overlap = 0
    for y in grid.values():     #loop trough the dict grid
        if y > 1:       # if y is greater then on one y theres an overlap
            overlap += 1
    return overlap

if __name__ == "__main__":  
    data = getData()
    print("Fogs overlapping: %s"%(getFogOverlap(data)))
    print("Fogs overlapping with Diagnal: %s"%(getFogOverlapDiag(data)))
