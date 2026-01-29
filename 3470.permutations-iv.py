#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List
from math import factorial

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Calculate factorials up to n for combinatorial calculations
        factorials = [1] * (n + 1)
        for i in range(2, n + 1):
            factorials[i] = factorials[i - 1] * i
        
        # Helper function to determine the number of valid permutations starting with specific prefix
        def count_valid_permutations(prefix):
            remaining = n - len(prefix)
            half = (remaining + 1) // 2 if remaining % 2 == 1 else remaining // 2
            return factorials[half] * factorials[remaining - half]
        
        available = list(range(1, n + 1))
        result = []
        last_even = True # Start assuming an 'even spot'
        while available:
            found = False
            for i in range(len(available)):
                if (last_even and available[i] % 2 == 0) or (not last_even and available[i] % 2 != 0):
                    continue
                count = count_valid_permutations(result + [available[i]])
                if k > count:
                    k -= count
                else:
                    result.append(available.pop(i))
                    last_even = not last_even
                    found = True
                    break
            if not found:
                return [] # If no valid permutation is found within bounds of k, return an empty list.
        return result if len(result) == n else []
# @lc code=end