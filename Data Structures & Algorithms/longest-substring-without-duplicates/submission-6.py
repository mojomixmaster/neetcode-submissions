class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i need an O(n) time and O(m) space solution

        # i need an invariant 
        # at iteration i, the chars stored in my current longest substring are unique

        longest_deduped_substring = 0

        # i need 2 fingers, left on the starting char of the substring
        # right scanning through the rest of the string until we hit a char already in substring

        # now we've got a correct solution... we need a more time efficient soln as we are currently O(n^2)
        # are we recomputing anything on each iteration? yes! we've already seen chars to the right, no need to loop again
        i = 0
        j = 0
        used_chars = {} # can strings be hashed? strings are immutable so yes!
        # key is char, value is index it was last seen at
        while j < len(s):
            if s[j] not in used_chars:
                used_chars[s[j]] = j
            else:
                i = max(i, used_chars[s[j]] + 1) # we need to respect invariant: only unique chars in sliding window
                # the next char is already in used_chars therefore this substring can no longer be constructed
                # all we need to do is discard the old duplicate and keep the NEW index of the duplicate char in our window

                used_chars[s[j]] = j                

            j += 1
            longest_deduped_substring = max(longest_deduped_substring, j-i) # length of window includes the char we just validated right before we move onto next iteration
        return longest_deduped_substring

        