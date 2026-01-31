# 
# @lc app=leetcode id=3748 lang=cpp
# 
# [3748] Count Stable Subarrays
# 

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        if (n == 0) return {};

        // pos[i] is the starting index of the maximal non-decreasing subarray ending at i.
        vector<int> pos(n);
        pos[0] = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] >= nums[i - 1]) {
                pos[i] = pos[i - 1];
            } else {
                pos[i] = i;
            }
        }

        // prefix_sum_pos[i] stores the sum of pos[0...i-1]
        vector<long long> prefix_sum_pos(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix_sum_pos[i + 1] = prefix_sum_pos[i] + pos[i];
        }

        int q = queries.size();
        vector<long long> ans(q);
        for (int k = 0; k < q; ++k) {
            int li = queries[k][0];
            int ri = queries[k][1];

            // Total stable subarrays = sum_{j=li}^{ri} (j + 1 - max(li, pos[j]))
            long long count = (long long)ri - li + 1;
            long long sum_j_plus_1 = count * (li + ri + 2) / 2;

            // Find m such that pos[m] >= li. Since pos is non-decreasing, we use binary search.
            auto it = lower_bound(pos.begin() + li, pos.begin() + ri + 1, li);
            int m = (int)(it - pos.begin());

            // sum_{j=li}^{ri} max(li, pos[j]) = sum_{j=li}^{m-1} li + sum_{j=m}^{ri} pos[j]
            long long sum_max = (long long)(m - li) * li + (prefix_sum_pos[ri + 1] - prefix_sum_pos[m]);

            ans[k] = sum_j_plus_1 - sum_max;
        }

        return ans;
    }
};
# @lc code=end