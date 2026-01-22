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
        long long maxResult = 0;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            // Compute AND of elements in B (set bits in mask)
            long long andB = 0;
            if (mask != 0) {
                andB = ~0LL;  // All 1s
                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        andB &= nums[i];
                    }
                }
            }
            
            // Compute XOR of remaining elements and build XOR basis
            long long X = 0;
            long long basis[31] = {};
            for (int i = 0; i < n; i++) {
                if (!(mask & (1 << i))) {
                    X ^= nums[i];
                    long long cur = nums[i];
                    for (int b = 30; b >= 0; b--) {
                        if (!(cur >> b & 1)) continue;
                        if (!basis[b]) {
                            basis[b] = cur;
                            break;
                        }
                        cur ^= basis[b];
                    }
                }
            }
            
            // Maximize (a & M) where M = ~X (in relevant bits)
            // We want to maximize XOR(A) + XOR(C) = X + 2*(a & ~X)
            long long M = ((1LL << 31) - 1) ^ X;
            long long a = 0;
            for (int b = 30; b >= 0; b--) {
                if (basis[b] && ((a ^ basis[b]) & M) > (a & M)) {
                    a ^= basis[b];
                }
            }
            
            long long xorSum = X + 2 * (a & M);
            maxResult = max(maxResult, andB + xorSum);
        }
        
        return maxResult;
    }
};
# @lc code=end