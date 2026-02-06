#
# @lc app=leetcode id=3563 lang=java
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
class Solution {
    public String lexicographicallySmallestString(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            while (!stack.isEmpty() && (stack.peek() == c + 1 || stack.peek() == c - 1 || (stack.peek() == 'a' && c == 'z') || (stack.peek() == 'z' && c == 'a'))) {
                stack.pop();
            }
            stack.push(c);
        }
        StringBuilder result = new StringBuilder();
        for (char c : stack) {
            result.append(c);
        }
        return result.toString();
    }
}
# @lc code=end