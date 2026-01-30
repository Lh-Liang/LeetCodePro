#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # Step 1: Collect all unique letters
        unique_letters = sorted(set(''.join(words)))
        letter_to_idx = {ch: ord(ch)-ord('a') for ch in unique_letters}

        # Step 2: Compute the frequency requirement for each word
        from collections import Counter
        word_counts = [Counter(w) for w in words]

        # Step 3: DP to generate all possible SCS frequency multisets
        # Since each word is length 2, and <=16 unique letters, the max SCS is small
        from functools import lru_cache
        n = len(words)
        # For each word, keep a pointer for how much is matched
        @lru_cache(maxsize=None)
        def dp(pos_tuple):
            # pos_tuple: for each word, the position in that word
            if all(pos == 2 for pos in pos_tuple):
                return set([tuple([0]*26)])
            result = set()
            # Try all possible next letters
            for ch in unique_letters:
                new_pos = list(pos_tuple)
                advanced = False
                for i, pos in enumerate(pos_tuple):
                    if pos < 2 and words[i][pos] == ch:
                        new_pos[i] += 1
                        advanced = True
                if not advanced:
                    continue
                # Get all results from this move
                for freq in dp(tuple(new_pos)):
                    freq = list(freq)
                    freq[ord(ch)-ord('a')] += 1
                    result.add(tuple(freq))
            return result
        # Initial positions: all at 0
        all_freqs = dp(tuple(0 for _ in range(n)))
        # Deduplicate by permutation (multiset): keep only unique frequency multisets
        unique_multisets = set()
        final_result = []
        for freq in all_freqs:
            key = tuple(sorted([freq[i] for i in range(26) if freq[i] > 0]))
            if key not in unique_multisets:
                unique_multisets.add(key)
                final_result.append(list(freq))
        return final_result
# @lc code=end