class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_string_counts = dict() # storing all seen str idxs with key being str's counts array (cast to str for immutability)
        grouped_anagrams = []
        grouped_anagram_index = 0
        for s in strs: # enumerate is 0-indexed
            print(f"anagram_index {grouped_anagram_index}, string {s}")

            counts = [0] * 26 # 1d list NOT a nested list as you might've worried 
            for ch in s:
                print(ch)
                counts[ord(ch) - ord('a')] += 1 # lowercase letter ASCII ordering to find index in alphabet
            
            counts = tuple(counts) # cast to tuple as tuple is immutable
            print(counts)
            correct_anagram_idx = seen_string_counts.get(counts, None)

            if correct_anagram_idx is not None:
                print(correct_anagram_idx)
                # print(counts)
                grouped_anagrams[correct_anagram_idx].append(s)
            
            else:
                print(correct_anagram_idx)
                seen_string_counts[counts] = grouped_anagram_index # place the new, unique string into its own index in final output list
                grouped_anagrams.append([s])
                grouped_anagram_index += 1

        return grouped_anagrams

