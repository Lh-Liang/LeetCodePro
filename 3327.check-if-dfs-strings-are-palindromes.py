#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        # Create adjacency list for tree representation
        children = defaultdict(list)
        for i in range(1, n):
            children[parent[i]].append(i)
        
        def is_palindrome(st):
            return st == st[::-1]
        
        def dfs(node):
            dfsStr = []
            stack = [node]
            while stack:
                current = stack.pop()
                dfsStr.append(s[current])
                for child in sorted(children[current], reverse=True): # Iterate children in increasing order of their numbers by reverse=True in stack append order. 
                    stack.append(child)
            return ''.join(dfsStr)
        
        answer = []
        for i in range(n):
            dfsStr = dfs(i)  # Get the DFS string starting from node i.
            answer.append(is_palindrome(dfsStr))  # Check if it is a palindrome.
        
        return answer
# @lc code=end