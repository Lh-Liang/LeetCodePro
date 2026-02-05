# @lc app=leetcode id=3327 lang=java
# [3327] Check if DFS Strings Are Palindromes

# @lc code=start
import java.util.*;

class Solution {
    private List<List<Integer>> tree;
    private String s;
    private StringBuilder dfsStr;
    
    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        this.s = s;
        this.tree = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            tree.add(new ArrayList<>());
        }
        for (int i = 1; i < n; i++) {
            tree.get(parent[i]).add(i);
        }

        boolean[] answer = new boolean[n];
        for (int i = 0; i < n; i++) {
            dfsStr = new StringBuilder();
            dfs(i);
            answer[i] = isPalindrome(dfsStr.toString());
        }
        return answer;
    }
    
    private void dfs(int x) {
        for (int y : tree.get(x)) {
            dfs(y);
        }
        dfsStr.append(s.charAt(x));
    }

    private boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
# @lc code=end