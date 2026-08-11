class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ok we have a window of FIXED length that slides across the string
        # everytime it slides, we need to find the maximum value in that window
        # and append that to a string containing the maximum values at each step
        # of the algo

        # what am i computing at each step?
        # for each group of 3 ints, compute the max

        # can i keep the current group im on as a slice of the current index
        # slices of python (not numpy) arrays are copies of the nums list so dont overwrite anything, just change the indices that we're slicing
        # this method was correct but didnt scale - hit TLE errors on test cases
        # we need to realise that when we slide a window we dont need to reconsider any vals in that window smaller than our current max. 
        # What if that current max was the left edge of the previous window (now discarded)? we need second largest number...
        # we need to implemet a Monotonically Decreasing Queu

        from collections import deque
        l = r = 0
        max_val_at_each_step = []
        q = deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # the deque cannot have smaller vals than the val (represented by its index in nums) we are about to append (the deque's invariant)
                q.pop()
            q.append(r)

            if r-l+1 == k: # r has moved along enough such that the window is now valid i.e. contains k numbers
                max_val_at_each_step.append(nums[q[0]])
                if l == q[0]: # left window edge is currently pointing to the max val in the window. we are about to slide window thus this val will fall out of range -> pop from queue
                    q.popleft()
                l += 1

            r += 1
        
        return max_val_at_each_step