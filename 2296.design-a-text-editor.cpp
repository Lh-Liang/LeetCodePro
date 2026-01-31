#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
#include <string>
#include <algorithm>
#include <stack>

using namespace std;

class TextEditor {
private:
    string left;
    string right;

public:
    TextEditor() {
    }
    
    void addText(string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int numToDelete = min((int)left.length(), k);
        left.erase(left.length() - numToDelete);
        return numToDelete;
    }
    
    string cursorLeft(int k) {
        int numToMove = min((int)left.length(), k);
        for (int i = 0; i < numToMove; ++i) {
            right += left.back();
            left.pop_back();
        }
        return getLeftTen();
    }
    
    string cursorRight(int k) {
        int numToMove = min((int)right.length(), k);
        for (int i = 0; i < numToMove; ++i) {
            left += right.back();
            right.pop_back();
        }
        return getLeftTen();
    }

    string getLeftTen() {
        int len = min((int)left.length(), 10);
        return left.substr(left.length() - len);
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