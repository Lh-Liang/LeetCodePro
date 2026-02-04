#
# @lc app=leetcode id=3630 lang=cpp
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
#include <climits>
using namespace std;

class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        long long maxResult = LLONG_MIN;
        
        // Iterate over all possible partitions (3^n possibilities)
        int totalPartitions = 1 << (2 * n); // Since each element has 3 choices: A, B, C
        for (int mask = 0; mask < totalPartitions; ++mask) {
            vector<int> A, B, C;
            int tempMask = mask;
            
            // Distribute numbers based on current mask
            for (int i = 0; i < n; ++i) {
                int choice = tempMask % 3;
                tempMask /= 3;
                if (choice == 0) A.push_back(nums[i]);
                else if (choice == 1) B.push_back(nums[i]);
                else C.push_back(nums[i]);
            }

            // Calculate XOR(A), AND(B), XOR(C)
            long long xorA = accumulate(A.begin(), A.end(), 0LL, bit_xor<int>());
            long long andB = B.empty() ? 0 : accumulate(B.begin(), B.end(), ~0LL, bit_and<int>());
            long long xorC = accumulate(C.begin(), C.end(), 0LL, bit_xor<int>());

            // Update maximum result
            maxResult = max(maxResult, xorA + andB + xorC);
        }
        return maxResult;
    }
}; 
# @lc code=end