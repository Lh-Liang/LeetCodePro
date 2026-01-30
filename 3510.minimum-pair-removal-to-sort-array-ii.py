#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Step 1: Early check for non-decreasing array
        if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
            return 0
        n = len(nums)
        arr = list(nums)
        ops = 0
        # Maintain (sum, index, version) for each pair
        heap = []
        version = [0] * n
        for i in range(n-1):
            heapq.heappush(heap, (arr[i]+arr[i+1], i, version[i], version[i+1]))
        while len(arr) > 1:
            # Step 2: Select leftmost minimum-sum valid pair
            while True:
                s, i, v1, v2 = heapq.heappop(heap)
                # Step 3: Ensure validity of selected pair
                if i < len(arr)-1 and version[i] == v1 and version[i+1] == v2:
                    break
            # Step 4: Merge pair and update data structures
            arr[i] = arr[i] + arr[i+1]
            version[i] += 1
            arr.pop(i+1)
            version.pop(i+1)
            ops += 1
            # Step 5: Update heap for affected pairs
            if i-1 >= 0:
                heapq.heappush(heap, (arr[i-1]+arr[i], i-1, version[i-1], version[i]))
            if i < len(arr)-1:
                heapq.heappush(heap, (arr[i]+arr[i+1], i, version[i], version[i+1]))
            # Step 6: Verification after each operation
            if all(arr[j] <= arr[j+1] for j in range(len(arr)-1)):
                break
        return ops
# @lc code=end