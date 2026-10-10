class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # ok lets abstract the problem a bit here.
        # we have 2 strings, s and t.

        # we need the number of distinct subsequences of s which are equal to t

        # so importantly here we have a fixed target. it is always the entirety of t.
        # 2 tells of any dp problem: 1. the overall problem can be broken down into smaller subproblems
        # (optimal substructure) and 2. larger problems can be solved by combining the answers to smaller problems (overlapping
        # subproblems)

        # 1. abstract / visualise
        # so we need to create "cat". we cant with just "c". neither with "ca" need to keep moving our pointer until
        # the window is now "caaat". cat can now be made! is there another way we can make cat other than using s[0], s[1] and
        # s[4]. yes! we can use s[0], s[2] and s[4] and s[0], s[3], s[4].

        # 2. define the subproblem
        # what information must a solved smaller state (or eg the current state) contain so I can determine/define all the remaining
        # future (larger) subproblems? What value do i store for this state? and what larger states depend on this state?

        # recall in bottomupDP, ALL smaller subproblems must be solved first so we must respect a certain order in our solution.

        # notice how as we walk through s we can also walk through t. before we reach t, we can see that
        # "caaa" can create "ca" 3 times. we can add t to each subsequence to now create "cat" three times.
        # so if we define dp[i][j] as the number of subsequeneces in prefix s[:i] that create s[:j] then
        # once we find a letter in s that equals s[j] we can carry over that number of subsequeneces to our new state
        # as we can now create s[:j+1].

        # so our final answer is dp[len(s)][len(t)]
        # ultimately we need to walk through s and evaluate whether t is equal to it
        # if so then dp = 1
        # then walk again and see if it is equal to next letter
        # if so then we can carry forward our previous state's value
        # if not then dp remains 0
        # walk again, if next value is equal to next val then carry forward again
        # if next val in s is equal to previous val then we can increment our previous dp state by 1

        # 3. define the recurrence relation

        # dp[i][j] = the number of distinct subsequences within s[:i] that create t[:j]
        # dp[0][0] = 1 # there is 1 way to make an empty prefix equal an empty prefix

        # if s[i] == t[j] then dp[i][i] = 1
        # increment i, incremenent j.
        # if s[i] == t[i] then dp[i][i] =1
        # elif s[i] == s[i-1] then dp[i][i] = dp[i-1][i] + 1

        # 4. implement
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1 # base case. every prefix has a subsequence which is an empty array which can be used to create the empty array
        
        # fill our dp table starting with smallest subproblems first
        for i in range(1, len(s)+1): # i needs to eventually be the prefix that covers teh whole index which is s[:len(s)]
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]: # there are two groups of subseqs that are now eligible to make t[:j].
                
                # group1: all subseqs in s[:i-1] that could make t[:j] (carried over by default)
                # group1 is saying all the distinct subsequences within s[:i-1] that can make t[:j] can still absolutely make t[:j] when we now include one more char option from s to try make subsequences that match t[:j].

                # group2: all subseqs in s[:i-1] that could make t[:j-1].
                # group2 is the interesting case. it says that all distinct subsequences within s[:i-1] that can make t[:j-1] can now have s[i-1] added to them to create t[:j]!
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]


        return dp[len(s)][len(t)]

