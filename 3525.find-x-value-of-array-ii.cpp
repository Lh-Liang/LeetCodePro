#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#
# @lc code=start
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<int> results;
        for (auto &query : queries) {
            int index = query[0];
            int value = query[1];
            int start = query[2];
            int xi = query[3];
            
            // Update nums with new value at indexi
            nums[index] = value;
            
            // Calculate product mod k for remaining elements after removing prefix up to starti-1
            long long productModK = 1;
            vector<int> modCount(k, 0);
            modCount[0] = 1; // Zero remainder is always possible with empty suffix removal.
            
            // Iterate over possible suffixes starting from 'start' to end of nums.
            for (int i = start; i < nums.size(); ++i) {
                productModK = (productModK * nums[i]) % k;
                modCount[productModK]++; // Count occurrences of each remainder mod k.
            } 
            results.push_back(modCount[xi]); // The x-value is the count of xi remainders mod k. 
        } 
        return results; 
    } 
}; 
# @lc code=end