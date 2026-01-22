#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#
# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        
        // Step 1: Count all good subarrays using prefix sum
        unordered_map<long long, long long> prefixCount;
        prefixCount[0] = 1;
        long long prefix = 0;
        long long totalGood = 0;
        
        for (int i = 0; i < n; i++) {
            prefix += nums[i];
            long long rem = prefix % k;
            totalGood += prefixCount[rem];
            prefixCount[rem]++;
        }
        
        // Step 2: Find runs of equal elements and compute duplicates
        long long duplicates = 0;
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && nums[j] == nums[i]) {
                j++;
            }
            // Run from index i to j-1 with value nums[i]
            long long L_run = j - i;
            long long v = nums[i];
            long long g = __gcd(v, (long long)k);
            long long step = (long long)k / g;
            if (step <= L_run) {
                long long M = L_run / step;
                duplicates += M * L_run - step * M * (M + 1) / 2;
            }
            i = j;
        }
        
        return totalGood - duplicates;
    }
};
# @lc code=end