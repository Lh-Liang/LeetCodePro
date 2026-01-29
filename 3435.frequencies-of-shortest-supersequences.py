#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        from collections import defaultdict, Counter
        alphabet_size = 26
        unique_freqs = set()  # Store unique frequency tuples of SCSs
        
        def calculate_scs(w1, w2):
            m, n = len(w1), len(w2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(m + 1):
                dp[i][0] = i
            for j in range(n + 1):
                dp[0][j] = j
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if w1[i - 1] == w2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            
            # Construct the SCS from the DP table
            scs = []
            i, j = m, n
            while i > 0 and j > 0:
                if w1[i - 1] == w2[j - 1]:
                    scs.append(w1[i - 1])
                    i -= 1; j -= 1
                elif dp[i - 1][j] < dp[i][j - 1]:
                    scs.append(w1[i - 1])
                    i -= 1
                else:
                    scs.append(w2[j - 1])
                    j -= 1
            while i > 0:
                scs.append(w1[i - 1])
                i -= 1
            while j > 0:
                scs.append(w2[j - 1])
                j -= 1
            return ''.join(reversed(scs))
        
        # Generate all combinations of words to calculate their SCS frequencies.
        from itertools import combinations
        def get_frequencies(scs):
            freq_array = [0] * alphabet_size
            for char in scs:
                freq_array[ord(char) - ord('a')] += 1
            return tuple(freq_array)
        
        # Calculate pairwise SCS frequencies and store unique ones.
        for w_combination in combinations(words, len(words)):
sctxtxtxtxtxtxtxtxtxttxtxttxttxttxttxttxttxttxttttttttttttstststststscttxxftftfttftftftftftfttttbbbbbbsdsdsdsdsdsdssdsdsdsdssfdfffdffdfdfdfdfdfdfdfdfdffffff