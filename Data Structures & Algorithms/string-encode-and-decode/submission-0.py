class Solution:

    def encode(self, strs: List[str]) -> str:
        # when encoding a list of strings into one string
        # what do we need to preserve?
        # the individual, consitutent strings i.e. the characters themselves
        # and where they start and end
        # a simple .join() preserves characters, but NOT boundaries
        # prefix each string with its length followed by a string marker e.g. '#'
        encoded_string = ''
        for s in strs:
            encoded_string += f'{len(s)}' + '#' + s # the '#' is needed for cases where length is double digit
        
        print(encoded_string)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        current_idx_pointer = 0
        marker_search_start_positions = [0]
        while current_idx_pointer < len(s):
            if s[current_idx_pointer] == '#':
                str_length = int(s[marker_search_start_positions[-1]:current_idx_pointer]) # every character from end of last str index to this hash comprises the length of the following string
                decoded_string.append(s[current_idx_pointer+1: current_idx_pointer+1+str_length])
                
                current_idx_pointer += (str_length+1)
                marker_search_start_positions.append(current_idx_pointer)
            
            current_idx_pointer += 1

        return decoded_string

