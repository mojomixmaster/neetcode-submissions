class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_counts = dict() # key is int, value is count
        for num in nums:
            if num not in integer_counts:
                integer_counts[num] = 1
            else:
                integer_counts[num] += 1
        print(integer_counts)
        
        sorted_counts = sorted(integer_counts.items(), key=lambda kv_pair: kv_pair[1], reverse=True) # sort the items of dict
        # based on value of the val in each key:val pair
        print(sorted_counts)

        topk_frequent_numbers = [key for key,val in sorted_counts[:k]]
        
        return topk_frequent_numbers
