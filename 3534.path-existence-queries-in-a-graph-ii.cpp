#
# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // Sort indices by nums value
        vector<int> sorted_idx(n);
        iota(sorted_idx.begin(), sorted_idx.end(), 0);
        sort(sorted_idx.begin(), sorted_idx.end(), [&](int a, int b) {
            return nums[a] < nums[b];
        });
        
        // Position of each node in sorted order
        vector<int> pos(n);
        for (int i = 0; i < n; i++) {
            pos[sorted_idx[i]] = i;
        }
        
        // Sorted values
        vector<int> sorted_vals(n);
        for (int i = 0; i < n; i++) {
            sorted_vals[i] = nums[sorted_idx[i]];
        }
        
        // For each position, compute rightmost reachable position
        vector<int> reach(n);
        for (int i = 0; i < n; i++) {
            auto it = upper_bound(sorted_vals.begin(), sorted_vals.end(), sorted_vals[i] + maxDiff);
            reach[i] = (int)(it - sorted_vals.begin()) - 1;
        }
        
        // Binary lifting
        const int LOG = 17; // log2(10^5) < 17
        vector<vector<int>> jump(LOG, vector<int>(n));
        
        // Base case: one jump goes to reach[i]
        for (int i = 0; i < n; i++) {
            jump[0][i] = reach[i];
        }
        
        // Build table
        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < n; i++) {
                jump[k][i] = jump[k-1][jump[k-1][i]];
            }
        }
        
        vector<int> answer;
        for (const auto& q : queries) {
            int u = q[0], v = q[1];
            int pu = pos[u], pv = pos[v];
            
            if (pu == pv) {
                answer.push_back(0);
                continue;
            }
            
            if (pu > pv) swap(pu, pv);
            
            int current = pu;
            int jumps = 0;
            for (int k = LOG - 1; k >= 0; k--) {
                if (jump[k][current] < pv && jump[k][current] > current) {
                    current = jump[k][current];
                    jumps += (1 << k);
                }
            }
            
            if (reach[current] < pv) {
                answer.push_back(-1);
            } else {
                answer.push_back(jumps + 1);
            }
        }
        
        return answer;
    }
};
# @lc code=end