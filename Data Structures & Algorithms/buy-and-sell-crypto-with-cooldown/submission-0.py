class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 tells for DP Problems:
            # 1. some type of optimisation i.e. max/min or "best" way
            # 2. Taking the locally best option each iteration doesn't lead to best 
            #    overall solution i.e. 'greedy doesnt work'.
        
        # 2-step method for solving DP problems:
        # 1. define the sub-problem
        # 2. find the formula that connects larger problems to smaller subproblems (recurrence relation)


        # abstract the problem:
        # array of the price of Neetcoin over a few days.
        # we can own at most one Neetcoin at a time.
        # we can buy/sell Neetcoin as many times as we want provided we do NOT buy
        # neetcoin 0-1 days after we sell one.
        # find the maximum profit we can achieve


        # whats changing each iteration? money in the bank and day index.
        # for each path we explore through search space, we must always traverse the entire length of prices so dp[i] where i is day index or price index is futile.
        # everyday we can sell, we can buy only if we haven't sold the day before.

        # think of search space as a tree, day 1 is the first node it has a buy and a 'pass' branch then we go to 2nd node which is day 2 which, if a coin was bought on day 1 has a pass (and has buy otherwise) and a sell branch then each branch splits into 2 more at level 3 correpsonding to all possible actions we can take on day3.

        # navigating this tree to its leaves and taking the max of all leaf nodes is O(2**n) where n is the length of the prices array as there are 2 decisions we can make at each node (day).

        # we can use a DP technique called caching to reduce time complexity to O(n).
        # cache key = (i, boolean for buy/sell) where is i is index in prices array. there are n * 2 possible keys so space complexity is O(2n) = O(n).

        dp = {} # caching dict: key=(i, buy/sell boolean), val=maxprofit
        # if sell: boolean =0 and price index incremented by 2 due to cooldown day
        # if buy: boolean=1 and price index incremented normally ie by 1

        def dfs(i, buy_sell_boolean):
            if i >= len(prices): return 0
            if (i, buy_sell_boolean) in dp: return dp[(i, buy_sell_boolean)]

            if buy_sell_boolean: # we are buying or passing (cooldown)
                buy = dfs(i+1, not buy_sell_boolean) - prices[i]
                cooldown = dfs(i+1, buy_sell_boolean)
                dp[(i, buy_sell_boolean)] = max(buy, cooldown)
            else: # we are selling or passing (cooldown)
                sell = dfs(i+2, not buy_sell_boolean) + prices[i]
                cooldown = dfs(i+1, buy_sell_boolean)
                dp[(i, buy_sell_boolean)] = max(sell, cooldown)
            return dp[(i, buy_sell_boolean)]

        return dfs(0, True) # we start at day 0 and can only buy as we start with 0 coins
        


        




        