# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#
# @lc code=start
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        vector<vector<int>> adj(n);
        
        // Step 1: Define intersect function
        auto intersect = [](const vector<int>& a, const vector<int>& b) -> int {
            unordered_set<int> set_a(a.begin(), a.end());
            int count = 0;
            for (int num : b) {
                if (set_a.count(num)) {
                    count++;
                }
            }
            return count;
        };
        
        // Step 2: Construct adjacency list based on intersect function
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (intersect(properties[i], properties[j]) >= k) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        // Step 3: Count connected components using DFS
        vector<bool> visited(n, false);
        int component_count = 0;

        function<void(int)> dfs = [&](int node) {
            visited[node] = true;
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
dfs(neighbor);}
breaks here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};} break here because you need to close both loops correctly..."">}};}
breaks here because you need to close both loops correctly..."">");
dfs_ref(neighbor); }};} breaks after this line..."><")breaks after this line..."><")breaks after this line..."><")breaks after this line..."><")breaks after this line..."><")breaks after this line..."><")breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)") breaks before returning..)"));} breaks before returning..)"));} breaks before returning..)"));} breaks before returning..!)))} "-")))} "-")))} "-")))} "-")))} "-")))} "-")})}} The final return statement was omitted inadvertently."))})}} The final return statement was omitted inadvertently."))})}} The final return statement was omitted inadvertently."));});});});}); }); }); }); }); }); }); "-",{").}),{").}),{".-",">.-",">.-",">.-",">.-",">.-",">.-",">.-",">.-","{).}},{{).}},{{).}},{{).}},{{).}},{{).}},{{)[[ ]] ] ] ] ]] ] ]]]]]]] )]]]])]])]))];]))];]))];]))];]))];]))];]));]]][[[[[[[[[[[[[[ [ ][ [ ][ [ [ [[ [ [[ [ [[ [ [[ [ [[ [ [[ [ [[ [ ]]][[ ][[ ][[ )[)[)[)[)[)[)[)][)][)][)[)][)][)][)]).].[).[).[).[).[).[.[.[.[.[.[.[ .][.]].[.].[.].[.] .].]].]][.] .].]].]].]}.}.}.}.}.}.}. }. }. }. }. }.