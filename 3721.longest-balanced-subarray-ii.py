#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        # Segment Tree arrays: 4 * n size
        # tree_min stores the minimum value in the range
        # tree_max stores the maximum value in the range
        # lazy stores the pending updates
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(v):
            if lazy[v] != 0:
                lazy[2*v] += lazy[v]
                tree_min[2*v] += lazy[v]
                tree_max[2*v] += lazy[v]
                
                lazy[2*v+1] += lazy[v]
                tree_min[2*v+1] += lazy[v]
                tree_max[2*v+1] += lazy[v]
                
                lazy[v] = 0

        def update(v, tl, tr, l, r, add):
            if l > r:
                return
            if l == tl and r == tr:
                tree_min[v] += add
                tree_max[v] += add
                lazy[v] += add
            else:
                push(v)
                tm = (tl + tr) // 2
                update(2*v, tl, tm, l, min(r, tm), add)
                update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
                tree_min[v] = min(tree_min[2*v], tree_min[2*v+1])
                tree_max[v] = max(tree_max[2*v], tree_max[2*v+1])

        def query(v, tl, tr):
            # If 0 is not within the range [min, max], it doesn't exist in this node's range
            if tree_min[v] > 0 or tree_max[v] < 0:
                return -1
            
            if tl == tr:
                return tl
            
            push(v)
            tm = (tl + tr) // 2
            
            # Try to find the first zero in the left child
            res = query(2*v, tl, tm)
            if res != -1:
                return res
            
            # If not found in left, try right child
            return query(2*v+1, tm+1, tr)

        last_pos = {}
        ans = 0
        
        for i, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            # If x is even, it adds +1 to the balance (distinct even - distinct odd)
            # If x is odd, it adds -1 to the balance
            val = 1 if x % 2 == 0 else -1
            
            # Update the range (prev + 1, i) for all start indices l
            # where the current x is a new distinct element.
            update(1, 0, n-1, prev + 1, i, val)
            
            # Find the smallest index l such that the subarray nums[l...i] is balanced (diff is 0)
            idx = query(1, 0, n-1)
            
            # If a valid index is found and it's within the current processed range
            if idx != -1 and idx <= i:
                ans = max(ans, i - idx + 1)
            
            last_pos[x] = i
            
        return ans
# @lc code=end