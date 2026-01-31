#
# @lc app=leetcode id=3739 lang=cpp
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        // The condition count(target) > length / 2 is equivalent to 
        // count(target) > count(others).
        // Assign 1 to target elements and -1 to others.
        // Subarray sum > 0 <=> P[j+1] > P[i].
        
        // Prefix sums range from -n to n. 
        vector<int> freq(2 * n + 1, 0);
        int offset = n;
        int curr_P = 0;
        
        // P[0] = 0
        freq[offset + curr_P] = 1;
        
        long long count_smaller = 0; 
        long long result = 0;
        
        for (int x : nums) {
            if (x == target) {
                // curr_P increases: P[k] = P[k-1] + 1.
                // New count_smaller = count of P[i] < P[k-1] + count of P[i] == P[k-1].
                count_smaller += freq[offset + curr_P];
                curr_P++;
            } else {
                // curr_P decreases: P[k] = P[k-1] - 1.
                // New count_smaller = count of P[i] < P[k-1] - count of P[i] == P[k-1] - 1.
                curr_P--;
                count_smaller -= freq[offset + curr_P];
            }
            result += count_smaller;
            freq[offset + curr_P]++;
        }
        
        return result;
    }
};
# @lc code=end