#
# @lc app=leetcode id=3630 lang=cpp
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        long long max_value = 0;
        // Explore all possible partitions using bitmasking. Total of 3^N partitions.
        for (int mask = 0; mask < (1 << n); ++mask) {
            long long xorA = 0, xorC = 0;
            int andB = -1; // -1 indicates B is empty initially.
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) == 0) { 
                    xorA ^= nums[i]; 
                } else { 
                    if (andB == -1) { 
                        andB = nums[i]; 
                    } else { 
                        andB &= nums[i]; 
                    } 
                } 
            } 
            max_value = max(max_value, xorA + (andB == -1 ? 0 : andB) + xorC);
        }
        return max_value;
    }
};
# @lc code=end