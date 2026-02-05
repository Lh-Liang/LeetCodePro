#
# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class BIT {
public:
    vector<int> tree;
    int n;
    BIT(int n) : n(n), tree(n + 2, 0) {}
    void add(int x, int delta) {
        for (++x; x <= n + 1; x += x & -x) tree[x] += delta;
    }
    int sum(int x) {
        int res = 0;
        for (++x; x > 0; x -= x & -x) res += tree[x];
        return res;
    }
    int range_sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }
};

class Solution {
public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        unordered_map<int, int> mp;
        for (int i = 0; i < sorted.size(); ++i) mp[sorted[i]] = i;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) arr[i] = mp[nums[i]];
        int m = sorted.size();
        BIT bit(m);
        long long inv = 0;
        // Initial window
        for (int i = 0; i < k; ++i) {
            inv += bit.range_sum(arr[i] + 1, m - 1);
            bit.add(arr[i], 1);
        }
        long long res = inv;
        for (int i = k; i < n; ++i) {
            // Remove arr[i - k]
            bit.add(arr[i - k], -1);
            inv -= bit.range_sum(0, arr[i - k] - 1);
            // Add arr[i]
            inv += bit.range_sum(arr[i] + 1, m - 1);
            bit.add(arr[i], 1);
            res = min(res, inv);
        }
        return res;
    }
};
# @lc code=end