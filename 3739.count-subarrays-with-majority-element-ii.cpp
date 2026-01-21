#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3739 lang=cpp
 *
 * [3739] Count Subarrays With Majority Element II
 */

// @lc code=start
class Solution {
    struct Fenwick {
        int n;
        vector<long long> bit;
        Fenwick(int n = 0) : n(n), bit(n + 1, 0) {}
        void add(int i, long long v) {
            for (; i <= n; i += i & -i) bit[i] += v;
        }
        long long sumPrefix(int i) const {
            long long s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
    };

public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = (int)nums.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; i++) {
            int v = (nums[i] == target) ? 1 : -1;
            pref[i + 1] = pref[i] + v;
        }

        // Coordinate compress prefix sums
        vector<int> xs = pref;
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        auto getId = [&](int x) {
            return (int)(lower_bound(xs.begin(), xs.end(), x) - xs.begin()) + 1; // 1-based
        };

        Fenwick fw((int)xs.size());
        long long ans = 0;

        // Insert pref[0]
        fw.add(getId(pref[0]), 1);

        for (int j = 1; j <= n; j++) {
            int id = getId(pref[j]);
            // count previous prefix sums strictly less than current
            ans += fw.sumPrefix(id - 1);
            fw.add(id, 1);
        }
        return ans;
    }
};
// @lc code=end
