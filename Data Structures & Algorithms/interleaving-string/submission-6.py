class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2 tells for any DP Problem:
        # 1. optimal substructure (the overall solution to a problem can be expressed using answers to smaller instances of the same problem)
        # 2. memoisation (answers to smaller subproblems are saved and resued in computing the answers to larger problems. recomputation is thus avoided.)

        # 4 step DP recipe
        # 1. abstract / visualise
        # 2. define the subproblem
        # 3. find the recurrence relation
        # 4. implement


        # 1. abstract/visualise
        # we have three strings. we are trying to find whether s3 is the result of 'interleaving' chopped up versions of s1 and s2 together. Interleaving means to divide s1 and s2 into n and m substrings respectively and combining them in alternating order into one final string. 
        
        # This can be done one of two ways: the combined string starts with a substring from s1 or a substring from s2 from which the following components to the string follow an alternating origin pattern.

        # lets do a simple example:
        # s3 = abab
        # s1 = aa, s2 = bb
        # we divide s1 and s2 into 2 substrings each such that n=m=2
        # create all candidate 'formed' strings and check if any of those strings matches s3.
        # this is done by looping through the longer set of substrings (either in this case), and creating a candidate string from index[i] of that set then index[i] of the other set and then advancing i until i is out of range for length of that set of substrings.

        # 2. define the subproblem
        # what is changing at each iteration? how many letters from s1 and s2 I've consumed and how many characters of s3 I've currently matched. dp[i][j] = whether s1[:i] and s2[:j] can interleave to form s3[:i+j]. the formed substring candidates are therefore i+j chars long.

        # 3. find the recurrence relation
        # take s1 = aaa, s2=bbb, s3= ababab
        # if dp[1][1] = True (as 'ab' == s3[:3]). Where can I go from here?
        # I need to match chars in s3 from s3[2:] . that is 'abab'. 
        # I can loop through s1 and keep advancing the pointer until what is in s1 no longer matches with the remaining string. I can also loop through s2 and try out the same
        # 4. Implement
        if len(s1) + len(s2) != len(s3): return False # we cannot create s3 from a complete interleave of s1 and s2

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)] # col x row
        dp[0][0] = True # base case: interleaving 2 empty strings into one empty string is possible.
        # print(dp)
        # what do i need to loop over to fill out my table? the dp states themselves
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i+j == len(s3): break
                # we want to match s3[i+j] = s3[0]
                if dp[i][j]: # i have succesfully formed s3[:i+j] from s1[:i] and s2[:j]
                # can i take the next letter from s1? ie does s1[i] match s3[i+j]?
                    if i < len(s1):
                        if s1[i] == s3[i+j]: dp[i+1][j] = True
                # can i take the next letter from s2? ie does s2[i] match s3[i+j]?
                    if j < len(s2):
                        if s2[j] == s3[i+j]: dp[i][j+1] = True

        
        # print(dp)
        return dp[len(s1)][len(s2)] # can i create s3 from interleaving len(s1) chars of s1 and len(s2) chars of s2?





  










