class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2 tells to any DP problem:
        # 1. optimal substructure (the best overall problem is made from the results of the best smaller problems)
        # 2. memoisation (saving the results of smaller problems as these results are reused in solving the result of larger problems. This is to avoid recomputation)

        # 4 step DP strategy:
        # 1. Visualise/Abstract
        # 2. Define the Subproblem
        # 3. Find the Recurrence Relation
        # 4. Implement

        # 1. Visualise/Abstract
        # we are given an array of integers and a target value. We can add or subtract every number in the array in our attempt to achieve target. We need to find the total number of combinations of integers that sum to target.

        # 2. Define the Subproblem
        # Whats changing at each iteration? the current sum and the integer we are in therefore dp should be keyed by a (index, current_sum) tuple. we start with remaining_sum = target and define dp[(index, sum)] = number of ways we can make sum using all the integers in num up to index. We certainly need to loop through integers and employ a recursive function that takes that integer and goes down one branch of the search space where it is added and another branch where it is subtracted.

        # 3. Lets use the basic example nums = [1,2,3]. target = 5
        # we start with integer 1. we call dfs(1, add) and dfs (1, subtract). dfs in both cases will have a running sum according to the instruction given to it. it will have 1 in 'add' case and -1 in 'subtract' case. within each dfs call. there must then be a pointer advancement to the next integer where further dfs calls are made. we have n integers and m possible decisions at each node therefore search space is O(m**n)

        # 4. Implement
        dp = [defaultdict(int) for _ in range(len(nums)+1)] # key=(index, sum). value=number of ways you can combine all integers up to index+1 (indices in the dp dict are 1-indexed) to make sum
        dp[0][0] = 1 # the number of ways to make a sum of 0 with no integers is 1
        for i in range(len(nums)): # loop through all integers in nums
            for curr_sum, n_ways in dp[i].items(): # loop through all the sums possible using all integers up to index i
                dp[i+1][curr_sum + nums[i]] += n_ways # we have n_ways to make curr_sum with first i indices. so this gets carried over into the number of ways we can make curr_sum + nums[i] with the first i+1 indices. say we have 4 unique operation sequences of the first 5 integers that all combine to sum. these 4 get carried over to the number of ways we can make sum+nums[i] as we add the new integer nums[i] as the newest operation to each operation sequence.
                dp[i+1][curr_sum - nums[i]] += n_ways

        return dp[len(nums)][target]






