#
# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
class BIT {
public:
    vector<int> tree;
    int n;
    BIT(int sz) : n(sz), tree(sz+2, 0) {}
    void add(int i, int x) {
        for (++i; i <= n+1; i += i & -i) tree[i] += x;
    }
    int sum(int i) {
        int s = 0;
        for (++i; i > 0; i -= i & -i) s += tree[i];
        return s;
    }
    int range(int l, int r) {
        return sum(r) - sum(l-1);
    }
};
class Solution {
public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> arr = nums;
        sort(arr.begin(), arr.end());
        arr.erase(unique(arr.begin(), arr.end()), arr.end());
        vector<int> compressed(n);
        for (int i = 0; i < n; ++i) {
            compressed[i] = lower_bound(arr.begin(), arr.end(), nums[i]) - arr.begin();
        }
        int m = arr.size();
        BIT bit(m);
        long long inv = 0;
        for (int i = 0; i < k; ++i) {
            inv += bit.range(compressed[i]+1, m-1);
            bit.add(compressed[i], 1);
        }
        long long res = inv;
        for (int i = k; i < n; ++i) {
            bit.add(compressed[i-k], -1);
            inv -= bit.range(0, compressed[i-k]-1);
            inv += bit.range(compressed[i]+1, m-1);
            bit.add(compressed[i], 1);
            res = min(res, inv);
        }
        return res;
    }
};
# @lc code=end