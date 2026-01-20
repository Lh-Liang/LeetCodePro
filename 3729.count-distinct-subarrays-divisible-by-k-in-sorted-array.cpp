#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
#include <vector>
#include <unordered_map>
#include <numeric>

using namespace std;

class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long totalGood = 0;
        unordered_map<long long, long long> prefixCounts;
        prefixCounts[0] = 1;
        long long currentSum = 0;
        
        // Step 1: Calculate total good subarrays using prefix sums modulo k
        for (int x : nums) {
            currentSum = (currentSum + x) % k;
            totalGood += prefixCounts[currentSum];
            prefixCounts[currentSum]++;
        }

        long long goodSame = 0;
        long long distinctSame = 0;

        // Step 2: Identify blocks of identical values to handle distinctness
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums[j] == nums[i]) {
                j++;
            }
            
            long long c = j - i;
            long long v = nums[i];
            
            // Condition: (L * v) % k == 0 => L is a multiple of m = k / gcd(v, k)
            long long m = (long long)k / std::gcd(v, (long long)k);
            long long X = c / m; // Number of distinct lengths L that work
            
            if (X > 0) {
                // Number of actual subarrays (i, j) in this block that are good
                // Sum of (c - L + 1) for L = m, 2m, ..., Xm
                // = X(c + 1) - m * (1 + 2 + ... + X)
                goodSame += X * (c + 1) - m * (X * (X + 1) / 2);
                // Number of distinct sequences of value v that are good
                distinctSame += X;
            }
            
            i = j;
        }

        // Result: Total good - (non-distinct same-value good) + (distinct same-value good)
        return totalGood - goodSame + distinctSame;
    }
};
# @lc code=end