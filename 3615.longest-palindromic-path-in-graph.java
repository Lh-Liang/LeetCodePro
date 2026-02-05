#
# @lc app=leetcode id=3615 lang=java
#
# [3615] Longest Palindromic Path in Graph
#
# @lc code=start
class Solution {
    public int maxLen(int n, int[][] edges, String label) {
        // Build adjacency list
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        int[] max = new int[1];
        for (int start = 0; start < n; start++) {
            dfs(start, 1 << start, new ArrayList<>(), graph, label, max);
        }
        return max[0];
    }
    private void dfs(int node, int visited, List<Integer> path, List<Integer>[] graph, String label, int[] max) {
        path.add(node);
        if (isPalindrome(path, label)) {
            // Verify all constraints before updating max
            max[0] = Math.max(max[0], path.size());
        }
        // Prune: if remaining nodes cannot surpass current max, skip
        if (path.size() + Integer.bitCount(~visited & ((1<<graph.length)-1)) <= max[0]) {
            path.remove(path.size() - 1);
            return;
        }
        for (int nei : graph[node]) {
            if ((visited & (1 << nei)) == 0) {
                dfs(nei, visited | (1 << nei), path, graph, label, max);
            }
        }
        path.remove(path.size() - 1);
    }
    private boolean isPalindrome(List<Integer> path, String label) {
        int l = 0, r = path.size() - 1;
        while (l < r) {
            if (label.charAt(path.get(l)) != label.charAt(path.get(r))) return false;
            l++; r--;
        }
        return true;
    }
}
# @lc code=end