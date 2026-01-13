#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List
from array import array

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        if k <= 0:
            return [0] * len(queries)

        # Build iterative segment tree
        size = 1
        while size < n:
            size <<= 1

        prods = [0] * (2 * size)  # product modulo k
        pref = array('I', [0]) * (2 * size * k)  # flat: pref[node*k + r]

        def _set_leaf(pos: int, val: int) -> None:
            i = pos + size
            p = val % k
            prods[i] = p
            base = i * k
            for r in range(k):
                pref[base + r] = 0
            pref[base + p] = 1

        def _pull(i: int) -> None:
            # merge children (2*i) then (2*i+1) into i
            left = 2 * i
            right = left + 1
            prodA = prods[left]
            prodB = prods[right]
            prods[i] = (prodA * prodB) % k

            baseA = left * k
            baseB = right * k
            tmp = [0] * k
            # prefixes entirely in A
            for r in range(k):
                tmp[r] = pref[baseA + r]
            # prefixes that include all A and some prefix of B
            for r in range(k):
                cnt = pref[baseB + r]
                if cnt:
                    tmp[(prodA * r) % k] += cnt

            baseC = i * k
            for r in range(k):
                pref[baseC + r] = tmp[r]

        # initialize leaves
        for i, v in enumerate(nums):
            _set_leaf(i, v)
        # build
        for i in range(size - 1, 0, -1):
            _pull(i)

        def update(pos: int, val: int) -> None:
            _set_leaf(pos, val)
            i = (pos + size) // 2
            while i:
                _pull(i)
                i //= 2

        def merge_node(A_prod: int, A_pref: List[int], B_prod: int, B_pref: List[int]):
            prodC = (A_prod * B_prod) % k
            tmp = A_pref[:]  # k is tiny
            for r in range(k):
                cnt = B_pref[r]
                if cnt:
                    tmp[(A_prod * r) % k] += cnt
            return prodC, tmp

        def get_node(i: int):
            base = i * k
            return prods[i], [pref[base + r] for r in range(k)]

        def query(l: int, r: int):
            # returns node info for nums[l:r] (contiguous)
            # identity: empty segment
            id_prod = 1 % k
            left_prod, left_pref = id_prod, [0] * k
            right_prod, right_pref = id_prod, [0] * k

            l += size
            r += size
            while l < r:
                if l & 1:
                    p, pc = get_node(l)
                    left_prod, left_pref = merge_node(left_prod, left_pref, p, pc)
                    l += 1
                if r & 1:
                    r -= 1
                    p, pc = get_node(r)
                    right_prod, right_pref = merge_node(p, pc, right_prod, right_pref)
                l //= 2
                r //= 2

            return merge_node(left_prod, left_pref, right_prod, right_pref)

        ans = []
        for idx, val, start, x in queries:
            update(idx, val)
            _, pc = query(start, n)
            ans.append(pc[x])
        return ans

# @lc code=end
