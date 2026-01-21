#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Count occurrences and positions of each number
        n = len(nums)
        indices = [[] for _ in range(51)]
        count_k = [0] * (n + 1)
        
        total_k = 0
        for i, x in enumerate(nums):
            if x == k:
                total_k += 1
            count_k[i + 1] = total_k
            indices[x].append(i)
            
        max_gain = 0
        
        # For each possible value v that we want to turn into k
        for v in range(1, 51):
            if v == k or not indices[v]:
                continue
            
            current_gain = 0
            local_max_gain = 0
            
            # Apply Kadane's algorithm logic on indices of v and k
            # We only need to consider subarrays starting and ending with v
            for i in range(len(indices[v])):
                if i > 0:
                    # Subtract the number of k's between the previous v and this v
                    # Number of k's in nums[indices[v][i-1]+1 : indices[v][i]]
                    num_k_between = count_k[indices[v][i]] - count_k[indices[v][i-1] + 1]
                    current_gain -= num_k_between
                    if current_gain < 0:
                        current_gain = 0
                
                current_gain += 1 # for the current v
                if current_gain > local_max_gain:
                    local_max_gain = current_gain
            
            if local_max_gain > max_gain:
                max_gain = local_max_gain
                
        return total_k + max_gain
# @lc code=end