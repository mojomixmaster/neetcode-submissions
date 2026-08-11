class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_counts = dict() # key is int, value is count
        topk_frequent_ints = []
        n = len(nums)
        for num in nums:
            integer_counts[num] = integer_counts.get(num, 0) + 1
        
        # sorted_counts = sorted(integer_counts.items(), key=lambda kv_pair: kv_pair[1], reverse=True) # sort the items of dict
        # # based on value of the val in each key:val pair # we can avoid this costly full array sort as we only need to sort topk elements

        # bucket sort
        # for an array of N integers, i need N buckets
        buckets = [0] * (n+1) # index of bucket is the amount of time a specific int appears
        # extra bucket as we need a bucket for nums that had count of 0 and nums that had count of n (worst-case)
        for num, num_frequency in integer_counts.items():
            if not buckets[num_frequency]: # if falsy ie 0
                buckets[num_frequency] = [num]
            else:
                buckets[num_frequency].append(num)
        
        ints_left_to_add = k
        for i in range(n, -1, -1): # index j is in the j+1th bucket so index n is in n+1th bucket which is buckets[n] in python's 0-indexed system
            if not buckets[i]: # if bucket has no numbers, skip bucket
                continue
            else:
                for j in buckets[i]:
                    if ints_left_to_add > 0:
                        topk_frequent_ints.append(j)
                        ints_left_to_add -= 1

        # topk_frequent_numbers = [key for key,val in sorted_counts[:k]]
        
        return topk_frequent_ints
