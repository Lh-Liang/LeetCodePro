#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        vector<int> candidates;
        int n = grid.size();
        
        for (int i = 0; i < n; ++i) {
            if (limits[i] > 0) {
                // Sort the row in descending order to pick the largest elements
                sort(grid[i].begin(), grid[i].end(), greater<int>());
                // Add the top limits[i] elements to the candidate pool
                int count = min((int)grid[i].size(), limits[i]);
                for (int j = 0; j < count; ++j) {
                    candidates.push_back(grid[i][j]);
                }
            }
        }
        
        // Sort all possible candidates across all rows in descending order
        sort(candidates.begin(), candidates.end(), greater<int>());
        
        long long totalSum = 0;
        // Take up to k elements from the candidate pool
        int take = min((int)candidates.size(), k);
        for (int i = 0; i < take; ++i) {
            totalSum += candidates[i];
        }
        
        return totalSum;
    }
};