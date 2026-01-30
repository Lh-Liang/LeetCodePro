#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from typing import List
import heapq

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.alive = True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
            return 0

        n = len(nums)
        nodes = [Node(v, i) for i, v in enumerate(nums)]
        for i in range(n-1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]

        heap = []
        pair_map = {}
        for i in range(n-1):
            s = nodes[i].val + nodes[i+1].val
            heapq.heappush(heap, (s, i))
            pair_map[(nodes[i].idx, nodes[i+1].idx)] = (s, i)

        ans = 0
        while True:
            arr = []
            curr = nodes[0]
            while curr:
                if curr.alive:
                    arr.append(curr.val)
                curr = curr.next
            if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
                break

            while heap:
                s, i = heapq.heappop(heap)
                left = nodes[i]
                right = left.next
                if left and right and left.alive and right.alive and left.next == right:
                    break
            # Merge left and right
            left.val += right.val
            right.alive = False
            left.next = right.next
            if right.next:
                right.next.prev = left
            # Remove obsolete pairs from heap (done by checking alive above)
            # Insert new pair with left and its new next, and its prev and left
            if left.next and left.next.alive:
                heapq.heappush(heap, (left.val + left.next.val, left.idx))
            if left.prev and left.prev.alive:
                heapq.heappush(heap, (left.prev.val + left.val, left.prev.idx))
            ans += 1
        return ans
# @lc code=end