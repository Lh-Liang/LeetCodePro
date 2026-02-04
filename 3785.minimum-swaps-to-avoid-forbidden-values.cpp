#
# @lc app=leetcode id=3785 lang=cpp
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = nums.size();
        int swaps = 0;
        unordered_map<int, int> numIndex; // To track number positions
        unordered_map<int, int> forbidIndex; // To track forbidden number positions
        
        // Initialize maps
        for (int i = 0; i < n; ++i) {
            numIndex[nums[i]] = i;
            forbidIndex[forbidden[i]] = i;
        }
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) { // Conflict exists here
                bool swapped = false;
                
                // Try finding a non-conflicting swap partner
                for (int j = 0; j < n && !swapped; ++j) {
                    if (j != i && nums[j] != forbidden[j] && nums[j] != forbidden[i]) { // Valid swap partner found 
                        swap(nums[i], nums[j]);
                        swaps++;                           swapped = true;                     }                 }                 if (!swapped) return -1; // If no valid swap partner found, return -1             }         }         return swaps;   } };  # @lc code=end