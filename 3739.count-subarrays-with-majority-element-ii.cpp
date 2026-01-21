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
        vector<int> P(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            P[i] = P[i - 1] + (nums[i - 1] == target ? 1 : -1);
        }
        int OFFSET = n;
        int MAXV = 2 * n + 2;
        vector<long long> tree(MAXV + 1, 0);
        auto update = [&](int idx, long long val) {
            while (idx <= MAXV) {
                tree[idx] += val;
                idx += idx & -idx;
            }
        };
        auto query = [&](int idx) -> long long {
            long long sum = 0;
            while (idx > 0) {
                sum += tree[idx];
                idx -= idx & -idx;
            }
            return sum;
        };
        long long ans = 0;
        int idx0 = P[0] + OFFSET + 1;
        update(idx0, 1);
        for (int r = 1; r <= n; ++r) {
            int tidx = P[r] + OFFSET + 1;
            long long cnt = query(tidx - 1);
            ans += cnt;
            update(tidx, 1);
        }
        return ans;
    }
};
# @lc code=end