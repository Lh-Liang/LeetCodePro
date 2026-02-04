#
# @lc app=leetcode id=3739 lang=cpp
#
# [3739] Count Subarrays With Majority Element II
#
# @lc code=start
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i] = (nums[i] == target) ? 1 : -1;
        }
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i+1] = prefix[i] + arr[i];
        }
        // For prefix sums, we want for subarray [l, r]:
        // prefix[r+1] - prefix[l] > 0 => prefix[l] < prefix[r+1]
        // Count for each r+1, the number of prefix[l] < prefix[r+1] (l in [0, r+1))
        vector<long long> all_vals = prefix;
        sort(all_vals.begin(), all_vals.end());
        all_vals.erase(unique(all_vals.begin(), all_vals.end()), all_vals.end());
        int m = all_vals.size();
        vector<int> bit(m + 2, 0);
        auto add = [&](int idx) {
            for (++idx; idx < bit.size(); idx += idx & -idx) ++bit[idx];
        };
        auto sum = [&](int idx) {
            int res = 0;
            for (++idx; idx > 0; idx -= idx & -idx) res += bit[idx];
            return res;
        };
        long long ans = 0;
        for (int i = 0; i < prefix.size(); ++i) {
            int idx = lower_bound(all_vals.begin(), all_vals.end(), prefix[i]) - all_vals.begin();
            if (i > 0) {
                ans += sum(idx - 1);
            }
            add(idx);
        }
        return ans;
    }
};
# @lc code=end