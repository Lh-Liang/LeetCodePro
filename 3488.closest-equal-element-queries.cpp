#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        // Store value and its original index
        vector<pair<int, int>> val_idx(n);
        for (int i = 0; i < n; ++i) {
            val_idx[i] = {nums[i], i};
        }
        
        // Sort to group identical values and their indices in ascending order
        sort(val_idx.begin(), val_idx.end());
        
        vector<int> closest_dist(n, -1);
        
        int i = 0;
        while (i < n) {
            int j = i;
            // Find the range of elements with the same value
            while (j < n && val_idx[j].first == val_idx[i].first) {
                j++;
            }
            
            int count = j - i;
            if (count > 1) {
                for (int m = 0; m < count; ++m) {
                    int curr_idx = val_idx[i + m].second;
                    // Neighbors in the sorted list of indices for this specific value
                    int prev_idx = val_idx[i + (m - 1 + count) % count].second;
                    int next_idx = val_idx[i + (m + 1) % count].second;
                    
                    // Lambda to calculate circular distance
                    auto get_circ_dist = [&](int a, int b) {
                        int d = std::abs(a - b);
                        return std::min(d, n - d);
                    };
                    
                    closest_dist[curr_idx] = std::min(get_circ_dist(curr_idx, prev_idx), 
                                                      get_circ_dist(curr_idx, next_idx));
                }
            }
            i = j;
        }
        
        vector<int> answer;
        answer.reserve(queries.size());
        for (int q : queries) {
            answer.push_back(closest_dist[q]);
        }
        return answer;
    }
};
# @lc code=end