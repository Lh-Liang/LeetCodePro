#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        import math

        class SegTree:
            def __init__(self, n):
                self.N = 1
                while self.N < n:
                    self.N <<= 1
                self.tree = [math.inf] * (self.N * 2)

            def update(self, pos, val):
                idx = pos + self.N
                self.tree[idx] = min(self.tree[idx], val)
                idx >>= 1
                while idx:
                    self.tree[idx] = min(self.tree[idx * 2], self.tree[idx * 2 + 1])
                    idx >>= 1

            def query(self, l, r):
                l += self.N
                r += self.N
                res = math.inf
                while l <= r:
                    if l & 1:
                        res = min(res, self.tree[l])
                        l += 1
                    if not r & 1:
                        res = min(res, self.tree[r])
                        r -= 1
                    l >>= 1
                    r >>= 1
                return res

        n = len(s)
        ans = -math.inf

        # All possible digits are '0'-'4'
        digits = [chr(ord('0') + d) for d in range(5)]

        for a in digits:
            for b in digits:
                if a == b:
                    continue

                # Prefix sums for characters a and b
                A = [0] * (n + 1)
                B = [0] * (n + 1)
                cntA = cntB = 0
                for idx, ch in enumerate(s):
                    cntA += ch == a
                    cntB += ch == b
                    A[idx + 1] = cntA
                    B[idx + 1] = cntB

                diff_arr = [A[i] - B[i] for i in range(n + 1)]

                # Four segment trees indexed by parity of A[i], B[i]
                segs = [[SegTree(n + 5) for _ in range(2)] for _ in range(2)]

                # Iterate over ending prefix index
                for end in range(k, n + 1):
                    start_idx = end - k          # smallest allowed starting prefix index
                    
                    # Add start_idx into data structures
                    Ai_start = A[start_idx]
                    Bi_start = B[start_idx]
                    parA_start = Ai_start & 1
                    parB_start = Bi_start & 1
                    d_start = diff_arr[start_idx]
                    segs[parA_start][parB_start].update(Bi_start, d_start)

                    Aj_end = A[end]
                    Bj_end = B[end]
                    parA_end = Aj_end & 1
                    parB_end = Bj_end & 1

                    req_parA = parA_end ^ 1      # opposite parity
                    req_parB = parB_end          # same parity

                    Pmax = Bj_end - 2             # need B[end]-B[start] >= 2
                    if Pmax >= 0:
                        mmin = segs[req_parA][req_parB].query(0, Pmax)
                        if mmin != math.inf:
                            cand = diff_arr[end] - mmin
                            ans = max(ans, cand)

        return int(ans)
# @lc code=end