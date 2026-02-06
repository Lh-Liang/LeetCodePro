#
# @lc app=leetcode id=3615 lang=java
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution {
    public int maxLen(int n, int[][] edges, String label) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        int[] max = new int[1];
        for (int i = 0; i < n; ++i) {
            boolean[] visited = new boolean[n];
            dfs(i, graph, label, new StringBuilder(), visited, max);
        }
        return max[0];
    }
    private void dfs(int node, List<Integer>[] graph, String label, StringBuilder path, boolean[] visited, int[] max) {
        path.append(label.charAt(node));
        visited[node] = true;
        if (isPalindrome(path)) {
            max[0] = Math.max(max[0], path.length());
        }
        for (int nei : graph[node]) {
            if (!visited[nei]) {
                dfs(nei, graph, label, path, visited, max);
            }
        }
        path.deleteCharAt(path.length() - 1);
        visited[node] = false;
    }
    private boolean isPalindrome(StringBuilder sb) {
        int l = 0, r = sb.length() - 1;
        while (l < r) {
            if (sb.charAt(l) != sb.charAt(r)) return false;
            ++l; --r;
        }
        return true;
    }
}
# @lc code=end