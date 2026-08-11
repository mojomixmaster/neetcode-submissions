class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        # for each idx_to_omit: multiply everything until it and with everything after it
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            if i == 1:
                prefix_product[i] *= nums[i-1]
                suffix_product[(len(nums)-1) - i] *= nums[(len(nums)-1)] # len(nums-1) is my '0-indexed' equivalent of counting from the back; index N-1 IS the last element where N = len(nums)
                
            else:
                prefix_product[i] = prefix_product[i-1] * nums[i-1]
                suffix_product[(len(nums)-1) - i] = suffix_product[(len(nums)-1) - i + 1] * nums[(len(nums)-1) - i + 1]
                
        for i in range(len(nums)):
            products[i] = prefix_product[i] * suffix_product[i]
            
        return products


