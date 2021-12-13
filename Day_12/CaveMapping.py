from collections import defaultdict


def getData(path):      #make a dictionary of steps from the input file
    data = defaultdict(list)
    for line in open(path):
        step_a, step_b = line.strip().split("-")
        data[step_a].append(step_b)
        data[step_b].append(step_a)
    return data

def getPaths(data, start, end, visited=None, may_visit_again=False):
    # print(start, end)
    if visited is None:                                                                         # Visited is none, cave isnt visited
        visited = set()                                                                         # make an empty set  

    if start==end:                                                                              # step 1 equels step 2, -> no path
        return 1

    pathCounter = 0                                                                             # set counter to 0
    for step in data[start]:                                                                    # loop trough data dict start (first step) values
        # print(step)
        new_may_visit_again = may_visit_again                                                   # set may visit to new value
        if step==step.lower() and step in visited:                                              # check conditions: check if the cave has been visited
            if may_visit_again or step in ['start','end']:                                      # if you may visit the cave again or the step is start or end
                continue
            else:
                new_may_visit_again = True                                                      # set to True to visit agian

        pathCounter += getPaths(data, step, end, visited | {start}, new_may_visit_again)        # recurse over function to get all paths
                                                                                                # the amount of calling function is counting paths
    return pathCounter          # after the loop is finisched return counter

if __name__ == "__main__":  
    test_data = getData("Day_12/test_data.txt")
    # print(test_data)
    data = getData("Day_12/data.txt")

    print("Part 1\n")
    # in part one we can visit big caves unlimeted amount of times
    print("Test data amount of paths: %s" %(getPaths(test_data, "start", "end", may_visit_again=True)))
    print("Real data amount of paths: %s" %(getPaths(data, "start", "end", may_visit_again=True)))

    print("\nPart2\n")
    # in part two we cannot visit end and start more than once
    print("Test data amount of paths: %s" %(getPaths(test_data, "start", "end")))
    print("Real data amount of paths: %s" %(getPaths(data, "start", "end")))


