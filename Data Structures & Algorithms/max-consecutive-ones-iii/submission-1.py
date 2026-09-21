class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 1. abstract / visualise the problem
        # we have a binary array (list of 0s and 1s) and we need to find the longest slice of this array
        # that contains at most k 0s.

        # this immediately appears to be a sliding window problem. We are scanning through the array,
        # constantly evaluating our window and contracting it when it violates our validity criteria

        # Sliding Window Recipe:
        # 1. establish condition for window invalidity
        # 2. process current item at r 
        # 3. expand window
        # 4. evaluate current window validity
        # 5. restore window validity if neccessary (decrementing l and processing l each time)
        # 6. process current valid window
        # 7. return to window expansion

        # Condition for Window Validity: the current window zeroesCount ≤ k.

        l, r = 0,0 # window is always exclusive of right index
        zeroesCount = 0
        maxLenConsecutiveOnes = 0
        while r < len(nums):
            if nums[r] == 0: # process item at r
                zeroesCount += 1
            r += 1 # expand current window to ensure item we just processed is now within it
            # print(r)

            while zeroesCount > k: # check if window is invalid. restore validity if neccessary
                # print(f"Invalid window at {l,r}")
                if nums[l] == 0:
                    zeroesCount -= 1
                l += 1
            
            maxLenConsecutiveOnes = max(maxLenConsecutiveOnes, r-l) # r-l is length of valid window as item at r is excluded.

        # edge cases?
        # what if we reach the end of the array and we haven't hit zeroesCount > k? The last element is already processed, no need for edge cases.

        return maxLenConsecutiveOnes