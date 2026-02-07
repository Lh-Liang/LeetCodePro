#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int operations = 0;
        while(true) {
            unordered_set<int> seen;
            bool hasDuplicates = false;
            for(int num : nums) {
                if(seen.count(num)) {
                    hasDuplicates = true;
                    break;
                } else {
                    seen.insert(num);
                }
            }
            if(!hasDuplicates) break; // Stop if no duplicates exist. 
            // Remove first three elements or all if less than three remain. 
            nums.erase(nums.begin(), nums.size() < 3 ? nums.end() : nums.begin() + 3); 
            operations++; 
        } 
        return operations; 
    } 
}; 
# @lc code=end