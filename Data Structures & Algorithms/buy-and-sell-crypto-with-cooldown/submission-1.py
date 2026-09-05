class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # There are 2 tells for any DP Problem:
        # 1. greedy doesn't work. the best overall solution is built from the best smaller solutions (optimal substructure)
        # 2. there are multiple computations of the same problem and results are reused. (overlapping subproblems)


        # quick guide to solving DP problems:
        # 1. visualise/abstract the problem
        # 2. define the subproblem
        # 3. find the recurrence relation
        # 4. implement

        #1. Visualising the problem:
        # we have an integer array of prices of Neetcoin where the ith item corresponds to the price of Neetcoin on day i. we start with 0 neetcoin.
        # we can buy and sell neetcoin as many times as we want. we can sell neetcoin on any day yet we can only buy neetcoin given that we have not sold any the day before (1 day cooldown).
        # we can only own one neetcoin at a time

        # lets think of a tree where each node corresponds to a certain day. node 1 is day 1. we have two choices. we can buy or skip (as we do not have any coin we cannot sell).
        # these two choices are branches to nodes on level 2 which correspond to choices we can make on day 2. if we bought the day before, we can sell. if we skipped the day before, we can buy.
        # we can also skip (do nothing)
        # this continues on until we get to all the nodes on day len(prices). The max profit obtainable is the path from root to leaf with the greatest total branch weight. branch weight is determined by how much money was made on the node (day) that it originates from.

        # 2. Define the subproblem:
        # what is changing every day? the day index, the total amount of profit we have made and whether we can buy a coin on that day or not.
        # this is looking like a 2D dp problem where we define dp[(i,j)] = the max profit achievable from day i onwards given whether we CAN buy on that day i.e. j is a boolean flag for allowed_to_buy.

        # 3. Find the Recurrence Relation 
        # say we are on day 3. what is our maximum profit? well, it is the maximum profit achievable on day 2 + the profit we can make if we have a coin to sell on day 3. There will need to be some type of recursive function as on any day we can certainly skip, and do one of buy or sell. Recursion will be needed here to exhaust the search space.

        # 4. Implement
        dp = {} # key=(day index, allowed_to_buy), value=max_profit_achievable_from_that_day
        def traverse_tree(i, allowed_to_buy):
            if i >= len(prices): return 0
            if (i, allowed_to_buy) in dp: return dp[(i, allowed_to_buy)] # enable memoisation (use cache to get answer to previously computed subproblems to avoid recomputation)
            if allowed_to_buy:
                dp[(i, True)] = max(traverse_tree(i+1, True), traverse_tree(i+1, False) - prices[i]) # the maximum profit between skipping on day 1 or buying on day1
            else:
                dp[(i, False)] = max(traverse_tree(i+2, True) + prices[i], traverse_tree(i+1, False)) # i either must sell today, or skip today and sell tomorrow
            
            return dp[(i, allowed_to_buy)]

        
        return traverse_tree(0, True)



       


     


        




        