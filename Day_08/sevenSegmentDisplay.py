from collections import Counter

def getData(path):
    data =[]
    for line in open(path, "r"):
        items = line.strip().split("|")
        items = [item.strip().split(" ") for item in items]
        data.append(items)
    return data

def getOutputs(data):
    # just the count of total length of segments if lenght is 2,3,4 or 7
    count = 0
    count += sum([len([segment for segment in line[1] if len(segment) in [2,3,4,7]]) for line in data])
    return count 

def getPartTwo(data):
    total = 0
    for line in data:
        # print(line)
        joinedLineInput = "".join(line[0])
        counter = Counter(joinedLineInput)
            # Check if segments have certain lenghts, put them into their own list
        digitFour = [segment for segment in line[0] if len(segment) == 4][0]
        digitOne = [segment for segment in line[0] if len(segment) == 2][0]
        digitEight = [segment for segment in line[0] if len(segment) == 7][0]
            # Check if letters appear a certain ammount, put them into their own list
        echo = [letter for letter, count in counter.items() if count == 4][0]
        bravo = [letter for letter, count in counter.items() if count == 6][0]
        foxtrot = [letter for letter, count in counter.items() if count == 9][0]
        # find the lest common 
        alpha = Counter("".join([i for i in line[0] if len(i) in (2,3)])).most_common()[-1][0]
        delta = Counter("".join([digitFour, digitOne + bravo])).most_common()[-1][0]
        charlie = [letter for letter in digitFour if letter not in [bravo, delta,foxtrot]][0]
        golf = [letter for letter in digitEight if letter not in [alpha, bravo, charlie, delta, echo, foxtrot]][0]
            # nested set of apearing letters 
        alphabet = [
                [set(alpha + bravo + charlie + echo + foxtrot + golf), 0],
                [set(charlie + foxtrot), 1],
                [set(alpha + charlie + delta + echo + golf), 2],
                [set(alpha + charlie + delta + foxtrot + golf), 3],
                [set(bravo + charlie + delta + foxtrot), 4],
                [set(alpha + bravo + delta + foxtrot + golf), 5], 
                [set(alpha + bravo + delta + echo + foxtrot + golf), 6],
                [set(alpha + charlie + foxtrot), 7], 
                [set(alpha + bravo + charlie + delta + echo + foxtrot + golf), 8], 
                [set(alpha + bravo + charlie + delta + foxtrot + golf), 9]
                    ]
        # print(alphabet)
        # sum up the amounts of digits appearing in the output
        secondSegment = []
        for segment in line[1]:
            secondSegment.append(str([alp[1] for alp in alphabet if alp[0] == set(list(segment))][0]))
        total += int("".join(secondSegment))
    return total

if __name__ == "__main__":  
    test_data = getData("Day_08/test_data.txt")
    data = getData("Day_08/data.txt")
    # print(data)
    print("\nPart 1 \n")
    print("Test data: %s" %(getOutputs(test_data)))
    print("Real data : %s" %(getOutputs(data)))

    print("\nPart 2 \n")
    print("TestData: %s" %(getPartTwo(test_data)))
    print("Real Data: %s" %(getPartTwo(data)))

    print("\n")


