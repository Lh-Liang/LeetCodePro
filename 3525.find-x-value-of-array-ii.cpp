#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> res;
        // We will keep nums updated throughout queries
        for (auto& q : queries) {
            int idx = q[0], val = q[1], start = q[2], xi = q[3];
            nums[idx] = val; // apply persistent update
            vector<int> arr(nums.begin() + start, nums.end());
            int m = arr.size();
            // Suffix product modulo k
            vector<int> suffix_prod(m + 1, 1);
            for (int i = m - 1; i >= 0; --i) {
                suffix_prod[i] = (1LL * arr[i] * suffix_prod[i + 1]) % k;
            }
            // For each possible suffix removal, i.e., arr[0..j], where j = 0..m-1
            // The product is prod(arr[0] * ... * arr[j]) = suffix_prod[0] / suffix_prod[j+1] (modulo k)
            // But division is not always possible in modular arithmetic, but since k is small, we can brute-force
            // Instead, accumulate prefix product modulo k from left to right, and for each possible suffix, check if the prefix product equals xi
            int prefix = 1, count = 0;
            for (int i = 0; i < m; ++i) {
                if (prefix == xi) count++;
                prefix = (1LL * prefix * arr[i]) % k;
            }
            // Also consider keeping the whole array (no suffix removed)
            if (prefix == xi) count++;
            res.push_back(count);
        }
        return res;
    }
};
# @lc code=end