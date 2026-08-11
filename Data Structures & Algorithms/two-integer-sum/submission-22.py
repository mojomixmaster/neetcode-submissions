class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid_solns = []
        target_value = target

        def backtrack(candidate_soln, current_total):
            for i in range(candidate_soln[-1] + 1, len(nums)):
                new_total = current_total + nums[i]

                if new_total == target_value and len(candidate_soln) < 2: # ensure candidate array can have at most 2 elements
                    candidate_soln.append(i)
                    valid_solns.append(candidate_soln)
                    break
            return
        
        while not valid_solns:
            for i in range(len(nums)):
                candidate_array = [] # undo previous choice
                current_total = 0 # undo previous choice

                root = nums[i] # explore new candidate
                current_total += root
                candidate_array.append(i)

                backtrack(candidate_array, current_total)

        return valid_solns[0]


