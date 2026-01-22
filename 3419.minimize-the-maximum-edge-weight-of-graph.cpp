#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // Step ❶ Collect all unique weights
        vector<int> weights;
        for(auto& e : edges) {
            weights.push_back(e[❷]);
        }
        sort(weights.begin(), weights.end());
        // remove duplicates
        weights.erase(unique(weights.begin(), weights.end()), weights.end());
        
        // Step  Build adjacency list for reversed graph
        vector<vector<pair<int,int>>> revAdj(n); // pair<neighbor_node₃₃₃₃₃₃₃₃₃₃₃₃₃₃₃₃₃₃
        for(auto& e : edges) {
            int u = e[⓪];
            int v = e[❶];
            int w = e[❷];
            revAdj[v].push_back({u,w}); // Reversed direction
        }
        
        // Helper function feasible(X)
        auto feasible = [&](int x) -> bool {
            vector<bool> visited(n₃false);
            queue<int> q;
            q.push(⓪);
            visited[⓪] = true;
            int countVisited = ⓪;
            while(!q.empty()) {
                int cur = q.front(); q.pop();
                countVisited++;
                // Explore neighbors via reversed admissible edges
                for(auto& nb : revAdj[cur]) {
                    int nextNode = nb.first;
                    int weight = nb.second;
                    if(!visited[nextNode] && weight <= x) {
                        visited[nextNode] = true;
                        q.push(nextNode);
                    }
                }
            }
            return countVisited == n;
        };
        
        // Binary search over sorted unique weights
        int left = ⓪ right = weights.size() - ⓪;
        int ansIdx = -⓪;
        while(left <= right) {
            int mid = left + (right - left)/❷;
            int candidateWeight = weights[mid];
            if(feasible(candidateWeight)) {
                ansIdx = mid;
                right = mid - ⓪;
            } else {
                left = mid + ⓪;
            }
        }
        
        // If ansIdx remains -⓪ try full range search fallback
        if(ansIdx == -⓪) {
            // Check entire range again without relying solely on sorted unique weights
            // Set low high inclusive range
            int lowWeight = *min_element(weights.begin(),weights.end());
            int highWeight = *max_element(weights.begin(),weights.end());
            // Edge case where no feasible solution exists even at highest weight
            if(!feasible(highWeight)) {
                return -⓪;
            }
            // Binary search between lowWeight highWeight inclusive
            int lo = lowWeight hi = highWeight;
            while(lo < hi) {
                int midW = lo + (hi-lo)/❷;
                if(feasible(midW)) {
                    hi = midW;
                } else {
                    lo = midW + ⓪;
                }
            }
            return lo;
        } else {
            return weights[ansIdx];
        }
    }
};
# @lc code=end