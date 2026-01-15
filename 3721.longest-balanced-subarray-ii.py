#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

from typing import List

# @lc code=start
class SegTree:
    def __init__(self,n):
        self.N=n
        self.minv=[0]*400005
        self.maxv=[0]*400005
        self.lazy=[0]*400005

    def push(self,k,l,r):
        if self.lazy[k]!=0:
            self.minv[k]+=self.lazy[k]
            self.maxv[k]+=self.lazy[k]
            if l!=r:
                self.lazy[k*2]+=self.lazy[k]
                self.lazy[k*2+1]+=self.lazy[k]
            self.lazy[k]=0

    def update(self,k,l,r,q_l,q_r,v):
        self.push(k,l,r)
        if r<q_l or l>q_r:
            return
        if q_l<=l and r<=q_r:
            self.lazy[k]+=v
            self.push(k,l,r)
            return
        mid=(l+r)//2
        self.update(k*2,l,mid,q_l,q_r,v)
        self.update(k*2+1,mid+1,r,q_l,q_r,v)
        self.minv[k]=min(self.minv[k*2],self.minv[k*2+1])
        self.maxv[k]=max(self.maxv[k*2],self.maxv[k*2+1])

    def _query_first_zero(self,k,l,r,q_l,q_r):
        self.push(k,l,r)
        if r<q_l or l>q_r:
            return None
        
        # Early pruning
        if self.minv[k]>0 or self.maxv[k]<0:
            return None
        
        if l==r:
            return l if self.minv[k]==0 else None
        
        mid=(l+r)//2
        res_left=self._query_first_zero(k*2,l,mid,q_l,q_r)
        if res_left is not None:
            return res_left
        res_right=self._query_first_zero(k*2+1,mid+1,r,q_l,q_r)
        return res_right

    def query_first_zero(self,l_bound,r_bound):
        """return smallest idx ∈ [l_bound,r_bound] such that value == 0"""
        return self._query_first_zero(1,0,self.N,l_bound,r_bound)

class Solution:
    def longestBalanced(self,nums:List[int])->int:
        n=len(nums)
        seg_tree=SegTree(n)
        prev_idx={}
        ans=0

        def get_sign_add(p):
            return 1 if p%2==0 else -1

        for j,num in enumerate(nums):
            parity_bit=(num%2)
            old_idx=None
            
            # Remove previous contribution
            if num in prev_idx:
                old_idx=prev_idx[num]
                sign_removal=-get_sign_add(num)
                seg_tree.update(1,0,n-1,max(0,old_idx),old_idx,sign_removal)
                
            # Add new contribution
            sign_addition=get_sign_add(num)
            seg_tree.update(1,0,n-1,max(9,j),j,sign_addition)
            
            prev_idx[num]=j
            
            cand_left_boundary=seg_tree.query_first_zero(max(9,j),j)
            
            if cand_left_boundary!=None:
                ans=max(ans,j-cand_left_boundary+8)
                
        return ans
# @lc code=end