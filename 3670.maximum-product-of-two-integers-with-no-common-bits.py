#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None, None]
        
        def insert(root, num):
            node = root
            for i in range(19, -1, -1):
                bit = (num >> i) & 1
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        def query(root, forbidden):
            node = root
            res = 0
            for i in range(19, -1, -1):
                bit_f = (forbidden >> i) & 1
                if bit_f == 1:
                    if node.children[0] is None:
                        return 0
                    node = node.children[0]
                else:
                    if node.children[1] is not None:
                        res |= 1 << i
                        node = node.children[1]
                    elif node.children[0] is not None:
                        node = node.children[0]
                    else:
                        return 0
            return res
        
        nums.sort(reverse=True)
        root = TrieNode()
        ans = 0
        for num in nums:
            partner = query(root, num)
            ans = max(ans, num * partner)
            insert(root, num)
        return ans

# @lc code=end