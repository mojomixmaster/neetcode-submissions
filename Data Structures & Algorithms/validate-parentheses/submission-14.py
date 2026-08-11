class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)) % 2 != 0: return False # str length must be even if it is to be composed of only bracket types
        # AND is valid

        # We are given string s
        # task: check if its valid ie all opening parentheses of a certain type can be paired
        # with their corresponding closing parentheses of same type. Brackets must be closed
        # in correct order ie if opening bracket of type B appears after type A, then its closing bracket
        # should appear before type A's i.e [A B B A].


        # what are we computing at each step?
        # We iterate through s until we find all opening parentheses, then loop through s again
        # until all closed brackets have been found and in correct order.
        # if either of valid conditions fails, immediatey return false

        # if '(' appears at index 4 and '{' appears at index 5 then the index at which 
        # '}' appears should be BEFORE ie SMALLER THAN ')'.

        # what data structure can support this type of computation?
        # if we keep a direct access array where each index is associated to one char (bracket type)
        # and the value are the indices within the STRING where that char was seen
        # if we loop through string and register at each index in arr how many times the 
        # associated char was seen
        # then perform our validation check
        # if that array is a full list of 0s -> string is valid
        # ensure we are not scanning the same redundant sections of the array on each computation step

        opening_bracket_types = ['(', '{', '[']
        closing_bracket_types = [')', '}', ']']
        char_pairs = {}
        for i in range(len(opening_bracket_types)):
            char_pairs[opening_bracket_types[i]] = closing_bracket_types[i]
        
        pairs_to_match = len(s) // 2
        matched_pair_indices = set()
        
        while pairs_to_match > 0:
            idx_of_last_opening_bracket = -1
            idx_of_first_closing_bracket = None
            for i in range(len(s)):
                curr = s[i]
                if s[i] in opening_bracket_types and i not in matched_pair_indices:
                    idx_of_last_opening_bracket = max(idx_of_last_opening_bracket, i)

                elif s[i] in closing_bracket_types and i not in matched_pair_indices:
                    idx_of_first_closing_bracket = i
                    break
            

            if idx_of_last_opening_bracket == -1 or idx_of_first_closing_bracket is None: return False
            if s[idx_of_first_closing_bracket] == char_pairs[s[idx_of_last_opening_bracket]]: # the pair has been correctly matched
                matched_pair_indices.add(idx_of_last_opening_bracket)
                matched_pair_indices.add(idx_of_first_closing_bracket)
                pairs_to_match -= 1
            else: return False

        return True





            
            
            

            


       
            

            

