#
# @lc app=leetcode id=2296 lang=java
#
# [2296] Design a Text Editor
#
# @lc code=start
import java.util.Deque;
import java.util.LinkedList;
import java.util.Iterator;

class TextEditor {
    private Deque<Character> left;
    private Deque<Character> right;

    public TextEditor() {
        left = new LinkedList<>();
        right = new LinkedList<>();
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
        while (k > 0 && !left.isEmpty()) {
            right.addFirst(left.removeLast());
            k--;
        }
        return getLast10();
    }

    public String cursorRight(int k) {
        while (k > 0 && !right.isEmpty()) {
            left.addLast(right.removeFirst());
            k--;
        }
        return getLast10();
    }

    // Efficiently get the last up to 10 characters from the left stack without iterating the entire stack
    private String getLast10() {
        StringBuilder sb = new StringBuilder();
        Iterator<Character> it = left.descendingIterator();
        int cnt = 0;
        // Collect up to 10 characters from the end of the left stack
        while (it.hasNext() && cnt < 10) {
            sb.append(it.next());
            cnt++;
        }
        // Since we built the string in reverse, reverse it before returning
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