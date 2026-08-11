class Solution:
    def trap(self, height: List[int]) -> int:
        # i need an O(n) time and O(n) space solution

        # Question 1: What is my unit of computation?
        # We could "find the puddles" but this is a messy boundary, variable shape region problem
        # Compute, for each column i, how high water stands on top of that one column
        # total water is then just sum over columns

        # Question 2: for single column i, what physically sets water height above height of column?
        # The minimum height of the bars adjacent to it

        # Question 3: How much water is actually trapped?
        # from above, its clearly min(adjacent_edges) - col_height

        # Question 4: Am i recomputing anything?
        # computing left_edge and right_edge for each col i is O(n) per col -> O(n^2). We can fix this
        # by noticing a hidden recurrence relation: left[i] is just left [i-1] extended by one element

        water_above_each_column = [0] * len(height) # initialise water_above_each_column that we will sum over to obtain final answer
         # first and last columns will never have water above them, so can skip their iterations
        highest_left_edge_index = 0

        highest_right_edges = [height[len(height)-1]] * (len(height))
        for j in range(len(height)-2, -1, -1): # last col has no right edge
            highest_right_edges[j] = max(height[j+1], highest_right_edges[j+1])
    
        
        for i in range(1, len(height)-1):
            if height[i-1] > height[highest_left_edge_index]:
                highest_left_edge_index = i-1
            
            if height[i] < height[highest_left_edge_index] and height[i] < highest_right_edges[i]: # for col i to hold water above it, it must have adjacent edges that are BOTH higher
                water_above_each_column[i] = min(height[highest_left_edge_index], highest_right_edges[i]) - height[i]

        
        total_water = 0
        for i in water_above_each_column:
            total_water += i

        return total_water



        


            

        
     



    