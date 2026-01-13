#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        # Special case: depth(1) = 0, and no other positive integer has depth 0.
        if k == 0:
            return 1  # since n >= 1

        # Max bits needed: n <= 1e15 < 2^50, but keep some margin.
        MAXB = 64

        # Precompute combinations C[n][r] for 0 <= n,r <= MAXB.
        C = [[0] * (MAXB + 1) for _ in range(MAXB + 1)]
        for i in range(MAXB + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                if j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

        def popcount(x: int) -> int:
            return x.bit_count()

        # Precompute depth for values up to MAXB.
        depth = [0] * (MAXB + 1)
        depth[1] = 0
        for v in range(2, MAXB + 1):
            depth[v] = 1 + depth[popcount(v)]

        # Count numbers in [0, n] with exactly `ones` set bits.
        def count_leq(nval: int, ones: int) -> int:
            if ones < 0:
                return 0
            bits = list(map(int, bin(nval)[2:]))  # MSB -> LSB
            m = len(bits)
            res = 0
            c = ones
            for i, b in enumerate(bits):
                rem = m - i - 1
                if b == 1:
                    if c <= rem:
                        res += C[rem][c]
                    c -= 1
                    if c < 0:
                        break
            else:
                # If we matched all bits and used exactly `ones` ones
                if c == 0:
                    res += 1
            return res

        # For k >= 1: sum over popcount c such that depth(c) == k-1.
        target = k - 1
        max_ones = n.bit_length()  # maximum possible popcount for numbers <= n
        ans = 0
        for c in range(1, max_ones + 1):
            if depth[c] == target:
                ans += count_leq(n, c)

        # Remove x=1 when k=1, because it has depth 0 but popcount 1.
        if k == 1 and n >= 1:
            ans -= 1

        return ans
# @lc code=end
