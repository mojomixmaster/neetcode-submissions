class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # What is the problem? 2D matrix of integers and a target. search through matrix
        # to see whether target exists within it.

        # Key Points: 
            # (1) each row in matrix in ascending order (could be duplicates tho)
            # (2) first integer of every row greater than last integer of previous row

        # Brute Force?
        # Loop through each row, for each element in that row check if element == target.
        # If True, return True immediately. This is O(n^2).

        # Can we Improve on this? YES! Binary Search!
        # Binary search neccessiates an initial window of ints, get the median int and compare it 
        # to target to know which side of the window the target (if in matrix) must fall into.

        m, n = len(matrix)-1, len(matrix[0])-1 # m rows, n columns in 0-indexed units

        # my initial idea is to loop through last element of each row to know which row we need to perform binary search in
        # this isn't scalable however. What if we did every 2^i rows where i is an int starting from 0 to N
        
        # on reflection, Galloping Search was the wrong implementation. It is ONLY when m is UNBOUNDED
        # right_edge_found = False # finger on the furthest (edge) row in window that target can be within
        # right_edge_idx, left_edge_idx = 0,0
        # i = 0
        # while right_edge_found is False: # we need our matrix window to be ONE ROW only
        #     current_row_idx = 2**i if 2**i <= m else m
        #     if target <= matrix[current_row_idx][n]: 
        #         right_edge_found = True
        #         right_edge_idx = current_row_idx
        #         left_edge_idx = int(2**(i-1))
        #     else: 
        #         if (2**i)<m: i += 1
        #         else: return False
        
        # we now know the rows window where target COULD be within, perform binary search within it to find the one ROW that target can be within!
        l, r = 0 , m
        while l < r:
            midpoint = l + ((r - l) //2) # midpoint rounds down so right_edge can never be midpoint but left_edge CAN
            if target == matrix[midpoint][n]: return True
            elif target < matrix[midpoint][n]:
                r = midpoint
            else:
                l = midpoint + 1 # target is greater than midpoint so we need to move window PAST midpoint to ensure the next midpoint isn't same index
        
        # we now know the ONE ROW where target COULD be within, perform binary search within it!
        window_l, window_r = 0 , n
        while window_l < window_r:
            midpoint = window_l + ((window_r - window_l) //2) # midpoint rounds down so right_edge can never be midpoint but left_edge CAN
            if target == matrix[l][midpoint]: return True
            elif target < matrix[l][midpoint]:
                window_r = midpoint
            else:
                window_l = midpoint + 1 # target is greater than midpoint so we need to move window PAST midpoint to ensure the next midpoint isn't same index

        if target == matrix[l][window_l]: return True # handle edge case where we have reached window of size 1 int

        return False
