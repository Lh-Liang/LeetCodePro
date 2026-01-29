#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        import heapq
        n = len(nums)
        if n <= 1:
            return 0
        operations = 0
        # Priority queue to store pairs (sum, index) sorted by sum
        pq = [(nums[i] + nums[i+1], i) for i in range(n - 1)]
        heapq.heapify(pq)
        # A set to keep track of valid indices in current nums array
        valid_indices = set(range(n))
        while True:
            # Check if already sorted or empty after operations
            if all(nums[i] <= nums[i+1] for i in range(n-1) if i in valid_indices):
                break
            while pq:
                min_sum, idx = heapq.heappop(pq)
                # Check if index is still valid in current nums array
                if idx in valid_indices and idx + 1 in valid_indices:
                    # Replace pair with their sum in nums array at idx position
                    nums[idx] = min_sum
                    valid_indices.remove(idx + 1)
                    operations += 1
                    # Update only necessary parts of priority queue for changed index positions
                    if idx - 1 in valid_indices:
                        heapq.heappush(pq, (nums[idx-1] + nums[idx], idx-1))
                    if idx + 2 in valid_indices:
                        heapq.heappush(pq, (nums[idx] + nums[idx+2], idx+1))
                    break
        return operations
# @lc code=end