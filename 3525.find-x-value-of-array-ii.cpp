#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#
# @lc code=start
class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<int> results;
        int n = nums.size();
        
        // Precompute prefix products modulo k
        vector<int> prefixProducts(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            prefixProducts[i] = (prefixProducts[i - 1] * nums[i - 1]) % k;
        }
        
        for (auto& query : queries) {
            int index = query[0];
            int value = query[1];
            int start = query[2];
            int x_value = query[3];
            
            // Update nums with new value at specified index and recompute prefix product if needed
            if (nums[index] != value) {
                nums[index] = value;
                for (int i = index + 1; i <= n; ++i) {
                    prefixProducts[i] = (prefixProducts[i - 1] * nums[i - 1]) % k;
                }
            }
            
            // Calculate x-value after removing prefix up to 'start'.
            long long product_mod_k = prefixProducts[start];
            int count_x_value = 0;
            for (int i = start; i < n; ++i) {
                long long suffix_product_mod_k = (prefixProducts[n] / prefixProducts[i]) % k;
                if (suffix_product_mod_k == x_value) {
                    count_x_value++;
                }
                product_mod_k = (product_mod_k * nums[i]) % k;
            }
            results.push_back(count_x_value);
        }
        return results;
    }
};
# @lc code=end