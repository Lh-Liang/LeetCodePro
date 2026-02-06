#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
from typing import List, Set, Tuple
from collections import defaultdict

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        def scs_length(x: str, y: str) -> int:
            m, n = len(x), len(y)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        dp[i][j] = i + j
                    elif x[i - 1] == y[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            return dp[m][n]
        
        def calculate_frequency(s: str) -> List[int]:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            return freq
        
        # Initialize a set to hold unique frequency tuples
        unique_freqs: Set[Tuple[int]] = set()
        
        # Use dynamic programming to find SCS for all pairs and build up solutions iteratively.
        # Start with an empty sequence and iteratively add each word.
        all_indices = range(len(words))
        current_scs_set: Set[str] = {''}
        for idx in all_indices:
            next_scs_set: Set[str] = set()
            current_word = words[idx]
            while current_scs_set:
                existing_scs = current_scs_set.pop()
                next_length = scs_length(existing_scs, current_word)
                # Create possible new SCS by merging existing with current word optimally.
                # Skip generation if it doesn't lead to shorter or same length solutions.
                new_scs_candidates: Set[str] = self.merge_sequences_optimally(existing_scs, current_word, next_length)
                next_scs_set.update(new_scs_candidates)
            current_scs_set = next_scs_set
        
        # Calculate frequencies for each unique SCS found that matches target length.
        for scs in current_scs_set:
            freq_array = tuple(calculate_frequency(scs))
            unique_freqs.add(freq_array)
        
        return list(unique_freqs)
    
def merge_sequences_optimally(self, x: str, y: str, target_length: int) -> Set[str]:
    # Implement merging logic here to generate optimal sequences based on DP table results...
n# @lc code=end