class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 2 common tells for any DP problem:
        # optimal substructure (the best overall solution is built from a combination of best smaller solutions)
        # recomputation / reuse of the same answers (repeated computation of the same subproblem)

        # 4 step guide to solving any DP Problem
        # 1. Visualise / Abstract
        # 2. Define the Subproblem
        # 3. Find the Recurrence Relation
        # 4. Implement

        # 1. Visualise/Abstract
        # we have a bag of distinct coin types and a total_amount we need to achieve by combining the coins in any configuration we like including several of the same coin type.
        # we need to return the number of distinct combinations to sum to total_amount.

        # 2. Define the Subproblem
        # What is changing every time we choose a coin? the total amount we now have, the number of coins we have selected, the breakdown of the type of each coin we have
        # C[n] contains the number of combinations that sum to amount n

        # 3. Find the Recurrence Relation
        # C[n+1] will be equal to sum(C[n+1 - c_i]) where c_i is all the coin types available. we evaluate each coin type and sum all the combinations. Consider C[1]. the number of combinations possible is the number of ways to make 0 plus the number of coins that equal 1 (1) therefore C[1] = C[0] + 1. Now C[2]. C[2] is the number of combinations that sum to all amounts up to 2 IFF there exists a coin which can take those amounts to current amount. ie if i have a coin of value 2 then C[2] += C[0] and if i also have a coin of value 1 then C[2] += C[1]. 

        # 4. Implement

        C = [0] * (amount+1) # index=amount, value=number of all unique coin combinations to get that amount
        C[0] = 1 # base case: number of ways to make 0 is 1 (using no coins)
        for c in coins: # loop through each coin
        # the number of ways to make an amount equal to the coin's value is at least 1 (using the coin itself)
            print(c)
            for i in range(c, amount+1): # coin c can only contribute to amounts ≥ c!
                if i == c:
                    C[i] += 1
                elif i > c:
                    C[i] += C[i-c]

            # print(C)
        return C[amount]
 
            