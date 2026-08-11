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
        # I am at the start of a packet.
        # Find this packet's marker.
        # Decode this packet.
        # Jump to the next packet.
        decoded_string = []
        current_idx_pointer = 0

        while current_idx_pointer < len(s):
            j = current_idx_pointer

            while j < len(s) and s[j] != '#':
                j += 1
            
            str_length = int(s[current_idx_pointer:j])
            
            decoded_string.append(s[j+1: j + 1 + str_length])
            current_idx_pointer = (j+1+str_length)

        return decoded_string

