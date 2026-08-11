class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Step 1: Frame the Problem
            # heights[i] represents the height of a bar. each bar has width 1.
            # we are given array of integers called heights.
            # we need to find the rectangle we can form from the bars with MAXMIMUM area
            # conditions of the rectangle? Width is number of bars in the rectangle
            # height is min(heights of each bar in rectangle)

        # Step 2: Brute-force Approach?
            # loop through each bar in heights, for each bar calculate the maximum area of the rectangle
            # formed by merging with (up to) all bars ahead of it. nested for loop -> O(n^2) time

            # for each rectangle formed, append rectangle area to list of rectangle areas
            # and return max(rectangle_areas) at the end

            # Am i recomputing anything each iteration?
            # When ive done my first nested for loop, ive already seen the heights of all bars ahead of me
            # 


        # Step 3: What is my Invariant and Per-Step Rule?
            # 

            rectangle_areas = set()
            i=0
            while i < len(heights):
                bar_height = heights[i]
                print(bar_height)
                rectangle_area = bar_height * 1 # symbollically put here to show width of each bar is 1
                if i < (len(heights) -1): # ensure we are not on last bar of array
                    for j in range(i+1, len(heights)):
                        rectangle_height = min(bar_height, heights[j])
                        rectangle_area = max(rectangle_area, rectangle_height * ((j-i)+1))
                        rectangle_areas.add(rectangle_area)
                        
                        bar_height = min(bar_height, rectangle_height)
                else: # we're on the last bar, so append its area (which is just its height)
                    rectangle_areas.add(bar_height)
                i += 1
            
            return max(rectangle_areas)
