class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing means increasing BUT there may be duplicate terms

        # i need a solution that is O(n) with O(1) additional space
        # invariant (i.e. what stays true while searching):
        # the valid answer, if not found yet, is between window [left:right]

        # 2 finger algorithm looks good for this

        i = 0 # finger 1
        j = len(numbers) - 1 # finger 2

        # if sum too small, increase smallest, vice versa for sum too large

        while i < j:
            if numbers[i] + numbers[j] == target:
                correct_pair_indices = [i+1, j+1]
                return correct_pair_indices
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1 # sum too large so lets add a smaller int

