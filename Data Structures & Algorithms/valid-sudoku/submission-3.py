class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = {} # keyed by row index
        column_set = {}
        is_valid = True

        for i in range(len(board)):
            col_index = 0
            row_set[i] = set() # initialise the row set as soon as event loop enters the row
            if not is_valid:
                break
            for j in board[i]: # loop through elements in row, each element's index represents the column index
                if i == 0:
                    column_set[col_index] = set() # initialise column set IFF event loop is still within 1st col else column_set gets rewritten everytime an element in that column is processed

                if j == ".":
                    col_index += 1
                    continue

                if j not in column_set[col_index] and j not in row_set[i]:
                    column_set[col_index].add(j)
                    row_set[i].add(j)
                else:
                    is_valid = False
                    break
                col_index += 1

        def threexthree_checker(board): # needs to be repeated 9 times, d for depth from top
            is_valid = True
            for d in range(0, 9, 3): # distance (depth) from top
                if not is_valid:
                    break
                for x in range(0, 9, 3): # distance from left
                    if not is_valid:
                        break
                    threexthree_set = set()
                    for row_step in range(3): # at each start point, we process the next 2 rows/cols as well
                        row = board[d+row_step]
                        for col_step in range(3):
                            if row[x+col_step] == ".": # looping through the column triplet in one row
                                continue
                            
                            if row[x+col_step] not in threexthree_set:
                                threexthree_set.add(row[x+col_step])
                            else:
                                is_valid = False
                                break
        
            return is_valid
        
        threexthrees_all_valid = threexthree_checker(board)

        combined_validation_flag = True if (threexthrees_all_valid is True and is_valid is True) else False

        return combined_validation_flag
                