#include <string>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
private:
    string left;
    string right;

    // Helper to get the last min(10, len) characters to the left of the cursor
    string getLeft10() {
        int len = min(10, (int)left.size());
        return left.substr(left.size() - len);
    }

public:
    TextEditor() {
    }
    
    void addText(string text) {
        left.append(text);
    }
    
    int deleteText(int k) {
        int toDelete = min(k, (int)left.size());
        for (int i = 0; i < toDelete; ++i) {
            left.pop_back();
        }
        return toDelete;
    }
    
    string cursorLeft(int k) {
        int toMove = min(k, (int)left.size());
        while (toMove--) {
            right.push_back(left.back());
            left.pop_back();
        }
        return getLeft10();
    }
    
    string cursorRight(int k) {
        int toMove = min(k, (int)right.size());
        while (toMove--) {
            left.push_back(right.back());
            right.pop_back();
        }
        return getLeft10();
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