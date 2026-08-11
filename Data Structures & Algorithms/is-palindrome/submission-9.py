class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i need an O(n) time algorithm
        # what exactly counts as a palindrome? only letters and digits ie strings stripped of any whitespaces
        # lower and upper case are equivalent
        # can i avoid building a new string?
        # yes! we can use 2 pointers (2 finger algo) one finger on first element and one finger on last then move both fingers to middle
        
        is_palindrome = True
        stripped_string = s.strip().lower() # we will skip invalid chars in place
        # to build a clean string you can loop through s and use if statement to
        # employ an .isalnum() func -> if true -> append to cleaned_string 

        print(stripped_string)

        i = 0 # finger 1
        j = (len(stripped_string) - 1) # finger 2
        c = len(stripped_string) // 2
        while i < j: 

            while not stripped_string[i].isalnum() and i < j:
                print(f"skipping {stripped_string[i]}")
                i += 1
            while not stripped_string[j].isalnum() and j > i:
                print(f"Skipping: {stripped_string[j]}")
                j -= 1

            if stripped_string[i].isalnum() and stripped_string[j].isalnum():
                if stripped_string[i] != stripped_string[j]:
                    is_palindrome = False
                    break
                else:
                    i, j = i+1, j-1
        
        return is_palindrome