#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#
# @lc code=start
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        const int MOD = 1e9 + 7;
        int m = mat.size();
        int n = mat[0].size();
        unordered_map<int, long long> gcd_count;
        // Initialize with first row values as potential gcds
        for (int num : mat[0]) {
            gcd_count[num]++;
        }
        // Process each subsequent row
        for (int i = 1; i < m; ++i) {
            unordered_map<int, long long> new_gcd_count;
            for (int num : mat[i]) {
                for (auto& [gcd_val, count] : gcd_count) {
                    int new_gcd = gcd(gcd_val, num);
                    new_gcd_count[new_gcd] = (new_gcd_count[new_gcd] + count) % MOD;
                }
                new_gcd_count[num] = (new_gcd_count[num] + 1) % MOD; // Count this number alone too.
            }
            gcd_count.swap(new_gcd_count); // Update with current row's results.
        }
        return gcd_count[1]; // Return number of ways to achieve gcd of 1.
    }
}; # @lc code=end