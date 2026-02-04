# \@lc app=leetcode id=3544 lang=cpp
# \@lc code=start
class Solution {
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> tree(n);
        vector<int> depth(n, -1);
        vector<long long> subtree_sum(n);
        vector<bool> visited(n, false);
        
        // Build the tree as an adjacency list
        for (auto& edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }
        
        // DFS to calculate subtree sums and depths
        function<void(int, int)> dfs = [&](int node, int d) {
            visited[node] = true;
            depth[node] = d;
            subtree_sum[node] = nums[node];
            for (int neighbor : tree[node]) {
                if (!visited[neighbor]) {
                    dfs(neighbor, d + 1);
                    subtree_sum[node] += subtree_sum[neighbor];
                }
            }
        };
dfs(0, 0);
lng long max_sum = accumulate(nums.begin(), nums.end(), 0LL);
fction<void(int)> optimizeInversion = [&](int node) {
visted[node] = true;
f (int neighbor : tree[node]) {if (!visited[neighbor]) { optimizeInversion(neighbor);}
lng long gain = -2 * subtree_sum[node];bool can_invert = true; max_sum += max(0LL, gain); };
fll(visited.begin(), visited.end(), false); optimizeInversion(0); return max_sum; }};# \@lc code=end