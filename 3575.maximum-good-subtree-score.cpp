#
# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> adj;
    vector<int> values;
    long long total_sum = 0;
    const int MOD = 1e9 + 7;
    long long dp_buffer[1024]; // Global buffer to avoid repeated allocations

    // Helper to extract digit mask from a value
    // Returns -1 if the value itself has duplicate digits
    int getMask(int val) {
        int mask = 0;
        if (val == 0) return 1; 
        while (val > 0) {
            int digit = val % 10;
            if ((mask >> digit) & 1) return -1;
            mask |= (1 << digit);
            val /= 10;
        }
        return mask;
    }

    // DFS to compute DP states for each subtree
    // Returns a vector of pairs {mask, max_score}
    vector<pair<int, long long>> dfs(int u) {
        vector<pair<int, long long>> current_states;
        current_states.reserve(1024);
        // Base state: empty subset, mask 0, score 0
        current_states.push_back({0, 0});

        for (int v : adj[u]) {
            vector<pair<int, long long>> child_states = dfs(v);
            
            vector<int> dirty;
            dirty.reserve(1024);
            
            // Merge child states into current states
            // We iterate all pairs and combine if masks are disjoint
            for (const auto& p1 : current_states) {
                for (const auto& p2 : child_states) {
                    if ((p1.first & p2.first) == 0) {
                        int nm = p1.first | p2.first;
                        long long ns = p1.second + p2.second;
                        
                        if (dp_buffer[nm] == -1) {
                            dp_buffer[nm] = ns;
                            dirty.push_back(nm);
                        } else {
                            if (ns > dp_buffer[nm]) dp_buffer[nm] = ns;
                        }
                    }
                }
            }
            
            // Update current_states from buffer and reset buffer
            current_states.clear();
            for (int m : dirty) {
                current_states.push_back({m, dp_buffer[m]});
                dp_buffer[m] = -1;
            }
        }

        // Try to include the current node u
        int u_mask = getMask(values[u]);
        if (u_mask != -1) {
             vector<int> dirty;
             dirty.reserve(1024);

             // First, load current states into buffer to serve as the base for "not including u"
             // and to allow merging "including u"
             for(const auto& p : current_states) {
                 if(dp_buffer[p.first] == -1) {
                     dp_buffer[p.first] = p.second;
                     dirty.push_back(p.first);
                 } else {
                     if (p.second > dp_buffer[p.first]) dp_buffer[p.first] = p.second;
                 }
             }

             // Now iterate current_states (which represent subsets of descendants)
             // and try to add u to them
             int sz = current_states.size();
             for(int i=0; i<sz; ++i) {
                 const auto& p = current_states[i];
                 if ((p.first & u_mask) == 0) {
                     int nm = p.first | u_mask;
                     long long ns = p.second + values[u];
                     
                     if (dp_buffer[nm] == -1) {
                         dp_buffer[nm] = ns;
                         dirty.push_back(nm);
                     } else {
                         if (ns > dp_buffer[nm]) dp_buffer[nm] = ns;
                     }
                 }
             }
             
             // Collect results back
             current_states.clear();
             for(int m : dirty) {
                 current_states.push_back({m, dp_buffer[m]});
                 dp_buffer[m] = -1;
             }
        }
        
        // Calculate max score for subtree rooted at u
        long long current_max = 0;
        for(const auto& p : current_states) {
            if (p.second > current_max) current_max = p.second;
        }
        total_sum = (total_sum + current_max) % MOD;
        
        return current_states;
    }

    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        int n = vals.size();
        adj.assign(n, vector<int>());
        values = vals;
        for (int i = 0; i < n; ++i) {
            if (par[i] != -1) {
                adj[par[i]].push_back(i);
            }
        }

        // Initialize buffer with -1
        fill(begin(dp_buffer), end(dp_buffer), -1);

        dfs(0);
        return total_sum;
    }
};
# @lc code=end