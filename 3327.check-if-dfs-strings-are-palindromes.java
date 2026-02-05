class Solution {
    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] tree = new List[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) tree[parent[i]].add(i);
        boolean[] answer = new boolean[n];
        for (int i = 0; i < n; ++i) {
            StringBuilder sb = new StringBuilder();
            dfs(i, s, tree, sb);
            answer[i] = isPalindrome(sb);
        }
        return answer;
    }
    private void dfs(int node, String s, List<Integer>[] tree, StringBuilder sb) {
        List<Integer> children = tree[node];
        Collections.sort(children);
        for (int child : children) {
            dfs(child, s, tree, sb);
        }
        sb.append(s.charAt(node));
    }
    private boolean isPalindrome(StringBuilder sb) {
        int l = 0, r = sb.length() - 1;
        while (l < r) {
            if (sb.charAt(l++) != sb.charAt(r--)) return false;
        }
        return true;
    }
}