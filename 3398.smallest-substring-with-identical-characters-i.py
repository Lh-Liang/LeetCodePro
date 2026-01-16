#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        # Binary search on the answer
        def canAchieve(maxLen: int) -> bool:
            # For each possible substring of length maxLen, check if we can break all longer segments
            # with at most numOps flips
            
            # First, find all maximal segments of identical characters
            segments = []
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                segments.append((i, j - 1))
                i = j
            
            # For a given maxLen, we need to ensure no segment is longer than maxLen
            # We can reduce a segment of length L to at most maxLen by flipping
            # ceil((L - maxLen) / 2) characters in optimal positions
            
            ops_needed = 0
            for start, end in segments:
                length = end - start + 1
                if length > maxLen:
                    # Number of operations needed to break this segment
                    # We place breaks every maxLen characters
                    # The number of breaks needed is ceil(length / maxLen) - 1
                    # But it's easier to think: we need to reduce length to maxLen
                    # We can reduce it by flipping every other character in the excess part
                    # If length is L and maxLen is M, excess is (L-M)
                    # We need to flip ceil((L-M)/2) characters
                    ops_needed += (length - maxLen + 1) // 2
                    if ops_needed > numOps:
                        return False
            return ops_needed <= numOps
        
        # Binary search for the minimum possible length
        left, right = 1, n
        result = n
        
        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
# @lc code=end