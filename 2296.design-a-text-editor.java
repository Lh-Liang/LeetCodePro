#
# @lc app=leetcode id=2296 lang=java
#
# [2296] Design a Text Editor
#

# @lc code=start
import java.util.*;
class TextEditor {
    Deque<Character> left;
    Deque<Character> right;
    public TextEditor() {
        left = new ArrayDeque<>();
        right = new ArrayDeque<>();
    }
    public void addText(String text) {
        for (char c : text.toCharArray()) {
            left.addLast(c);
        }
    }
    public int deleteText(int k) {
        int deleted = 0;
        while (deleted < k && !left.isEmpty()) {
            left.removeLast();
            deleted++;
        }
        return deleted;
    }
    public String cursorLeft(int k) {
        int moved = 0;
        while (moved < k && !left.isEmpty()) {
            right.addFirst(left.removeLast());
            moved++;
        }
        return getLast10();
    }
    public String cursorRight(int k) {
        int moved = 0;
        while (moved < k && !right.isEmpty()) {
            left.addLast(right.removeFirst());
            moved++;
        }
        return getLast10();
    }
    private String getLast10() {
        StringBuilder sb = new StringBuilder();
        Iterator<Character> it = left.descendingIterator();
        int cnt = 0;
        while (it.hasNext() && cnt < 10) {
            sb.append(it.next());
            cnt++;
        }
        return sb.reverse().toString();
    }
}
/**
* Your TextEditor object will be instantiated and called as such:
* TextEditor obj = new TextEditor();
* obj.addText(text);
* int param_2 = obj.deleteText(k);
* String param_3 = obj.cursorLeft(k);
* String param_4 = obj.cursorRight(k);
*/
# @lc code=end