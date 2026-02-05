#
# @lc app=leetcode id=2296 lang=java
#
# [2296] Design a Text Editor
#
# @lc code=start
import java.util.*;
class TextEditor {
    Deque<Character> left; // Text to the left of cursor
    Deque<Character> right; // Text to the right of cursor
    public TextEditor() {
        left = new ArrayDeque<>();
        right = new ArrayDeque<>();
    }
    public void addText(String text) {
        for (char c : text.toCharArray()) {
            left.offerLast(c);
        }
    }
    public int deleteText(int k) {
        int count = 0;
        while (count < k && !left.isEmpty()) {
            left.pollLast();
            count++;
        }
        return count;
    }
    public String cursorLeft(int k) {
        while (k > 0 && !left.isEmpty()) {
            right.offerFirst(left.pollLast());
            k--;
        }
        return getLeftText();
    }
    public String cursorRight(int k) {
        while (k > 0 && !right.isEmpty()) {
            left.offerLast(right.pollFirst());
            k--;
        }
        return getLeftText();
    }
    private String getLeftText() {
        StringBuilder sb = new StringBuilder();
        Iterator<Character> iter = left.descendingIterator();
        int count = 10; // We only need last 10 characters
        while (count > 0 && iter.hasNext()) {
            sb.append(iter.next());
            count--;
        }
        return sb.reverse().toString(); // Reverse because we added in reverse order
    }
}
deque "/return # @lc code=end