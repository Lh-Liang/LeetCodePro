#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        const long long MOD = 1e9 + 7, BASE = 911;
        unordered_set<long long> hashes;
        for (int i = 0; i < n; ++i) {
            long long hash = 0;
            for (int j = i; j < n; ++j) {
                hash = (hash * BASE + nums[j]) % MOD;
                long long sum = prefix[j + 1] - prefix[i];
                if (sum % k == 0) {
                    hashes.insert(hash);
                }
            }
        }
        return hashes.size();
    }
};
# @lc code=end