class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we need an O(n) time and O(1) space solution

        # Invariant:
            # The window is valid iff it contains ALL of the chars in s1
        
        # Window Metadata:
            # chars_in_window: The letters in window
            # chars_in_s1: the chars in s1. should not be set as algorithm will fail in cases where s1 has duplicate chars
                # perhaps an array where index is count and value is which chars appear that specific number of counts? array = array. We can tuple array to hash to enable O(1) comparison.
                # Hmmm.... too complicated actually, lets just keep a dict of key: value for both chars_in_s1 and chars_in_window but thats O(n) space!
                # We can instead just track an integer 'chars_satisfied' where this int represents the number of chars in s1 currently in the window that have the same counts as in s1
        
        # What do I update when l moves forward?
            # chars_in_window: discard the letter was previously the first letter in the window and update the count

        # we can slightly amend our invariant to account for this tracking int: window is valid if chars_satisfied = true
        # window size is FIXED to the length of s1

        l = 0
        r = 0
        char_counts_in_window = {}
        char_counts_in_s1 = {}
        chars_satisfied = 0

        if len(s2) < len(s1):
            return False

        for char in s1:
            char_counts_in_s1[char] = char_counts_in_s1.get(char, 0)
            char_counts_in_s1[char] += 1
        
        while r < len(s2):
            char_counts_in_window[s2[r]] = char_counts_in_window.get(s2[r], 0)
            char_counts_in_window[s2[r]] += 1

            if s2[r] in s1 and char_counts_in_window[s2[r]] == char_counts_in_s1[s2[r]]:
                chars_satisfied += 1 # we are saying that there is now ONE more character in s2's window whose count is the exact same as in s1

            if r-l+1 == len(s1): # if our window size is equal to s1, lets test if the window is valid
                if chars_satisfied == len(char_counts_in_s1): # window validation test
                    return True
                if s2[l] in char_counts_in_s1 and char_counts_in_window[s2[l]] == char_counts_in_s1[s2[l]]:
                    chars_satisfied -= 1 # we're about to incremenet l and discard this char, if it WAS in s1, we will unfortunately have to decrement its count and therefore chars_satisfied
                
                char_counts_in_window[s2[l]] -= 1
                l += 1 # we reached a window size of len(s1) yet chars_satisfied wasn't equal to number of keys needed to be satisfied in char_counts_in_s1
            
            r += 1

        return False