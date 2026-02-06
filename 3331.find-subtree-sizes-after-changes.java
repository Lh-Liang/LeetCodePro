#
# @lc app=leetcode id=3331 lang=java
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        int[] newParent = parent.clone();
        // Step 1: For each node, find the closest ancestor with the same character
        for (int x = 1; x < n; x++) {
            int p = parent[x];
            while (p != -1 && s.charAt(p) != s.charAt(x)) {
                p = parent[p];
            }
            if (p != -1) {
                newParent[x] = p;
            }
        }
        // Step 2: Build the new tree adjacency list
        List<Integer>[] tree = new List[n];
        for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            tree[newParent[i]].add(i);
        }
        // Step 3: DFS to compute subtree sizes
        int[] ans = new int[n];
        dfs(0, tree, ans);
        return ans;
    }
    private int dfs(int node, List<Integer>[] tree, int[] ans) {
        int size = 1;
        for (int child : tree[node]) {
            size += dfs(child, tree, ans);
        }
        ans[node] = size;
        return size;
    }
}
# @lc code=end