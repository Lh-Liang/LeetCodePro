#
# @lc app=leetcode id=3327 lang=java
#
# [3327] Check if DFS Strings Are Palindromes
#
# @lc code=start
class Solution {
    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] tree = new List[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) {
            tree[parent[i]].add(i);
        }
        // Sort children for each node to enforce increasing order
        for (int i = 0; i < n; ++i) Collections.sort(tree[i]);
        
        // Cache postorder traversals
        List<Integer>[] postorder = new List[n];
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; ++i) {
            postorder[i] = new ArrayList<>();
            dfs(i, tree, postorder[i], visited);
            Arrays.fill(visited, false); // Reset for each node
        }
        boolean[] answer = new boolean[n];
        for (int i = 0; i < n; ++i) {
            List<Integer> post = postorder[i];
            int l = 0, r = post.size() - 1;
            boolean isPalin = true;
            while (l < r) {
                if (s.charAt(post.get(l)) != s.charAt(post.get(r))) {
                    isPalin = false;
                    break;
                }
                l++; r--;
            }
            answer[i] = isPalin;
        }
        return answer;
    }
    private void dfs(int x, List<Integer>[] tree, List<Integer> res, boolean[] visited) {
        if (visited[x]) return;
        visited[x] = true;
        for (int y : tree[x]) {
            dfs(y, tree, res, visited);
        }
        res.add(x);
    }
}
# @lc code=end