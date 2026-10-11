class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # lets abstract the problem a bit here
        # we are trying to perform the minimum number of edit operations TO word1 ONLY to make it equal word2

        # an edit operation can be one of : 1. insert, 2. delete or 3. replace

        # lets try look for some optimal substructure here (1st tell of dp)
        # example word1 = "monkeys", word2 = "money"

        # lets walk through word1 and word2, with one pointer for each.
        # m=m, great no edits needed to transform word1[:1] to word2[:2]
        # same with o and n
        # now k != n! what can we do from here! ie how do we edit "monk" to become "mone"?
        # lets first consider an insert operation.
        # this entails converting the current prefix of word1 to prev smaller prefix of word2 then inserting the current letter of word2
        # dp[i][j] = dp[i][j-1] + 1

        # lets now consider a delete operation.
        # this entails converting the prev smaller prefix of word1 to current word2 and deleting current letter of word2
        # dp[i][j] = dp[i-1][j] + 1

        # lets now consider a replace operation
        # this entails converting prev smaller prefix of word1 to prev smaller prefix of word2 and replacing current char in word1 with current char in word2. since char from both strings consumed: dp[i][j] = dp[i-1][j-1] + 1

        # 2. Define the subproblem: 
        # what information must a smaller subproblem preserve so that all remaining future larger subproblems can be defined / determined? we need to know where we are at currently in word1 and where we are currently at in word2. From here, the choice for any state is the same going forward as we have ensured the current prefix of word1 has been edited to match word2.
        # so we need to store pointers i and j. note this is NOT an 0/1 knapsack problem as we have to consuem each letter of word1 as we are trying to edit the entire word to become word2 so every char needs processing.

        # dp[i][j] = the minimum number of edit operations to convert word1[:i] to word2[:j]. Can i collapse histories that take the current prefix of word1 and lead to the same prefix of word2 into the same state? yes! we only care about propagating the MINIMUM edit distance forward, so we can aggregate state historeis and take the minimum edit distnace

        # 3. Define the recurrence relation
        # dp[i][j] = dp[i-1][j-1] if i == j
        # else dp[i][j] = 1 + min(insert, edit, replace)

        # 4. implement
        
        dp = [[float('inf')]*(len(word2)+1) for _ in range(len(word1)+1)]
        dp[0][0] = 0 # base case
        for i in range(len(word1)+1):
            dp[i][0] = i # base case. just delete all letters to match empty str
        for j in range(len(word2)+1):
            dp[0][j] = j # base case. just add all letters of word2 to word1's empty str to make strs match
        
        # solve smaller subproblems first
        for i in range(1, len(word1)+1): # i and j are INDICES into DP TABLE. to use i and j as indices into the strings, subtract each by 1 to obtain the char at the actual position you want.
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1], # insert
                        dp[i-1][j], # delete
                        dp[i-1][j-1] # replace
                    )

        return dp[len(word1)][len(word2)]

