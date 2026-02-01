#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

/*
 * @lc app=leetcode id=3462 lang=cpp
 *
 * [3462] Maximum Sum With at Most K Elements
 */

// @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        int n = grid.size();
        vector<int> candidatePool;

        // Step 1: Extract the top 'limits[i]' elements from each row.
        for (int i = 0; i < n; ++i) {
            // Sort row in descending order to easily pick the largest elements.
            sort(grid[i].begin(), grid[i].end(), greater<int>());
            
            // Only take up to the allowed limit for this specific row.
            int count = min((int)grid[i].size(), limits[i]);
            for (int j = 0; j < count; ++j) {
                candidatePool.push_back(grid[i][j]);
            }
        }

        // Step 2: Sort the combined candidates from all rows in descending order.
        sort(candidatePool.begin(), candidatePool.end(), greater<int>());

        // Step 3: Pick the top k elements from the pool.
        long long totalSum = 0;
        int elementsToPick = min((int)candidatePool.size(), k);
        for (int i = 0; i < elementsToPick; ++i) {
            totalSum += (long long)candidatePool[i];
        }

        return totalSum;
    }
};
// @lc code=end