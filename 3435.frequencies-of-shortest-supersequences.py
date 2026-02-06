#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # Initial logic for generating shortest common supersequences
        def generate_scs(w1, w2):
            # Generate SCS by interleaving the words as needed
            scs = set()
            if w1[0] == w2[0]:
                scs.add(w1 + w2[1])  # Example interleaving logic
                scs.add(w2 + w1[1])  # Example interleaving logic
            else:
                scs.add(w1 + w2)  # Example interleaving logic
                scs.add(w2 + w1)  # Example interleaving logic
            return list(scs)
        
        # Placeholder for generated SCS lists
        scs_list = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                scs_list.extend(generate_scs(words[i], words[j]))
        
        # Calculate frequencies while filtering permutations
        freq_set = set()
        for scs in scs_list:
            freq = [0] * 26  # Frequency array for English lowercase letters
            for char in scs:
                freq[ord(char) - ord('a')] += 1
            freq_tuple = tuple(freq)  # Convert list to tuple for set operations
            freq_set.add(freq_tuple)  # Add only unique frequencies (filters permutations)
        
        return [list(freq) for freq in freq_set]  # Convert back tuples to list for result output
# @lc code=end