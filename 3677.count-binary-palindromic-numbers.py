#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1  # only "0"

        def rev_bits(x: int, bits: int) -> int:
            r = 0
            for _ in range(bits):
                r = (r << 1) | (x & 1)
                x >>= 1
            return r

        def make_pal(x: int, L: int) -> int:
            # x encodes the first half (including the leading 1)
            if L % 2 == 0:
                half = L // 2
                return (x << half) | rev_bits(x, half)
            else:
                half = (L + 1) // 2
                return (x << (half - 1)) | rev_bits(x >> 1, half - 1)

        ans = 1  # count k=0
        bl = n.bit_length()

        # Count all palindromes with length < bl
        for L in range(1, bl):
            half = (L + 1) // 2
            ans += 1 << (half - 1)

        # Count palindromes with length == bl
        L = bl
        half = (L + 1) // 2
        start = 1 << (half - 1)
        prefix = n >> (L - half)  # top 'half' bits

        cnt = prefix - start
        if cnt < 0:
            cnt = 0

        if prefix >= start:
            pal = make_pal(prefix, L)
            if pal <= n:
                cnt += 1

        ans += cnt
        return ans
# @lc code=end
