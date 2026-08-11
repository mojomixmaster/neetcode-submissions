# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         valid_solns = []

#         def backtrack(candidate_soln, current_total):
#             for i in range(candidate_soln[-1] + 1, len(nums)):
#                 new_total = current_total + nums[i]

#                 if new_total == target_value and len(candidate_soln) == 1: # ensure candidate array can have at most 2 elements
#                     candidate_soln.append(i)
#                     valid_solns.append(candidate_soln)
#                     break
#             return
        
#         for i in range(len(nums)):
#             candidate_array = [] # undo previous choice
#             current_total = 0 # undo previous choice

#             root = nums[i] # explore new candidate
#             current_total += root
#             candidate_array.append(i.copy())

#             backtrack(candidate_array, current_total)

#         return valid_solns[0]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # algorithm design 101: 
        # question 1: what is the state? does it need to be candidate_soln, current_total, valid_solns
        # or can it just be a dict of what values have been seen and their index?
        # question 2: what decision am i making? for each number, have i already seen the number that pairs with this one?
        # question 3: what can i avoid recomputing? can i use hashmap?
        seen = dict()

        for i, val in enumerate(nums):         
            # now ask: what question do you need the hashmap to answer fast?
            # answer: for this new value, are there any indices already seen who had a value that i need to sum to target?
            needed_value = target - val
            needed_index = seen.get(needed_value, None)
            if needed_index is not None:
                return [needed_index, i]
            seen[val] = i


            



    
        
 



