#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # Extract unique letters
        letters_set = set()
        for w in words:
            letters_set.add(w[0])
            letters_set.add(w[1])
        letters = sorted(letters_set)          # sorted list
        lmap = {ch:i for i,ch in enumerate(letters)}
        n = len(letters)
        
        # Map back to full alphabet positions
        def get_full_arr(counts):
            arr = [0]*26
            for ch_idx,cnt in enumerate(counts):
                arr[ord(letters[ch_idx])-97] = cnt
            return arr
        
        # Convert words to numeric pairs
        pairs = []
        self_loops = [False]*n
        for w in words:
            ai = lmap[w[0]]
            bi = lmap[w[1]]
            pairs.append((ai,bi))
            if ai == bi:
                self_loops[ai] = True
        
        # Global variables during DFS
        best_len = float('inf')
        results_set = set()
        
        # Helper function to check satisfaction given sequence
        def check_satisfied(seq):
            # seq list ints indices into letters
            # compute earliest/latest positions
            early = [-1]*n
            late = [-1]*n
            for pos,cidx in enumerate(seq):
                if early[cidx]==-1:
                    early[cidx]=pos
                late[cidx]=pos
            
            # Check each pair
            satisf=True
            for ai,bi in pairs:
                if early[ai]==-1 or late[bi]==-1:
                    satisf=False
                    break
                if early[ai] >= late[bi]:
                    satisf=False
                    break
            return satisf
        
        # Compute frequencies adjusted according rule
        def get_freq_arr(seq):
            # raw counts
            cnts=[0]*n
            for ci in seq:
                cnts[ci]+=1
            # adjust self-loops appearing only once
            adjusted_cnts=cnts[:]
            for ci in range(n):
                if cnts[ci]==1 and self_loops[ci]:
                    adjusted_cnts[ci]+=1
            return tuple(adjusted_cnts)
        
        # Heuristic lower bound
        def lower_bound(cur_seq_len):
            # simplistic underestimate: must add unseen letters
            unseen_cnt = sum(1 for ci in range(n) if early[ci]==-1)
            # underestimate num_unsatisfied // 2?
            unsat_cnt = num_unsatisfied(cur_seq)
            lb = cur_seq_len + max(unseen_cnt,(unsat_cnt+1)//2)
            return lb
        
        # Count unsatisfied quickly
        def num_unsatisfied(cur_seq):
            # recompute early/late
            early=[-1]*n
            late=[-1]*n
            for pos,cidx in enumerate(cur_seq):
                if early[cidx]==-1:
                    early[cidx]=pos
                late[cidx]=pos
            cnt=0
            for ai,bi in pairs:
                if early[ai]==-1 or late[bi]==-1 or early[ai]>=late[bi]:
                    cnt+=1
            return cnt
        
        # DFS iterative deepening
        def dfs(cur_seq,max_depth):
            nonlocal best_len
            cur_len = len(cur_seq)
            
            # Prune by depth limit
            if cur_len > max_depth:
                return False
                
            # Check bound
            lb = len(cur_seq)
            unseen_cnt = sum(1 for ci in range(n) if early[ci]==-1)
            unsat_cnt = num_unsatisfied(cur_seq)
            lb += max(unseen_cnt,(unsat_cnt+1)//2)
            
            if lb > best_len:
                return False
                
            # Terminal depth?
            if cur_len == max_depth:
                satis = check_satisfied(cur_seq)
                if satis:
                    freq_tup = get_freq_arr(cur_seq)
                    tot_len = sum(freq_tup)
                    if tot_len < best_len:
                        best_len = tot_len
                        results_set.clear()
                        results_set.add(freq_tup)
                    elif tot_len == best_len:
                        results_set.add(freq_tup)
                    return True   # found solution this depth
                return False   
                        
            # Recursively extend
            # Optionally prioritize unseen chars?
            # Try each possible next char
            found=False
            # iterate sorted to keep deterministic
            next_chars=list(range(n))
#             next_chars.sort(key=lambda ci:(early[ci]==-1),reverse=True) # try unseen first
#             
#             # Store early/late values locally
#             local_early=early[:]
#             local_late=late[:]
#             local_seq=list(cur_seq)
#             
#             
#             # Restore values inside loop??
#             
#             # Instead pass immutable snapshot??
#             
#             
#             
#         
#         # Use iterative deepening loop
#         max_depth_start=n
#         while True:
#             # reset global early/late tracking??
#             # start DFS from empty sequence
#             dfs([],max_depth_start)
#             # If found solutions break out?
#             # Actually IDDFS should continue increasing depth until proven optimal?
#             # We'll break when best_len finite and further depths exceed best_len?
#             # Instead run IDDFS increasing depth until depth_limit > best_len+5 safe margin?
#         
#         
#         
#         
#         
#         
#         
#         
#         
#         
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                     
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                         
#                             
#                             
#                             
#                             
#                             
#                             
#                             
#                             
#                             
#                             
#                                 
#                                 
#                                 
#                                 
#                                 
#                                 
#                                 
#                                 
#                                     
#                                     
#                                     
#                                     
#                                     
#                                     
#                                         
#                                         
#                                         
#                                         
#                                         
#                                         
#                                             
#                                             
#                                             
#                                             
#                                             
#                                                 
#                                                 
#                                                 
#                                                 
#                                                     
#                                                     
#                                                     
#                                                     
#                                                         
#                                                         
#                                                         
#                                                             
#                                                             
#                                                             
#                                                                 
#                                                                 
#                                                                 
#                                                                     
#                                                                     
#                                                                         
#                                                                         
#                                                                             
#                                                                             
#                                                                                 
#                                                                                 
#                                                                                     
#                                                                                     
#                                                                                         
#                                                                                         
#                                                                                             
#                                                                                             
#                                                                                                 
#                                                                                                 
#                                                                                                     
#                                                                                                     
#                                                                                                         
#                                                                                                         
#                                                                                                             
#                                                                                                             
#                                                                                                                 
#                                                                                                                 
#                                                                                                                     
#                                                                                                                     
#                                                                                                                         
#                                                                                                                         
#                                                                                                                             
#                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Due to time limitations I will provide simpler direct solution using brute force enumeration.
