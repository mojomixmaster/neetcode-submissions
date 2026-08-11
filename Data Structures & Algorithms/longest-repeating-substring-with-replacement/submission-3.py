class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I need an O(n) time and O(m) space soln
        """
        Invariant: 
            the window is valid as long as k ≥ [(r - l + 1) - max_freq]  i.e. I have enough replacement tokens to make the entire window one character.
            
        Metadata to track:
            char_counts map: character → current count IN window, updated as r advances
            max_freq: running max of any character's count, updated in O(1) as max(max_freq, char_counts[s[r]]) i.e. never needs to decrease

        On left eviction: 
            char_counts[s[l]] -= 1, then l += 1. max_freq is left alone. A stale high value only makes the window conservatively smaller, never incorrectly larger.          
        """

        l = 0   # initalise my 2 pointers
        r = 0
        chars_in_window_count = {}
        count_of_most_frequent_char_in_window = 0
        length_of_longest_substring = 0

        while r < len(s): # algorithm iterates until right pointer is at end of array
            chars_in_window_count[s[r]] = chars_in_window_count.get(s[r], 0)
            chars_in_window_count[s[r]] += 1

            count_of_most_frequent_char_in_window = max(count_of_most_frequent_char_in_window, chars_in_window_count[s[r]])
            print(count_of_most_frequent_char_in_window)

            # now we need to check if window is valid ie invariant is preserved
            if k < ((r-l+1) - count_of_most_frequent_char_in_window): # if true: window is invalid
                print(f'Window found to be invalid at {r, l}')
                chars_in_window_count[s[l]] -= 1
                length_of_longest_substring = max(length_of_longest_substring, r-l) # the char we're currently on makes the window invalid - don't count it in
                l += 1 # decrement char count THEN increment left finger to next element to accurately reflect current char counts in the window
            
            # window is valid, so lets keep extending our window
            r += 1
            length_of_longest_substring = max(length_of_longest_substring, r-l)
        
        return length_of_longest_substring




