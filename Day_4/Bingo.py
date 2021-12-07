import numpy as np
def getData():      #read file and format data
    data = [x for x in open('Day_4/data.txt', 'r').read().strip().split('\n')]
    numbers = [int(x) for x in data[0].split(",")]
    boards = [[y.split() for y in line.split("\n")] for line in open('Day_4/data.txt', 'r').read().strip().split('\n\n')][1:]
    boards = [[[int(x) for x in row] for row in board] for board in boards]
    return numbers, boards

test_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
test_boards = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],[
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17,  5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],[
        [14, 21, 17, 24, 4],
        [10, 16 ,15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
]

def checkWin(board, number):
    row_sum = board.sum(axis=1)                                 # make sum of rows in board
    col_sum = board.sum(axis=0)                                 # make sum of collumns in board
    # print(row_sum)
    # print(col_sum)
    if np.any(row_sum == 1000) or np.any(col_sum == 1000):      # check if sum is 1000 (5 times 200)
        # print(board)
        # print("nummer: %s" %(numbers[index]))
        # print(board[np.where(board != 200)])
        boardSum = np.sum(board[np.where(board != 200)])        # calculate board sum
        # print("sum: %s" %(boardSum))
        total = boardSum * number                               # calculte score
        # print(total)
        return True, total                                      # return score
    else:
        return False, 0

def findFirstWinningBoard(numbers, boards):
    boards = np.array(boards)                                   # make numpy array of the boards
    for index in range(len(numbers)):                           # loop trough numbers list
        boards= np.where(boards == numbers[index], 200, boards) # change index to 200 if number is called
        # print(boards)
        for board in boards:                                    # loop trough bords
            # print(board)
            # print(numbers[index])
            win, score = checkWin(board, numbers[index])        # check for win, and get score
            if win:                                             # win is True
                return score                                    # return the score
            
def findLastWinningBoard(numbers, boards):
    boards = np.array(boards)                                   # make numpy array of the boards
    lastBoardScore = None
    del_board_index = []
    for index in range(len(numbers)):                           # loop trough numbers list
        boards= np.where(boards == numbers[index], 200, boards) # change index to 200 if number is called
        # print(boards)
        for b_id in range(len(boards)):                         # loop trough bords
            # print(board)
            # print(numbers[index])
            win, score = checkWin(boards[b_id], numbers[index]) # check for win, and get score
            if win:     #win is True
                del_board_index.append(b_id)                    # save board index of winning board
                lastBoardScore = score                          # save score of most recent winning board
        if len(del_board_index) != 0:                           # delete index is not None
            boards = np.delete(boards, del_board_index, axis=0) # delete board from boards
            del_board_index = []                                # reset del_index to None
            # print(len(boards))
        # print(win, lastBoardScore)
    return lastBoardScore                                       # return last score winningbord 

if __name__ == "__main__": 
    numbers, boards = getData()
    print("\nTest data\n")
    print("Test data part 1: first winning board score: %s" %(findFirstWinningBoard(test_numbers, test_boards))) 
    print("Test data part 2: last winning board score: %s" %(findLastWinningBoard(test_numbers, test_boards)))

    print("\n\nInput data \n")
    print("Test data part 1: first winning board score: %s" %(findFirstWinningBoard(numbers, boards)))
    print("Test data part 2: last winning board score: %s" %(findLastWinningBoard(numbers, boards)))
    print('\n')
 