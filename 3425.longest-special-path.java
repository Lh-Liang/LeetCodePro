#
# @lc app=leetcode id=3425 lang=java
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        List<int[]>[] tree = new List[n];
        for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();
        for (int[] e : edges) {
            tree[e[0]].add(new int[]{e[1], e[2]});
            tree[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] res = new int[]{0, 1}; // {maxLen, minNodes}
        Set<Integer> seen = new HashSet<>();
        dfs(0, -1, 0, 1, seen, nums, tree, res);
        // After traversal, ensure result matches constraints (not necessary here but included for robustness)
        return res;
    }
    private void dfs(int u, int parent, int curLen, int nodeCount, Set<Integer> seen, int[] nums, List<int[]>[] tree, int[] res) {
        // Pre-recursion: ensure uniqueness constraint
        if (seen.contains(nums[u])) return;
        seen.add(nums[u]);
        // Update result if needed
        if (curLen > res[0]) {
            res[0] = curLen;
            res[1] = nodeCount;
        } else if (curLen == res[0]) {
            res[1] = Math.min(res[1], nodeCount);
        }
        // Recurse on all children (except parent)
        for (int[] nei : tree[u]) {
            int v = nei[0], w = nei[1];
            if (v == parent) continue;
            dfs(v, u, curLen + w, nodeCount + 1, seen, nums, tree, res);
        }
        // Post-recursion: backtrack state
        seen.remove(nums[u]);
    }
}
# @lc code=end