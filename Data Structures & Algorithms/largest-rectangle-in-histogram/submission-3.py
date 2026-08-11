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

        # Step 3: What is my Invariant and Per-Step Rule?
            # Invariant: we maintain a stack of seen_bar_heights = []. at any point in algorithm's iteration, 
            # the stack holds the heights of rectangles that can be extended from their starting index (in heights) all the way to current index (in heights)

            # Per-Step Rule: Loop through heights. For each bar, push its index and height to stack.
            # Go to next bar, check if stack not empty then perform comparison. if stack[-1][h] (height of rectangle on stack) is smaller then current rectangle, then rectangle on stack CAN be extended,
            # push current rectangle with its own (index, height) pair as its own rectangle may also be extendable.

            # if stack[-1][h] > current_height then rectangle on stack NOT extendable. compute area of it then POP. push current rectangle as normal.

            maxArea = 0
            stack = [] # pair: (index, height)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h: # rectangle on stack's height is greater than height we just reached therefore not extendable
                    area = stack[-1][1] * (i - (stack[-1][0]))
                    print(area)
                    maxArea = max(maxArea, area)
                    start = stack[-1][0]
                    stack.pop() # start of current rectangle must now absorb bar that is about to be pop'ds index

                # stack[-1][1] now < h therefore this rectangle is extendable and push current rectangle too
                stack.append([start, h])
            
            for rect in stack:
                print(rect)
                area = rect[1] * (len(heights) - rect[0])
                maxArea = max(area, maxArea)
            
            return maxArea



            # rectangle_areas = set()
            # i=0
            # while i < len(heights):
            #     bar_height = heights[i]
            #     print(bar_height)
            #     rectangle_area = bar_height * 1 # symbollically put here to show width of each bar is 1
            #     if i < (len(heights)-1): # ensure we are not on last bar of array
            #         for j in range(i+1, len(heights)):
            #             rectangle_height = min(bar_height, heights[j])
            #             rectangle_area = max(rectangle_area, rectangle_height * ((j-i)+1))
            #             rectangle_areas.add(rectangle_area)
                        
            #             bar_height = min(bar_height, rectangle_height)
            #     else: # we're on the last bar, so append its area (which is just its height)
            #         rectangle_areas.add(bar_height)
            #     i += 1
            
            # return max(rectangle_areas)
