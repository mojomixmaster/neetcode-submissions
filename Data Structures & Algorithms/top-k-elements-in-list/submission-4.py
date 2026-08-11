class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_counts = dict() # key is int, value is count
        for num in nums:
            integer_counts[num] = integer_counts.get(num, 0) + 1
        
        sorted_counts = sorted(integer_counts.items(), key=lambda kv_pair: kv_pair[1], reverse=True) # sort the items of dict
        # based on value of the val in each key:val pair

        topk_frequent_numbers = [key for key,val in sorted_counts[:k]]
        
        return topk_frequent_numbers
