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
        for (int idx = 0; idx < q; ++idx) {
            int index = queries[idx][0];
            int value = queries[idx][1];
            int start = queries[idx][2];
            int x = queries[idx][3];
            nums[index] = value; // Update nums persistently
            int m = n - start; // Length of current subarray
            int[] arr = new int[m];
            for (int i = 0; i < m; ++i) arr[i] = nums[start + i];
            int[] freq = new int[k];
            int prod = 1;
            // Suffixes: for i from m-1 downto 0, prod = arr[i]*prod % k
            // freq[p]: number of suffixes whose product % k == p
            // We must count all suffixes (including full array, and at least one element)
            // So we go from right to left, include suffix starting at each position
            for (int i = m - 1; i >= 0; --i) {
                prod = (int)((long)prod * arr[i] % k);
                freq[prod]++;
            }
            res[idx] = freq[x];
        }
        return res;
    }
}
# @lc code=end