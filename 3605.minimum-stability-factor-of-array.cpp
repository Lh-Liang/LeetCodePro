#
# @lc app=leetcode id=3605 lang=cpp
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
class Solution {
public:
    // Function to calculate HCF using Euclid's Algorithm
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    
    // Function to calculate HCF of an array segment
    int arrayGCD(vector<int>& nums, int start, int end) {
        int result = nums[start];
        for (int i = start + 1; i <= end; ++i) {
            result = gcd(result, nums[i]);
            if (result < 2) return result; // Early exit if GCD < 2
        }
        return result;
    }
    
    int minStable(vector<int>& nums, int maxC) {
        int n = nums.size();
        // Step 1: Find the initial longest stable subarray using sliding window
        // Initialize variables for sliding window and stability factor calculation
        int left = 0, right = 0;
        int minStabilityFactor = n; // Start with max possible length
        while (right < n) {
            if (arrayGCD(nums, left, right) >= 2) {
                minStabilityFactor = std::min(minStabilityFactor, right - left + 1);
                left++;
            } else {
                right++;
            }
        }
        
        // Step 2: Consider modifications if maxC > 0 (not implemented in detail)
        // Implement logic for modifying elements and recalculating minStabilityFactor here...
        
        return minStabilityFactor;
    }
};
# @lc code=end