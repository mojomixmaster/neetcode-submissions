class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = max sell price - min buy price given buy price < sell price

        # for each price, see if there's prices after it that are lower, if not then skip that price
        max_profit = 0
        for i in range(len(prices)-1):
            buy_price = prices[i]
            sell_price = max(prices[i+1:])

            if sell_price < buy_price:
                continue

            print(sell_price, buy_price)

            potential_profit = sell_price - buy_price

            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit


            

            

