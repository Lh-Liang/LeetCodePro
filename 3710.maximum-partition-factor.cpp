#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#
# @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;
        
        set<int> distSet;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                distSet.insert(dist);
            }
        }
        distSet.insert(0);
        
        int maxFactor = 0;
        
        for (int threshold : distSet) {
            vector<vector<int>> adj(n);
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                    if (dist < threshold) {
                        adj[i].push_back(j);
                        adj[j].push_back(i);
                    }
                }
            }
            
            vector<int> color(n, -1), component(n, -1);
            int numComponents = 0;
            bool isBipartite = true;
            
            function<bool(int, int, int)> dfs = [&](int u, int c, int comp) -> bool {
                color[u] = c;
                component[u] = comp;
                for (int v : adj[u]) {
                    if (color[v] == -1) {
                        if (!dfs(v, 1 - c, comp)) return false;
                    } else if (color[v] == c) return false;
                }
                return true;
            };
            
            for (int i = 0; i < n && isBipartite; i++) {
                if (color[i] == -1) {
                    if (!dfs(i, 0, numComponents)) isBipartite = false;
                    else numComponents++;
                }
            }
            
            if (!isBipartite) continue;
            
            vector<vector<vector<int>>> compClasses(numComponents, vector<vector<int>>(2));
            for (int i = 0; i < n; i++) {
                compClasses[component[i]][color[i]].push_back(i);
            }
            
            vector<int> singletons, nonSingletonComps;
            for (int comp = 0; comp < numComponents; comp++) {
                int size = compClasses[comp][0].size() + compClasses[comp][1].size();
                if (size == 1) {
                    singletons.push_back(compClasses[comp][0].empty() ? compClasses[comp][1][0] : compClasses[comp][0][0]);
                } else nonSingletonComps.push_back(comp);
            }
            
            int k = nonSingletonComps.size();
            if (k > 20) continue;
            
            for (int mask = 0; mask < (1 << k); mask++) {
                vector<int> groupA, groupB;
                for (int idx = 0; idx < k; idx++) {
                    int comp = nonSingletonComps[idx];
                    if (mask & (1 << idx)) {
                        groupA.insert(groupA.end(), compClasses[comp][0].begin(), compClasses[comp][0].end());
                        groupB.insert(groupB.end(), compClasses[comp][1].begin(), compClasses[comp][1].end());
                    } else {
                        groupA.insert(groupA.end(), compClasses[comp][1].begin(), compClasses[comp][1].end());
                        groupB.insert(groupB.end(), compClasses[comp][0].begin(), compClasses[comp][0].end());
                    }
                }
                
                for (int v : singletons) {
                    if (groupA.size() <= groupB.size()) groupA.push_back(v);
                    else groupB.push_back(v);
                }
                
                if (groupA.empty() || groupB.empty()) continue;
                
                int minDistA = INT_MAX, minDistB = INT_MAX;
                for (size_t i = 0; i < groupA.size(); i++) {
                    for (size_t j = i + 1; j < groupA.size(); j++) {
                        int dist = abs(points[groupA[i]][0] - points[groupA[j]][0]) + abs(points[groupA[i]][1] - points[groupA[j]][1]);
                        minDistA = min(minDistA, dist);
                    }
                }
                for (size_t i = 0; i < groupB.size(); i++) {
                    for (size_t j = i + 1; j < groupB.size(); j++) {
                        int dist = abs(points[groupB[i]][0] - points[groupB[j]][0]) + abs(points[groupB[i]][1] - points[groupB[j]][1]);
                        minDistB = min(minDistB, dist);
                    }
                }
                
                if (groupA.size() == 1) minDistA = INT_MAX;
                if (groupB.size() == 1) minDistB = INT_MAX;
                
                int partitionFactor = min(minDistA, minDistB);
                if (partitionFactor == INT_MAX) partitionFactor = 0;
                maxFactor = max(maxFactor, partitionFactor);
            }
        }
        
        return maxFactor;
    }
};
# @lc code=end