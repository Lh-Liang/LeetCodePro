#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#
# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        if not caption: return ""
        n = len(caption)
        i = 0
        result = []
        while i < n:
            count = 1
            while i + count < n and caption[i + count] == caption[i]:
                count += 1
            if count >= 3:
                result.extend(caption[i] * count) # already good segment
            else:
                # Handle segments less than 3 by adjusting characters
                if i > 0 and i + count < n and caption[i - 1] == caption[i + count]:
                    result.extend(caption[i - 1] * (3 - count)) # expand with previous char if possible 
                else:
                    result.extend(caption[i] * 3) # expand current char to make group good 
            i += count
        return ''.join(result) # @lc code=end