#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#
# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        memo = {}
        
        def dfs(progress):
            # progress[i] = how many characters of word[i] have been matched
            if all(p == 2 for p in progress):
                return {tuple([0] * 26)}  # Base case: empty frequency
            
            if progress in memo:
                return memo[progress]
            
            # Get all unique characters
            chars = set()
            for word in words:
                chars.add(word[0])
                chars.add(word[1])
            
            min_len = float('inf')
            best_freqs = set()
            
            for ch in sorted(chars):  # Sort for consistency
                new_progress = list(progress)
                for i, word in enumerate(words):
                    if new_progress[i] < 2 and word[new_progress[i]] == ch:
                        new_progress[i] += 1
                
                # Skip if no progress was made
                if tuple(new_progress) == progress:
                    continue
                
                sub_freqs = dfs(tuple(new_progress))
                for freq in sub_freqs:
                    new_freq = list(freq)
                    new_freq[ord(ch) - ord('a')] += 1
                    total = sum(new_freq)
                    
                    if total < min_len:
                        min_len = total
                        best_freqs = {tuple(new_freq)}
                    elif total == min_len:
                        best_freqs.add(tuple(new_freq))
            
            memo[progress] = best_freqs
            return best_freqs
        
        initial_progress = tuple([0] * n)
        freqs = dfs(initial_progress)
        
        return [list(f) for f in freqs]
# @lc code=end