#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
from typing import List
from collections import Counter
from itertools import permutations, combinations

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # Helper function to calculate frequency array
        def calculate_frequency(s):
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            return freq
        
        # Function to check if s2 is a subsequence of s1 using two-pointer technique
        def is_subsequence(s1, s2):
            it = iter(s1)
            return all(char in it for char in s2)
        
        # Generate candidate supersequences by combining words minimally and checking subsequences
        def generate_supersequences(words):
            result_set = set()
            for perm in permutations(words):
                current_scs = perm[0]
                for word in perm[1:]:
                    if not is_subsequence(current_scs, word):
                        current_scs += ''.join([ch for ch in word if ch not in current_scs])
                result_set.add(current_scs)
            return result_set
        
        scs_set = generate_supersequences(words)
        unique_freqs = {tuple(calculate_frequency(scs)) for scs in scs_set}
        return list(unique_freqs)
# @lc code=end