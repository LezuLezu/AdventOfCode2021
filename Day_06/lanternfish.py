from collections import defaultdict
def getData():
    with open("Day_06/data.txt", "r") as file:
        data = [int(age) for age in file.read().strip().split(",")]
    return data

def getLanterFish(data, days):
    # Age to count dictionary keeps track of the amount of fish on each "age" on the start
    # Ex: in the test data there are 2 fish on age 3, one fish on age 4, 2 and one. 
    age_to_count = defaultdict(int)
    for fish in data:
        age_to_count[fish] += 1
    # print(age_to_count)
    for day in range(days):
        fishAge = defaultdict(int)
        # Age to count dictionary keeps track of the amount of fish on each "age" during the days
        for age, count in age_to_count.items():
            if age > 0:
                # if the fish their age is greater then 0, reduce age/count by 1 and add it to the fishAge dict with their counter altered
                fishAge[age - 1] += count
            else:
                # Age is 0, the fish their age is reset to 6 and the new fish is set to 8 and added to the dict with their counter altered
                fishAge[6] += count
                fishAge[8] += count
            age_to_count = fishAge
            # daily count is set to main dict for next loop
    return sum(age_to_count.values())


if __name__ == "__main__":  
    Testdata = [3,4,3,1,2]
    print("\nTestInput amount of lanternfish after 18 days: %s\n" %(getLanterFish(Testdata, 18)))
    print("\nTestInput amount of lanternfish after 80 days: %s\n" %(getLanterFish(Testdata, 80)))
    data = getData()
    print("\nPart 1 amount of lanternfish after 80 days: %s\n" %(getLanterFish(data, 80)))
    print("\nPart 2 amount of lanternfish after 256 days: %s\n" %(getLanterFish(data, 256)))


    