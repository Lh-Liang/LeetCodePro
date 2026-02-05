# @lc app=leetcode id=3563 lang=java
# [3563] Lexicographically Smallest String After Adjacent Removals
# @lc code=start
class Solution {
    public String lexicographicallySmallestString(String s) {
        Deque<Character> stack = new LinkedList<>();
        for (char c : s.toCharArray()) {
            while (!stack.isEmpty() && areConsecutive(stack.peek(), c)) {
                stack.pop();
            }
            stack.push(c);
        }
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.append(stack.removeLast());
        }
        return result.toString();
    }
    
    private boolean areConsecutive(char a, char b) {
        return (a + 1 == b) || (b + 1 == a) || (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
    }
}
# @lc code=end