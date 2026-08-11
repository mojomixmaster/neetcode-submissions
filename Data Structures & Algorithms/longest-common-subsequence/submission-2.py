class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # abstract the problem:
        # we are given two strings and we need to find the longest
        # sequence of letters that exists in BOTH strings. the final answer is the
        # integer length of this string.

        # naively, it seems that we need to exhaust the search space and ensure we 
        # have checked all possible string sequeneces in list1 and then check if it exists
        # in list2. This is an O(n**2) algorithm where we have 2 fingers on text1's first letter,
        # we take that current substring (text1[0]) and see if it exists in text2 (O(n) search)
        # we then update longest_seen_substring if its length is greater than current
        # longest_seen_substring and move our right finger forward (updating some counter as well 
        # of the last letter in the substring's index in the main string), checking if the 
        # substring exists repeatedly until our right finger reaches the end of the string. 
        
        # For every 
        # iteration in which adding that new letter the right finger moves to, to current 
        # longest_seen_substring and that new substring does not exist, right finger simply moves 
        # one more and checks if this newly concoted substring exists, and so on.
        
        # Then we repeat the entire process with both fingers starting on the 2nd letter in the 
        # string (text1[1]).
        # This is O(n**2), is there a faster approach?

# Bottom-up approach. If i have two strings "aaab" and "bbaab", the LCS is "aab".
# Starting from the first letter of each string, is the first letter in ecah string the same? If not, either move the finger of left string forward OR the finger of right string forward and repeat check for identical letters. This is equivalent to moving our position on the dp grid either RIGHT or DOWN. If letters are identical, we advance both fingers to thus move our position DIAGONALLY right.

# I am solving the top-level problem by first solving smaller, simpler problems and re-using their solutions to avoid recomputation -> dynamic programming!

# dp table: dp[l][r] = longest common substring found for left string suffix from index l inclusive and right string suffix from index r inclusive.

        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)] # indices are 0-indexed to allow for base case comparisons between empty substrings to always equal 0
        # we need to build our dp table from the bottom-up to allow for this dynamic, quick table navigation we speak of above ie all values of the table need to be filled before table navigation. for this, we need to build from our base cases up.
        # rows are text1, columns are text2. we need to build from bottom right corner going left finishing the last row then go one row up and repeat until we've finished the table.
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # the 2 letters are identical so the answer for the lcs is the answer for the lcs of each string's suffix starting from the next index (text1[i+1:], text2[j+1:]) PLUS 1 to include the current indices which are identical (automatically add 1 to the prev calculated lcs answer)
                
                else: # we take the max of the lcs between one of the current suffixes and, for the string not chosen to remain at its current suffix, its suffix most recently used in a lcs calculation (which is the suffix that omits the current letter ie 1 letter shorter).
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        


        

