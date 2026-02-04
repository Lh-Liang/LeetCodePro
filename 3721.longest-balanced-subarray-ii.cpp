#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        unordered_map<int, int> balanceIndex;
        int maxLen = 0, balance = 0;
        balanceIndex[0] = -1; // Initial state to handle cases where subarray starts at index 0
        unordered_set<int> seenEven, seenOdd;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] % 2 == 0) { // Even number
                seenEven.insert(nums[i]);
            } else { // Odd number
                seenOdd.insert(nums[i]);
            }
            
            int currentBalance = seenEven.size() - seenOdd.size();
            
            if (currentBalance == 0) {
                maxLen = max(maxLen, i + 1);
            }
            
            if (balanceIndex.find(currentBalance) != balanceIndex.end()) {
                maxLen = max(maxLen, i - balanceIndex[currentBalance]);
            } else {
                balanceIndex[currentBalance] = i;
            }
        }
        return maxLen;
    }
}; 
# @lc code=end