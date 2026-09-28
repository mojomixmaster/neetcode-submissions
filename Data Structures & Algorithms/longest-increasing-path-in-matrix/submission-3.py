class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 2 tells for any DP Problem:
        # 1. optimal substructure
        # 2. overlapping subproblems

        # abstract / visualise
        # we have a 2D matrix of non-negative integers.
        # return the length of the longest strictly increasing path within the matrix

        # on a path walk, one can either move horizontally or vertically.
        # you cannot move diagonally.

        # say we start at 5, we can move right or down. none of which give us a value > 5. Ok lets start top right at 3. we can move down. from 6 we can move down or left
        # none of which are > 6 so its [3,6 ].

        # what information must a solved smaller state contain so that I can use it to build larger states?

        # for each matrix value, the longest increasing path that ends at that cell value.

        # from there. you can try go up, go down, go right, go left and see where the path can legimately increase

        # find the recurrence relation
        # dp[i][j] = longest increasing path that ends at cell (i,j)
        # need to go up down right left and see if any number is less than it,
        # if it is, find its LIP value and then add one to it. take the max of all these values and assign it to dp[i][j].

        dp = [[1]*len(matrix[0]) for _ in range(len(matrix))] # same index system as matrix
        longestIncPath = 0
        # I must solve the smallest subproblems first,
        # this means i need to evaluate paths from the smallest values in the matrix first     
        cells = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cells.append((matrix[i][j], i , j))
        # print(cells)
        
        sortedCells = sorted(cells, key=lambda x: x[0]) # ascending=True by default
        # print(sortedCells)

        for _, i, j in sortedCells:
            currVal = matrix[i][j]
            # print(currVal)
            # when we are at last row, we can only go left or up to see if we can extend their paths to current index.
            longestPathSteps = 0 # at any general point, I can go left, right, down or up
            # Choice 1: Can I go left?
            if j > 0:
                longestPathSteps = max(
                    longestPathSteps,
                    dp[i][j-1] if matrix[i][j-1] < currVal else 0
                )
            # Choice 2: Can I go right?
            if j < len(matrix[0])-1:
                longestPathSteps = max(
                    longestPathSteps,
                    dp[i][j+1] if matrix[i][j+1] < currVal else 0
                )
            # Choice 3: Can I go up?
            if i > 0:
                longestPathSteps = max(
                    longestPathSteps,
                    dp[i-1][j] if matrix[i-1][j] < currVal else 0
                )
            # Choice 4: Can i go down?
            if i < len(matrix)-1:
                longestPathSteps = max(
                    longestPathSteps,
                    dp[i+1][j] if matrix[i+1][j] < currVal else 0
                )
            # print(f"longest path for {i}{j} is {longestPathSteps}")
            dp[i][j] += longestPathSteps
            longestIncPath = max(longestIncPath, dp[i][j])

        return longestIncPath


