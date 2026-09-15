class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2 tells for any DP Problem:
        # 1. optimal substructure (the problem can be solved optimally by breaking it down into subproblems and solving those subproblems)
        # 2. overlapping subproblems (answers to larger problems can be expressed in terms of smaller subproblems. recomputation of smaller subproblems is thus avoided.)

        # 4 step DP recipe
        # 1. abstract / visualise
        # 2. define the subproblem
        # 3. find the recurrence relation
        # 4. implement

        # 1. abstract/visualise
        # we have three strings: s1, s2 and s3. We need to see whether we can form s3 purely by interleaving s1 and s2. What does interleaving mean? It means s1 and s2 are decomposed into n and m substrings respectively and combined together into a single string in an alternating pattern.

        # for example. say we had s1 = "aa" and s2="bb", s3="abba". Can I form s3 by interleaving s1 and s2?If i split "aa" into two substrings ["a", "a"] and "bb" into one substring ["bb"] then the two can be interleaved so long as we start our combined string with a substring from s1.

        # we start on the string whose first letter matches the first letter of s3. for each successive letter, we check again if it matches the next letter in s3 and advance again if so.
        # if not, we then check if the next letter in s2 matches s3. if no match then it is not possible to interleave so the answer is false.

        # our task: figure out if its possible to interleave s1 and s2 to create s3/

        # 2. define the subproblem
        # as we advance through the algorithm, what is changing at each iteration? the number of characters from s1 and s2 that we have consumed. What state variables completely describe everything a future state needs? How many chars from s1 and s2 have been consumed and whether they interleave to create the substring of s3 that is as long as total number of chars consumed.

        # define dp[i][j] = boolean as "Can i create s3[:i+j] by interleaving s1[:i] and s2[:j]?"

        # 3. find the recurrence relation
        # lets go back to our simple example. the first char of s3 is "a" which is also the first char of s1. therefore dp[1][0] = True and we advance our finger on s1 to s1[1]. 
        # What are my choices from here? I can add another char from s1 if they match, if they don't match, I can try adding a char from s2. If no match again, then the state remains False.

        # In general: if dp[i][j]:
        # if s1[i] == s3[i+j]: dp[i+1][j] = True
        # elif s2[i] == s3[i+j]: dp[i][j+1] = True

        # are there any states where the answer is trivially known? yes! dp[0][0] = True as interleaving 2 empty strings always creates anohter empty string

        # 4. Implement
        if len(s1) + len(s2) != len(s3): return False # impossible to interleave as we do not have the correct total number of chars and all chars must be consumed.

        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)] # +1 to include empty strings
        dp[0][0] = True # base case
        print(dp)

        for i in range(len(s1)+1): # i is the pointer to the dp table's row.
            print(i)
            for j in range(len(s2)+1): # since dp's table is indexed by i and j, j must be able to 
            # traverse the entire length of the TABLE, not just the char. the table is one element
            # longer and wider as it includes the empty string!
                if dp[i][j]: # we can only progress from prior states that are true. 
                # for every true state, we can only progress either down one cell or right one cell i.e. consuming one more char from s1 or s2 respectively.
                    print(j)
                # for this, the last row of the DP table will be populated in the i=3 pass.
                    if i < len(s1) and s1[i] == s3[i+j]:
                        print(s1[i])
                        dp[i+1][j] = True
                    if j < len(s2) and s2[j] == s3[i+j]:
                        print(s2[j])
                        dp[i][j+1] = True
        
        print(dp)
        return dp[len(s1)][len(s2)]

  
