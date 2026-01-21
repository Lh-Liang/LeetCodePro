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
        long long maxVal = 0;
        
        // Try all possible partitions
        for (int maskA = 0; maskA < (1 << n); maskA++) {
            int remaining = ((1 << n) - 1) ^ maskA;
            
            // Iterate through all subsets of remaining
            for (int maskB = remaining; ; maskB = (maskB - 1) & remaining) {
                int maskC = remaining ^ maskB;
                
                // Calculate XOR(A)
                long long xorA = 0;
                for (int i = 0; i < n; i++) {
                    if (maskA & (1 << i)) {
                        xorA ^= nums[i];
                    }
                }
                
                // Calculate AND(B)
                long long andB = 0;
                bool firstB = true;
                for (int i = 0; i < n; i++) {
                    if (maskB & (1 << i)) {
                        if (firstB) {
                            andB = nums[i];
                            firstB = false;
                        } else {
                            andB &= nums[i];
                        }
                    }
                }
                
                // Calculate XOR(C)
                long long xorC = 0;
                for (int i = 0; i < n; i++) {
                    if (maskC & (1 << i)) {
                        xorC ^= nums[i];
                    }
                }
                
                maxVal = max(maxVal, xorA + andB + xorC);
                
                if (maskB == 0) break;
            }
        }
        
        return maxVal;
    }
};
# @lc code=end