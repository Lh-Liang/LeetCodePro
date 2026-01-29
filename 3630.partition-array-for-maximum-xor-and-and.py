#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        basis = [0] * 31
        self.ans = 0

        def get_max_xor_masked(basis, mask):
            res = 0
            temp_basis = []
            for b in basis:
                if b == 0: continue
                x = b & mask
                if x == 0: continue
                for tb in temp_basis:
                    x = min(x, x ^ tb)
                if x > 0:
                    temp_basis.append(x)
                    temp_basis.sort(reverse=True)
            for tb in temp_basis:
                res = max(res, res ^ tb)
            return res

        def solve(idx, cur_and, cur_xor_v, b_count):
            if idx == n:
                val_b = cur_and if b_count > 0 else 0
                # Mask is ~cur_xor_v, limited to 30 bits
                mask = 0x3FFFFFFF ^ cur_xor_v
                max_xor_val = get_max_xor_masked(basis, mask)
                total = val_b + cur_xor_v + 2 * max_xor_val
                if total > self.ans:
                    self.ans = total
                return

            val = nums[idx]
            
            # Branch 1: Put nums[idx] in B
            new_and = val if b_count == 0 else cur_and & val
            solve(idx + 1, new_and, cur_xor_v, b_count + 1)

            # Branch 2: Put nums[idx] in V (A or C)
            # Update basis with backtracking
            x = val
            pos = -1
            for i in range(30, -1, -1):
                if (x >> i) & 1:
                    if not basis[i]:
                        basis[i] = x
                        pos = i
                        break
                    x ^= basis[i]
            
            solve(idx + 1, cur_and, cur_xor_v ^ val, b_count)
            
            if pos != -1:
                basis[pos] = 0

        solve(0, 0, 0, 0)
        return self.ans
# @lc code=end