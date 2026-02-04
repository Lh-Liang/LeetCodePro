#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        // Calculate all Manhattan distances between point pairs
        vector<int> distances;
        int n = points.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                distances.push_back(dist);
            }
        }
        // Sort distances for binary search
        sort(distances.begin(), distances.end());
        // Binary search for maximum partition factor
        int left = 0, right = distances.size() - 1;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (canPartition(points, distances[mid])) {
                left = mid; // This distance can be achieved, try larger one
            } else {
                right = mid - 1; // Too large, try smaller one
            }
        }
        return distances[left]; // Maximum partition factor found at left index     
    }
    
    bool canPartition(const vector<vector<int>>& points, int minDist) {
        // Use union-find to check if we can partition with this minimum distance
        int n = points.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int u) { return u == parent[u] ? u : parent[u] = find(parent[u]); };
        auto unite = [&](int u, int v) { parent[find(u)] = find(v); };
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) < minDist)
                    unite(i, j);
            }
        }
        unordered_set<int> roots;
        for (int i = 0; i < n; ++i)
            roots.insert(find(i));
        return roots.size() >= 2; // Valid partition if there are at least two separate groups
    }
};
# @lc code=end