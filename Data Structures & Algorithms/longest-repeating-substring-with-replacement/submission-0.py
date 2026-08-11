class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I need an O(n) time and O(m) space soln
        # what is my invariant?
        # Constraint: I can only replace k characters with any other character in english alphabet
        # INVARIANT: 
            # If i have a string of length L, and most freq char appears f times
            # i need L-f replacements to make string entirely unique.
            # Therefore, my window is VALID iff k >= L-f i.e. 
            # I have enough replacement tokens to make string unique.

        # how do i track f as window slides? build char:count dict!
        max_string_length = 0
        char_counts = {}
        l = 0
        r = 0
        max_freq = 0

        while r < len(s):
            f_count = char_counts.get(s[r], 0)
            char_counts[s[r]] = f_count+1 # map updates as window slides

            max_freq = max(max_freq, char_counts[s[r]])

            if k < ((r-l+1) - max_freq): # window INVALID ie keeps invariant TRUE
                char_counts[s[l]] -= 1
                l += 1
            max_string_length = max(max_string_length, (r-l+1))
            r += 1
        return max_string_length



