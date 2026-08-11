class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i need an O(n) time and O(m) space solution

        # i need an invariant 
        # at iteration i, the chars stored in my current longest string are unique

        longest_deduped_substring = 0

        # i need 2 fingers, left on the starting char of the substring
        # right scanning through the rest of the string until we hit a char already in substring
        i = 0
        while i < len(s):
            used_chars = set() # can strings be hashed? strings are immutable so yes!
            used_chars.add(s[i])
            j = i + 1
            while j < len(s):
                if s[j] not in used_chars:
                    used_chars.add(s[j])
                    j += 1
                else:
                    break # the next string is already in used_chars therefore this substring can no longer be constructed
            longest_deduped_substring = max(longest_deduped_substring, len(used_chars))
            
            i += 1

        return longest_deduped_substring

        