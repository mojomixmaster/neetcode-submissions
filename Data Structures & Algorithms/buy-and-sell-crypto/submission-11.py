class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = max sell price - min buy price given buy price < sell price

        # for each price, see if there's prices after it that are lower, if not then skip that price
        # The main issue is that for every possible buy day, you recompute the best future sell price from scratch.
        # A more optimal approach tracks the minimum price seen so far while scanning once
        
        max_profit = 0
        
        left = 0 # buy price
        right = 1 # sell price
        while right < len(prices):
            
            max_profit = max(max_profit, prices[right] - prices[left])

            if prices[right] < prices[left]: # lower buy price. our finger at every iteration should always
            # point to lowest buy price seen so far
                left = right
            
            right += 1
                
        
        return max_profit


            

            

