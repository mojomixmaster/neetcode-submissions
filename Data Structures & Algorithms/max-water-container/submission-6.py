class Solution:
    def maxArea(self, heights: List[int]) -> int:
      # so we need to choose the 2 bars to define the boundaries of a container
      # such that this container holds the MAXMIMUM amount of water that can possibly
      # be stored across all combinations of different bars as container boundaries

      # we need an O(n) time and O(1) space solution

      # the water height can never exceed the height of the MINIMUM of the container's edges
      # so we are trying to find the 2 numbers that can fit the greatest amount of numbers between them (width)
    
        def compute_area(edge_index_1, edge_index_2):
            area = min(heights[edge_index_1], heights[edge_index_2]) * (edge_index_2 - edge_index_1)
            return area

        # 2 finger algos provide an O(n) time way search through a structured subset of pairs

        i = 0 # finger 1
        j = (len(heights)-1) # finger 2

        best_area = compute_area(i, j) # start with best_area assigned to first trial case

        while i < j:
        # which edge is limiting the water height?
            if heights[i] < heights[j]:
                i += 1
                while i < j and heights[i] <= heights [i-1]:
                    i += 1
            else:
                j -= 1 # height of right bar is lower so decrement it 
                while i < j and heights[j] <= heights[j+1]: # firstly ensure we wont go out of bounds by ensuring the finger invariant is maintained
                # secondly we can skip bars with duplicate heights as this will certainly not improve water volume
                    j -= 1
            
            best_area = max(best_area, compute_area(i, j))

        return best_area




