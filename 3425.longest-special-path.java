#
# @lc app=leetcode id=3425 lang=java
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        List<int[]>[] adj = new List[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
            adj[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] res = new int[]{0, Integer.MAX_VALUE}; // [max_length, min_nodes]
        Set<Integer> path = new HashSet<>();
        dfs(0, -1, adj, nums, path, 0, 1, res);
        res[1] = Math.max(1, res[1]); // at least one node
        return res;
    }
    private void dfs(int u, int parent, List<int[]>[] adj, int[] nums, Set<Integer> path, int curLen, int curNodes, int[] res) {
        if (path.contains(nums[u])) {
            if (curLen > res[0]) {
                res[0] = curLen;
                res[1] = curNodes - 1;
            } else if (curLen == res[0]) {
                res[1] = Math.min(res[1], curNodes - 1);
            }
            return;
        }
        path.add(nums[u]);
        boolean isLeaf = true;
        for (int[] nei : adj[u]) {
            if (nei[0] != parent) {
                isLeaf = false;
                dfs(nei[0], u, adj, nums, path, curLen + nei[1], curNodes + 1, res);
            }
        }
        if (isLeaf) {
            if (curLen > res[0]) {
                res[0] = curLen;
                res[1] = curNodes;
            } else if (curLen == res[0]) {
                res[1] = Math.min(res[1], curNodes);
            }
        }
        path.remove(nums[u]);
    }
}
# @lc code=end