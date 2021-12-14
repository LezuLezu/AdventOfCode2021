
from collections import defaultdict

def getData(path):          # fetch and parse data into dict, and baseLine
    data = {}
    with open(path) as file:
        for line in file:
            line = line.strip()
            if "->" in line:
                base_a, base_b = line.split(" -> ")
                data[base_a] = base_b
            elif line:
                baseLine = line
    return baseLine, data

def getPolymer(template, data, run):
    polymer = defaultdict(int)                   # make dictionary for template base polymer
    for i in range(len(template) - 1):           # loop trough base polymer
       polymer[template[i : i+2]] += 1           # insert bas pairs from base polymer into dict
    polymer[template[-1]] += 1                   # insert bases from base polymer into dict
    # print(polymer)                 

    for step in range(run):                                     # loop the given amount of steps
        tempPolymer = defaultdict(int)                          # new temporary dict for polymer amounts
        for base, amount in polymer.items():                    # loop trough existing polymer dict
            if base in data:                                    # check if the base is in data (base dict)
                tempPolymer[base[0] + data[base]] += amount     # add base pair to dict with addint amount of appearence
                tempPolymer[data[base] + base[1]] += amount     # add base pair to dict with addint amount of appearence
            else:
                tempPolymer[base] += amount                     # base not in data: add the base with the amount of appearence
        polymer = tempPolymer                                   # temporary dict becomes polymer dict
    # print(polymer)

    freq_base_dict = defaultdict(int)                                                   # new dictionary to keep track of appearences of bases
    for base, amount in polymer.items():                                                # loop trough polymer dict
        freq_base_dict[base[0]] += amount                                               # add the base to the frequencie dict with corresponding value
    max_base_key = max(freq_base_dict.keys(), key=(lambda k: freq_base_dict[k]))        # find the base with the least appearences
    min_base_key = min(freq_base_dict.keys(), key=(lambda k: freq_base_dict[k]))        # find the base with the most appearences
    answer = (freq_base_dict.get(max_base_key)) - (freq_base_dict.get(min_base_key))    # calculate the answer by substracing the amount of least appearing base from most appearing base
    return answer                                                                       # return the answer


if __name__ == "__main__":
    test_template, test_data = getData("Day_14/test_data.txt")
    template, data = getData("Day_14/data.txt")

    print("\nPart one\n")
    print("Test data: %s" %(getPolymer(test_template, test_data, 10)))
    print("Real data: %s" %(getPolymer(template, data, 10)))

    print("\nPart two\n")
    print("Test data: %s" %(getPolymer(test_template, test_data, 40)))
    print("Real data: %s\n" %(getPolymer(template, data, 40)))