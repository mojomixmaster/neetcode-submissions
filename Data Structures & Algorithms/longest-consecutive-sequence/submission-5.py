class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1) i could sort... but i need an O(n) time algorithm.. sorting is O(n * log(n))
        # 2) what operation do i need to make fast? given x... does x+1 or x-1 exist?
        # solution: i need fast lookups for this... lets do a set O(1) lookup
        # 3) if i start building sequences from every number, then i will redo a lot of work
        # solution: only start solution sequences from x when x-1 does NOT exist
        # 4) what is my invariant? I only expand from numbers with no direct predecessor
        # i.e. each number is only visisted as part of a chain only once
        longest_sequence = []
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])

        for num in nums_set: # if we did 'for num in nums', 
        # then for cases where elements that should appear later in a consecutive set
        # have an earlier index than elements that would appear in that set before them, 
        # then those larger elements are skipped e.g. [1, 3, 4 ,2] -> 3 and 4 are skipped from candidate_seq
            candidate_seq = []
            if num-1 not in nums_set:
                candidate_seq.append(num)
                for _ in range(len(nums)):
                    next_val = candidate_seq[-1] + 1 # you want to make sure you are walking NUMERICALLY, not by set element order

                    if next_val in nums_set:
                        candidate_seq.append(next_val)
                    else:
                        break

                if len(candidate_seq) > len(longest_sequence):
                    longest_sequence = candidate_seq

        return len(longest_sequence)