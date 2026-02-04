#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        priority_queue<int> pq;
        // Iterate over each row in the grid
        for (int i = 0; i < grid.size(); ++i) {
            // Sort each row in descending order to prioritize larger elements
            sort(grid[i].rbegin(), grid[i].rend());
            // Add eligible elements up to limit[i] into the max-heap
            for (int j = 0; j < min(limits[i], (int)grid[i].size()); ++j) {
                pq.push(grid[i][j]);
            }
        }
        long long sum = 0; // Variable to store the maximum sum of selected elements
        // Extract up to k elements from the heap for maximum sum calculation
        while (k > 0 && !pq.empty()) {
            sum += pq.top(); // Add largest element from heap to sum
            pq.pop(); // Remove the element from heap after adding it to sum
            --k; // Decrement k as one element has been selected and added
        }
        return sum; // Return maximum sum obtained with at most k elements respecting all constraints
    }
};
# @lc code=end