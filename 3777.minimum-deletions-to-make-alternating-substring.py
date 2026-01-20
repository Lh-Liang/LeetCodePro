#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class FenwickTree:
    __slots__ = 'tree'
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Convert string to integer array: 0 for 'A', 1 for 'B'
        arr = [0] * n
        for i, c in enumerate(s):
            if c == 'B':
                arr[i] = 1
        
        # Fenwick Tree to store differences between adjacent characters.
        # We track `diff[i]` which is 1 if arr[i] != arr[i+1] else 0.
        # This is stored at index `i+1` in the 1-based Fenwick Tree.
        ft = FenwickTree(n)
        
        # Build initial state
        for i in range(n - 1):
            if arr[i] != arr[i+1]:
                ft.update(i + 1, 1)
        
        ans = []
        for q in queries:
            if q[0] == 1:
                idx = q[1]
                
                # Update left neighbor relation (diff at idx-1, stored at idx)
                if idx > 0:
                    # If currently equal, they become different -> add 1
                    # If currently different, they become equal -> sub 1
                    if arr[idx-1] == arr[idx]:
                        ft.update(idx, 1)
                    else:
                        ft.update(idx, -1)
                        
                # Update right neighbor relation (diff at idx, stored at idx+1)
                if idx < n - 1:
                    if arr[idx] == arr[idx+1]:
                        ft.update(idx + 1, 1)
                    else:
                        ft.update(idx + 1, -1)
                
                # Flip the character
                arr[idx] ^= 1
                
            else:
                l, r = q[1], q[2]
                if l == r:
                    ans.append(0)
                else:
                    # Number of diffs in s[l...r] is sum of diffs for indices l to r-1.
                    # In BIT, this corresponds to query(r) - query(l).
                    count_diffs = ft.query(r) - ft.query(l)
                    
                    # LAS length = count_diffs + 1
                    # Deletions = (r - l + 1) - LAS length
                    #           = (r - l + 1) - (count_diffs + 1)
                    #           = r - l - count_diffs
                    ans.append(r - l - count_diffs)
                    
        return ans
# @lc code=end