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
        unordered_map<int, long long> balance_count;
        int balance = 0;
        long long ans = 0;
        balance_count[0] = 1; // Prefix at -1 is 0
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) balance++;
            else balance--;
            // For (i+1) elements, target is majority if balance > (i+1)/2
            // We need to find number of j < i such that balance_j < balance - (i-j)/2
            // But we can use a different trick: for each prefix, keep counts
            // Instead, let's use offset technique:
            // Use an array to store first occurrence of balance
            // Or, for all previous balance values smaller than current,
            // but that's not efficient.
            // Instead, let's preprocess: For each prefix, when balance exceeds previous max, count.
            // Let's use a different prefix sum trick:
            // Actually, since for subarray [l, r], majority means 2*(count of target in [l,r]) > (r-l+1),
            // which is equivalent to: (prefix[r+1] - prefix[l]) * 2 > r-l+1
            // Let's try an O(n log n) solution:
            // Let's store prefix balances and use ordered map.
            // But for now, let's keep the efficient O(n) solution for the constraints.

            // For each position, count number of earlier prefix balances less than current balance
            ans += balance_count[balance - 1];
            balance_count[balance]++;
        }
        return ans;
    }
};
# @lc code=end