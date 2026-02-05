#
# @lc app=leetcode id=3525 lang=java
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution {
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        int q = queries.length;
        int[] res = new int[q];
        for (int qi = 0; qi < q; ++qi) {
            int idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], xi = queries[qi][3];
            nums[idx] = val;
            int m = n - start;
            // Step 1: Get the working subarray
            // Step 2: Precompute suffix products modulo k
            // There are m possible suffixes: nums[start..n-1], nums[start+1..n-1], ..., nums[n-1..n-1]
            int[] suffixProd = new int[m + 1];
            suffixProd[m] = 1; // empty suffix (product=1)
            for (int j = m - 1; j >= 0; --j) {
                suffixProd[j] = (int)(((long)suffixProd[j + 1] * nums[start + j]) % k);
            }
            // Step 3: For each possible suffix, check if the product % k == xi
            int count = 0;
            // Only consider suffixes that leave the array non-empty.
            // i.e., suffix starting at position j in [0, m-1]
            for (int j = 0; j < m; ++j) {
                if (suffixProd[j] == xi) count++;
            }
            res[qi] = count;
        }
        return res;
    }
}
# @lc code=end