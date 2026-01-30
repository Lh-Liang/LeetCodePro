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
private:
    string left_side;
    string right_side;

public:
    TextEditor() {
        left_side = "";
        right_side = "";
    }
    
    void addText(string text) {
        left_side += text;
    }
    
    int deleteText(int k) {
        int numToDelete = min(k, (int)left_side.length());
        for (int i = 0; i < numToDelete; ++i) {
            left_side.pop_back();
        }
        return numToDelete;
    }
    
    string cursorLeft(int k) {
        int numToMove = min(k, (int)left_side.length());
        for (int i = 0; i < numToMove; ++i) {
            right_side.push_back(left_side.back());
            left_side.pop_back();
        }
        int len = min(10, (int)left_side.length());
        return left_side.substr(left_side.length() - len);
    }
    
    string cursorRight(int k) {
        int numToMove = min(k, (int)right_side.length());
        for (int i = 0; i < numToMove; ++i) {
            left_side.push_back(right_side.back());
            right_side.pop_back();
        }
        int len = min(10, (int)left_side.length());
        return left_side.substr(left_side.length() - len);
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