class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        duplicate_flag = False
        for i in nums:
            if i in vals:
                duplicate_flag = True
                return duplicate_flag
            vals.add(i)
        
        return duplicate_flag