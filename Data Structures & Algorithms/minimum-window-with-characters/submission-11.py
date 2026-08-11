class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # i will need to loop through s
        # and identify whenever the char im currently on is also in T
        # if in T, remove it from a set of chars_in_T_not_yet_included
        # and append to the final str: min_window_substring

        # on first glance, this seems like a for loop through s...
        # wait, it seems like a sliding window problem
        # left edge clamped to some starting index in the for loop
        # right edge (window) keeps growing (adding items to window) until the window contains
        # ALL the chars in T

        # we will need to keep track of what the shortest candidate string is so far...
        # im fairly confident this algo starts with looping through s O(n)

        # What am I actually computing? For each char, I am testing, is it in T, if so, append to some
        # candidate string. Once i am at end of s OR all chars of T in string, append that candidate string
        # to a list of the candidate strings we will then loop through to find the shortest one

        # hmmm.... we can fix this by saying candidate_substring_length = len(c_substring)
        # if c_sub_length < current_min_length:
        # min_window_substring = candidate_window_substring

        # how do i keep track of whats already been included from T ? as this will need to 
        # consider duplicates as individual chars. ok what if we have a key:char value: counts in t dict
        # candidate string only considered if ALL values in dict are 0

        chars_in_t = {}
        for char in t:
            chars_in_t[char] = chars_in_t.get(char, 0)
            chars_in_t[char] += 1

        l = 0 # window edges both initialised to first char
        r = 0
        min_window_substring = ""
        candidate_substring = ""
        
        candidate_counts = chars_in_t.copy()
        while r < len(s):
            # print(s[r])
            if s[r] in t: # if the counts for that specific char in t already satifisfied, ensure value never goes below zero

                candidate_counts[s[r]] = max(0, candidate_counts[s[r]]-1)

                if not candidate_substring:
                    l = r # only slide window if our candidate string is still empty (start window from this point of first t match)

                candidate_substring += s[r] # start the window from the first match with t
            
            else: # else block is needed here to avoid duplicate additions of chars in t
                if candidate_substring:
                    candidate_substring += s[r] # we add characters in from the right, discard from left
            
            if not any(candidate_counts.values()): # checks if all values of counts dict are 0 -> criteria for valid substring met!
                # print('dih empty!')
                if not min_window_substring or (len(candidate_substring) < len(min_window_substring)): # if all values are Falsy ie 0. .values() returns a dict_values object which IS iterable
                    min_window_substring = candidate_substring
                    # print(f"min window equal to {min_window_substring}")
                candidate_substring = "" # reset candidate string to evaluate downstream candidates
                candidate_counts = chars_in_t.copy() # reset counts dict to evaluate downstream candidates

                r = l # directly attached to the new window starting index stored in l
                num_t_matches = 0
                # print(f"new window start {s[r]}")

            r += 1

        return min_window_substring