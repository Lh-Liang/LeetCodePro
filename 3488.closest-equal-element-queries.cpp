#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        // Step 1: Analyze constraints and requirements.
        // N is up to 10^5, so we need an O(N log N) or O(N) solution.
        // The distance is circular, meaning the distance between indices i and j is min(|i-j|, n - |i-j|).
        int n = nums.size();
        
        // Step 2: Group indices by their values.
        // We use a vector of pairs (value, original_index) and sort it.
        vector<pair<int, int>> val_idx(n);
        for (int i = 0; i < n; ++i) {
            val_idx[i] = {nums[i], i};
        }
        sort(val_idx.begin(), val_idx.end());
        
        vector<int> min_dist(n, -1);
        
        // Step 3: Iterate through groups of identical values.
        // For a value appearing at sorted indices [p0, p1, ..., pk-1]:
        // The closest equal element to pi is either its predecessor (pi-1) or successor (pi+1).
        // In a circular array, p0's neighbors are pk-1 and p1; pk-1's neighbors are pk-2 and p0.
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && val_idx[j].first == val_idx[i].first) {
                j++;
            }
            
            int k = j - i;
            if (k > 1) {
                // Step 4: Calculate circular distances for each occurrence.
                for (int m = 0; m < k; ++m) {
                    int curr_idx = val_idx[i + m].second;
                    int prev_idx, next_idx;
                    
                    if (m == 0) {
                        prev_idx = val_idx[i + k - 1].second;
                        next_idx = val_idx[i + 1].second;
                    } else if (m == k - 1) {
                        prev_idx = val_idx[i + m - 1].second;
                        next_idx = val_idx[i].second;
                    } else {
                        prev_idx = val_idx[i + m - 1].second;
                        next_idx = val_idx[i + m + 1].second;
                    }
                    
                    // Calculate circular distance: min(|a-b|, n - |a-b|)
                    auto get_circ_dist = [&](int a, int b) {
                        int diff = abs(a - b);
                        return min(diff, n - diff);
                    };
                    
                    min_dist[curr_idx] = min(get_circ_dist(curr_idx, prev_idx), 
                                             get_circ_dist(curr_idx, next_idx));
                }
            }
            i = j;
        }
        
        // Step 5: Answer queries using the precomputed min_dist array.
        vector<int> result;
        result.reserve(queries.size());
        for (int q : queries) {
            result.push_back(min_dist[q]);
        }
        
        return result;
    }
};
# @lc code=end