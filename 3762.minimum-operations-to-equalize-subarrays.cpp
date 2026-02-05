#
# @lc app=leetcode id=3762 lang=cpp
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<long long> ans;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            vector<int> sub;
            for (int i = l; i <= r; ++i) sub.push_back(nums[i]);
            int rem = sub[0] % k;
            bool possible = true;
            for (int x : sub) {
                if (x % k != rem) {
                    possible = false;
                    break;
                }
            }
            if (!possible) {
                ans.push_back(-1);
                continue;
            }
            vector<long long> vals;
            for (int x : sub) vals.push_back((x - rem) / k);
            sort(vals.begin(), vals.end());
            long long median = vals[vals.size() / 2];
            long long ops = 0;
            for (long long v : vals) ops += abs(v - median);
            ans.push_back(ops);
        }
        return ans;
    }
};
# @lc code=end