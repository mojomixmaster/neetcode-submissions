class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i need an O(n^2) time and O(1) extra space solution
        # output should not contain any duplicates so output var is likely a set
        # if i sorted the array then i could easily do a 3 finger algo
        # if i fixed one finger and moved the other 2, then i create a 2Sum problem
        # recall in 2sum, we let the sign of the sum decide which pointer moves!
        # Invariant: The valid pair, if it still exists, lies somewhere between left and right.
        triplet_values_set = set()  # we want deduped VALUES not indices! # this can grow to O(N_answers) memory
        # we need an O(1) space solution. a set is dedupe-after-fact implementation.
        # we need a dedupe-during-construction mechanism
        triplets = []


        nums = sorted(nums)

        def compute_triplet(i, j, k): # lil helper func to bundle up repeated computation
                three_sum = nums[i] + nums[j] + nums[k]
                return three_sum

        for i in range(len(nums) - 2): # if our fixed pointer is at i, then 2 other fingers should be past i as the invariant is
        # all possible solutions with a fixed pointer of nums[0, ..., i-1] have been exhausted/fully considered
            if i > 0 and nums[i] == nums[i-1]: # prevents duplicate triplets being searched during runtime 
                continue
            fixed_pointer = nums[i]
            j = i + 1
            k = (len(nums)-1)

            while j < k:
                three_sum = compute_triplet(i,j,k)

                if three_sum == 0:
                    # if tuple([nums[i], nums[j], nums[k]]) not in triplet_values_set:
                        # triplet_values_set.add(tuple([nums[i], nums[j], nums[k]]))
                    triplets.append([nums[i], nums[j], nums[k]]) 
                    j += 1 # move both pointers inward
                    k -= 1
                    while j < len(nums)-2 and nums[j-1] == nums[j]:
                        j += 1 
                    while k > j and nums[k+1] == nums[k]:
                        k -= 1
        
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
            
        return triplets


                    



