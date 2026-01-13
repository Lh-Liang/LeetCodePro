#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

from typing import List

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        bits = [1 if c == '1' else 0 for c in s]
        total_ones = sum(bits)

        INF = 10**9
        # Node tuple layout:
        # (len, rc,
        #  pref_c1, pref_l1, pref_c2, pref_l2,
        #  suf_c1,  suf_l1,  suf_c2,  suf_l2,
        #  maxZero, minSurOne, maxAdj)
        EMPTY = (0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, INF, 0)

        def leaf(bit: int):
            mz = 1 if bit == 0 else 0
            return (1, 1, bit, 1, -1, 0, bit, 1, -1, 0, mz, INF, 0)

        def merge(A, B):
            if A[0] == 0:
                return B
            if B[0] == 0:
                return A

            (lenA, rcA, apc1, apl1, apc2, apl2, asc1, asl1, asc2, asl2, amaxZ, amin1, amaxAdj) = A
            (lenB, rcB, bpc1, bpl1, bpc2, bpl2, bsc1, bsl1, bsc2, bsl2, bmaxZ, bmin1, bmaxAdj) = B

            # maxZero
            crossZ = 0
            if asc1 == 0 and bpc1 == 0:
                crossZ = asl1 + bpl1
            maxZero = amaxZ
            if bmaxZ > maxZero:
                maxZero = bmaxZ
            if crossZ > maxZero:
                maxZero = crossZ

            # internal surrounded-one stats
            minSur = amin1 if amin1 < bmin1 else bmin1
            maxAdj = amaxAdj if amaxAdj > bmaxAdj else bmaxAdj

            # Cross-boundary candidates:
            # Case A: [0-run][1-run] | [0-run]
            if asc1 == 1 and bpc1 == 0 and rcA >= 2 and asc2 == 0:
                b_len = asl1
                adj_sum = asl2 + bpl1
                if b_len < minSur:
                    minSur = b_len
                if adj_sum > maxAdj:
                    maxAdj = adj_sum

            # Case B: [0-run] | [1-run][0-run]
            if asc1 == 0 and bpc1 == 1 and rcB >= 2 and bpc2 == 0:
                b_len = bpl1
                adj_sum = asl1 + bpl2
                if b_len < minSur:
                    minSur = b_len
                if adj_sum > maxAdj:
                    maxAdj = adj_sum

            # Case C: [0-run][1-run] | [1-run][0-run] (merged 1-run)
            if asc1 == 1 and bpc1 == 1 and rcA >= 2 and rcB >= 2 and asc2 == 0 and bpc2 == 0:
                b_len = asl1 + bpl1
                adj_sum = asl2 + bpl2
                if b_len < minSur:
                    minSur = b_len
                if adj_sum > maxAdj:
                    maxAdj = adj_sum

            # run count capped at 3
            if rcA == 3 or rcB == 3:
                rc = 3
            else:
                runs = rcA + rcB
                if asc1 == bpc1:
                    runs -= 1
                rc = 3 if runs >= 3 else runs

            totalLen = lenA + lenB

            # prefix: first two runs
            if rcA == 3:
                pref_c1, pref_l1, pref_c2, pref_l2 = apc1, apl1, apc2, apl2
            elif rcA == 2:
                pref_c1, pref_l1 = apc1, apl1
                pref_c2, pref_l2 = apc2, apl2 + (bpl1 if bpc1 == apc2 else 0)
            else:  # rcA == 1
                pref_c1 = apc1
                pref_l1 = lenA + (bpl1 if bpc1 == apc1 else 0)
                if bpc1 == apc1:
                    if rcB >= 2:
                        pref_c2, pref_l2 = bpc2, bpl2
                    else:
                        pref_c2, pref_l2 = -1, 0
                else:
                    pref_c2, pref_l2 = bpc1, bpl1

            # suffix: last two runs (stored as last run then second last)
            if rcB == 3:
                suf_c1, suf_l1, suf_c2, suf_l2 = bsc1, bsl1, bsc2, bsl2
            elif rcB == 2:
                suf_c1, suf_l1 = bsc1, bsl1
                suf_c2, suf_l2 = bsc2, bsl2 + (asl1 if asc1 == bsc2 else 0)
            else:  # rcB == 1
                suf_c1 = bsc1
                suf_l1 = lenB + (asl1 if asc1 == bsc1 else 0)
                if asc1 == bsc1:
                    if rcA >= 2:
                        suf_c2, suf_l2 = asc2, asl2
                    else:
                        suf_c2, suf_l2 = -1, 0
                else:
                    suf_c2, suf_l2 = asc1, asl1

            # If combined is a single run, normalize pref/suf second runs to -1
            if rc == 1:
                pref_c2, pref_l2 = -1, 0
                suf_c2, suf_l2 = -1, 0
                # ensure lengths match totalLen
                pref_l1 = totalLen
                suf_l1 = totalLen

            return (
                totalLen, rc,
                pref_c1, pref_l1, pref_c2, pref_l2,
                suf_c1, suf_l1, suf_c2, suf_l2,
                maxZero, minSur, maxAdj
            )

        # Build iterative segtree
        size = 1
        while size < n:
            size <<= 1
        tree = [EMPTY] * (2 * size)
        for i in range(n):
            tree[size + i] = leaf(bits[i])
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def query(l: int, r: int):
            l += size
            r += size
            leftRes = EMPTY
            rightRes = EMPTY
            while l <= r:
                if l & 1:
                    leftRes = merge(leftRes, tree[l])
                    l += 1
                if not (r & 1):
                    rightRes = merge(tree[r], rightRes)
                    r -= 1
                l >>= 1
                r >>= 1
            return merge(leftRes, rightRes)

        ans = []
        for l, r in queries:
            node = query(l, r)
            minSurOne = node[11]
            if minSurOne >= INF:
                gain = 0
            else:
                maxZeroLen = node[10]
                maxAdjSum = node[12]
                gain = max(maxZeroLen - minSurOne, maxAdjSum)
            ans.append(total_ones + gain)
        return ans
# @lc code=end
