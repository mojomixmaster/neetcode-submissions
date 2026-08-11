class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i need an O(n) time algorithm
        # what exactly counts as a palindrome? only letters and digits ie strings stripped of any whitespaces
        # lower and upper case are equivalent
        # can i avoid building a new string?
        # yes! we can use 2 pointers (2 finger algo) one finger on first element and one finger on last then move both fingers to middle
        
        # is_palindrome = True -> no need for this, excess state. just return immediately if not palindrome
        stripped_string = s.strip().lower() # we will skip invalid chars in place
        # to build a clean string you can loop through s and use if statement to
        # employ an .isalnum() func -> if true -> append to cleaned_string
        # IMPORTANT: .lower() creates whole new string which is O(n) memory 

        print(stripped_string)

        i = 0 # finger 1
        j = (len(stripped_string) - 1) # finger 2
        while i < j: # 2 fingers should be indep vars and NEVER overlap

            while i < j and not stripped_string[i].isalnum(): # always confirm bounds before indexing
                print(f"skipping {stripped_string[i]}")
                i += 1
            while j > i and not stripped_string[j].isalnum():
                print(f"Skipping: {stripped_string[j]}")
                j -= 1

            if stripped_string[i] != stripped_string[j]:
                return False
            else:
                i, j = i+1, j-1
        
        return True