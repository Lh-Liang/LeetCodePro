#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

from typing import List
import sys

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v,l in edges:
            adj[u].append((v,l))
            adj[v].append((u,l))
        
        sys.setrecursionlimit(100000)
        
        best_len = -float('inf')
        min_nodes = float('inf')
        
        # Stacks
        path_nodes = []          # stores nodes along current DFS branch
        path_cum = []           # cumulative lengths
        last_seen = {}          # value -> index in stack
        
        def dfs(u:int, parent:int, cum:int, lb_parent:int):
            nonlocal best_len, min_nodes
            
            idx_before_push = len(path_nodes)
            val = nums[u]
            
            # compute local lower bound
            local_lb = lb_parent
            prev_idx = last_seen.get(val)
            if prev_idx is not None:
                local_lb = max(local_lb, prev_idx + 1)
            
            # save previous state
            saved_exist = False
            saved_idx = None
            if val in last_seen:
                saved_exist = True
                saved_idx = last_seen[val]
            
            # update last_seen BEFORE pushing
            last_seen[val] = idx_before_push
            
            # push onto stacks
            path_nodes.append(u)
            path_cum.append(cum)
            
            # compute candidate special path ending here
            req_idx = local_lb          # earliest allowed starting index
            cand_len = cum - path_cum[req_idx]
            cand_nodes = idx_before_push - req_idx + 1
            
            # update global answer
            if cand_len > best_len:
                best_len = cand_len
                min_nodes = cand_nodes
            elif cand_len == best_len:
                min_nodes = min(min_nodes, cand_nodes)
            
            # recurse children
            for neigh,w in adj[u]:
                if neigh == parent:
                    continue
                next_cum = cum + w
                dfs(neigh,u,next_cum,local_lb)
                
            # backtrack
            path_nodes.pop()
            path_cum.pop()
            if saved_exist:
                last_seen[val] = saved_idx
            else:
                del last_seen[val]
        
        dfs(0,-1,0,0)
        
        return [best_len,int(min_nodes)]
# @lc code=end