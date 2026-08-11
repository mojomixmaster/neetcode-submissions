class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is a binary search problem.
        # array is sorted in ascending order.
        # 2 pointers: outline the boundaries of the current search space

        # solution? we need to compare target with integer at midpoint of array.
        # If target > midpoint then we know target lies in 2nd half of array. else 1st half
        # repeat (each time dividing search space by 2) until target is located.
        # when r - l = 1 then target should equal midpoint if it is inside the array.

        # Invariant: at any point in the algorithm's execution, left and right pointers delineate
        # a legitimate domain of integers which target's value is within.

        # Per-step Rule: obtain midpoint of search space (l-r //2 ), extract value at that index and 
        # compare with target. if target > midpoint_value then target falls in right half of search space
        # increase l to index of midpoint. else: target falls in left half, decrease r to index of midpoint

        l = 0
        r = len(nums)-1 # keep pointers consistent units: 0-indexed indices

        while l < r: # r must be at least one more than l ie there is at least 2 numbers in search window (so midpoint can be found to make a search)
            midpoint_idx = l + ((r - l) // 2) # round down
            midpoint_value = nums[midpoint_idx]

            if target == midpoint_value: return midpoint_idx
            elif target > midpoint_value: # target is in 2nd half of arr ie arr[midpoint_idx:]
                l = midpoint_idx+1
            else: # target is in 1st half of arr ie arr[:midpoint_idx]
                r = midpoint_idx-1
        
        if target == nums[l]: return l # when r and l are the same then we are comparing target directly against one integer
        
        return -1


