#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
#include <string>
#include <algorithm>

using namespace std;

class TextEditor {
    // left stores characters to the left of the cursor
    // right stores characters to the right of the cursor in reverse order
    string left, right;

public:
    TextEditor() {
    }
    
    void addText(string text) {
        // O(text.length) - Appending to the end of left string
        left += text;
    }
    
    int deleteText(int k) {
        // O(k) - Removing from the end of left string
        int actual_deleted = min(k, (int)left.size());
        for (int i = 0; i < actual_deleted; ++i) {
            left.pop_back();
        }
        return actual_deleted;
    }
    
    string cursorLeft(int k) {
        // O(k) - Moving characters from left to right stack
        int move_count = min(k, (int)left.size());
        for (int i = 0; i < move_count; ++i) {
            right.push_back(left.back());
            left.pop_back();
        }
        return getLeft10();
    }
    
    string cursorRight(int k) {
        // O(k) - Moving characters from right to left stack
        int move_count = min(k, (int)right.size());
        for (int i = 0; i < move_count; ++i) {
            left.push_back(right.back());
            right.pop_back();
        }
        return getLeft10();
    }

private:
    // Helper to get up to 10 characters to the left of the cursor
    string getLeft10() {
        int len = min(10, (int)left.size());
        return left.substr(left.size() - len);
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
# @lc code=end