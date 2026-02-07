#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#
# @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        priority_queue<int> maxHeap;
        for (int i = 0; i < grid.size(); ++i) {
            sort(grid[i].rbegin(), grid[i].rend()); // Sort each row in descending order
            for (int j = 0; j < min(limits[i], (int)grid[i].size()); ++j) {
                maxHeap.push(grid[i][j]); // Add up to limits[i] elements from each row to the heap
            }
        }
        long long sum = 0;
        while (k-- > 0 && !maxHeap.empty()) {
            sum += maxHeap.top();
            maxHeap.pop(); // Extract top k elements from heap for maximum sum
        }
        return sum;
    }
};
# @lc code=end