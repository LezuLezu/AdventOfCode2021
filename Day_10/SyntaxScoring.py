def getData(path):              #fetch and parse input
    with open(path) as file:
        data = file.read().splitlines()
        data = [[str(item) for item in line] for line in data]
    return data

# dicts for scores and bracket pairs
score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137, '(': 1, '[': 2, '{': 3, '<': 4}
allowedBrackets = {'(': ')', '[': ']', '<': '>', '{': '}'}


def getSyntaxErrors(data):
    # part 1
    errors = []                                                                     # empty list to keep track of error brackets
    brackets_stack = []                                                             # empty list to keep track of bracket stacks
    for line in data:                                                               # loop tru data list
        brackets = []                                                               # new empty list for brackets
        for item in line:                                                           # loop trough brackets in lines
            if item in allowedBrackets:                                             # check if the bracket is in allowedBrackets dict
                brackets.append(item)                                               # if so add it to stack list brackets
            else:
                if item != allowedBrackets[brackets[-1]]:                           # if not, check if item is not an closing bracket of the previous one
                    errors.append(item)                                             # if not ending bracket add to error list
                    break
                brackets.pop()                                                      # pop the previous bracket if the current is its ending bracket
        else:
            brackets_stack.append(brackets)                                         # add bracket list to stack list
    print("Part one error sum: %s" %(sum([score_dict[item] for item in errors])))   # print the sum of error brackets
    #part 2
    scores = []                                                                     # empty list for scores
    for brackStack in brackets_stack:                                               # loop trough brackets stack list
        score = 0                                                                   # set score to 0, score != scores !!
        for bracket in brackStack[::-1]:                                            # loop trough brackets in stack backwards
            score *= 5                                                              # multiplie score by 5
            score += score_dict[bracket]                                            # add score by points per bracket
        scores.append(score)                                                        # add score to scores list
    print("\nPart two middle score: %s\n" %(sorted(scores)[len(scores)//2]))        # find the middle score by sorting the list and deviding the lengt of the list by 2


if __name__ == "__main__":  
    test_data = getData("Day_10/test_data.txt")
    data = getData("Day_10/data.txt")
    # print(test_data)

    print("\nTest Data\n")
    getSyntaxErrors(test_data)

    print("\nReal Data\n")
    getSyntaxErrors(data)
