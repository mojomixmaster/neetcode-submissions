class Solution:
    def findMin(self, nums: List[int]) -> int:
        # abstract the problem:
        # we have an array of n numbers originally sorted in ascending order
        # the array was rotated between 1 and n times.
        # each rotation = the last element of array moves to front 
        # we need to find the minimum element in the array
        # WITHOUT doing a for loop to scan all elements.

        # all numbers in array are UNIQUE

        # naive solution is loop through each element and assess whether
        # arr[i] < current_min_val_seen. assign current_min_val_seen to arr[i] if so.
        # then return current_min_val_seen.

        # This is O(n) time ... is there a faster approach?
        # if i have an array of say len(3) and nums = [3 ,2 ,1]
        # the array was originally in ascending order therefore arr[i-1]
        # was always < arr[i]
        # if i could find a way to know how many rotations were performed,
        # i could go simply extract the min value immediately.

        # well there is a way: it is keep iterating through array until you find the
        # position, i, where arr[i] > arr[i+1]. arr[i+1] was the first element originally and
        # thus the minimum value.

        # theres only ONE value in the array that is less than its previous value and that value is the min value.
        # if no value satisifes this then the min value is the first value (has nothing behind it) and no rotations have been performed.

        # we can do a guided binary search: start with l on 1st number and r on the last. 
        # if arr[r] < arr[l] and arr[midpoint] > arr[l] then we know that nums increases at least from 1st value to midpoint and
        # the min value lies thus between midpoint and r

        # else arr[l] is smaller than r so we know the value lies between l and midpoint
        # nums = [3, 2, 1]
 
        l = 0
        r = len(nums)-1

        while l < r:
            if r - l > 1:
                midpoint = l + (r-l)//2 # we need to find the position where nums drops.
                print(midpoint)
                if nums[l] > nums[midpoint]: # we know for sure the drop has happened between l and midpoint
                    # min_val = min(min_val, arr[midpoint])
                    r = midpoint
                # we now know for sure the drop happens either (1) the first number or (2) between midpoint and r
                elif nums[l] < nums[midpoint] and nums[midpoint] > nums[r]: # the drop must happen between midpoint and r as r would otherwise be greater than midpoint
                    l = midpoint + 1 # midpoint is NOT the min as we've just ascertained that nums[l] is smaller than it -> discard from window
                    print(l, r)
                else: return nums[l] # min val is the first element because nums[l] is < nums[midpoint] and nums[midpoint] < nums[r] therefore entire array sorted in ascending order so 1st val is smallest 
            else:
                return min(nums[l], nums[r])

        return nums[l]