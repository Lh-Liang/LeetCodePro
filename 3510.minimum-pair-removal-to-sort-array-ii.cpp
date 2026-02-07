#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int operations = 0;
        int n = nums.size();
        set<int> indices; // Stores indices of problematic points
        
        // Identify initial problematic points
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                indices.insert(i);
            }
        }
        
        while (!indices.empty()) {
            auto it = indices.begin();
            int index = *it;
            indices.erase(it);
            
            // Merge the pair at index with its sum
            nums[index] = nums[index] + nums[index + 1];
            nums.erase(nums.begin() + index + 1);
            --n;
            ++operations;

            // Re-evaluate and adjust problematic points around the merged point
            if (index > 0 && nums[index - 1] > nums[index]) {
                indices.insert(index - 1);
            }
            if (index < n - 1 && nums[index] > nums[index + 1]) {
                indices.insert(index);
            }
        }
        return operations;
    }
};
success