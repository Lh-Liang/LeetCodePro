#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#
# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        from collections import Counter
        from itertools import permutations
        # Generate all possible SCS
        scs_set = set()
        for perm in permutations(words):
            scs = self.shortest_common_supersequence(perm)
            scs_set.add(scs)
        # Compute frequency arrays and filter duplicates
        freq_list = []
        seen_freqs = set()
        for scs in scs_set:
            freq = [0] * 26 # Frequency array for each letter a-z
            for char in scs:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) not in seen_freqs:
                seen_freqs.add(tuple(freq))
                freq_list.append(freq)
        return freq_list
    
    def shortest_common_supersequence(self, perm): # Helper function to find SCS of permuted words.
        # This function assumes 'perm' is a permutation of 'words' and returns the shortest common supersequence. 
        result = perm[0]
        for word in perm[1:]:
            i, j = 0, 0
            # Merge two words into an SCS by including all characters from both in order. 
            while i < len(result) and j < len(word): 
                if result[i] == word[j]: 
                    j += 1 	# Move along both strings if characters match. 	n                i += 1 	# Always move along the result string. 	n            result += word[j:] # Append remaining characters of 'word'. 	n         return result # Return the constructed SCS string. 	n# @lc code=end