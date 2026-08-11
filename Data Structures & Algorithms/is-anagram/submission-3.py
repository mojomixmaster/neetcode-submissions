class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        s_chars = dict()
        t_chars = dict()
        for ch in s:
            if ch not in s_chars:
                s_chars[ch] = 1
            s_chars[ch] += 1
        for ch in t:
            if ch not in t_chars:
                t_chars[ch] = 1
            t_chars[ch] += 1

        if s_chars == t_chars:
            is_anagram = True
        
        return is_anagram