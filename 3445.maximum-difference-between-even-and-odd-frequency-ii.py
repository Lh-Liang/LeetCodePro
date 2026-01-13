#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        max_diff = float('-inf')
        
        for i in range(n):
            freq = {}
            for j in range(i, n):
                # Update frequency for s[j]
                freq[s[j]] = freq.get(s[j], 0) + 1
                
                # Check if substring length is at least k
                if j - i + 1 >= k:
                    # Find max odd frequency
                    max_odd = float('-inf')
                    for count in freq.values():
                        if count % 2 == 1:
                            max_odd = max(max_odd, count)
                    
                    # Find min even frequency
                    min_even = float('inf')
                    for count in freq.values():
                        if count % 2 == 0:
                            min_even = min(min_even, count)
                    
                    # Calculate difference if both exist
                    if max_odd != float('-inf') and min_even != float('inf'):
                        max_diff = max(max_diff, max_odd - min_even)
        
        return int(max_diff)
# @lc code=end