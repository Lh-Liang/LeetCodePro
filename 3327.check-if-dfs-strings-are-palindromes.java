#
# @lc app=leetcode id=3327 lang=java
#
# [3327] Check if DFS Strings Are Palindromes
#
# @lc code=start
class Solution {
    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        List<List<Integer>> children = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            children.add(new ArrayList<>());
        }
        for (int i = 1; i < n; i++) {
            children.get(parent[i]).add(i);
        }
        
        boolean[] answer = new boolean[n];
        for (int i = 0; i < n; i++) {
            StringBuilder dfsStr = new StringBuilder();
            dfs(i, s, children, dfsStr);
            answer[i] = isPalindrome(dfsStr.toString());
        }
        return answer;
    }
    
    private void dfs(int x, String s, List<List<Integer>> children, StringBuilder dfsStr) {
        for (int y : children.get(x)) {
            dfs(y, s, children, dfsStr);
        }
        dfsStr.append(s.charAt(x));
    } 
    
    private boolean isPalindrome(String str) {	return str.equals(new StringBuilder(str).reverse().toString()); } 
} 
# @lc code=end