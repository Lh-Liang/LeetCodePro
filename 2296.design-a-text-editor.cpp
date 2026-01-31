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
    string left;
    string right;

public:
    TextEditor() {
        // Strings are naturally initialized to empty
    }
    
    void addText(string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int n = min(k, (int)left.size());
        left.resize(left.size() - n);
        return n;
    }
    
    string cursorLeft(int k) {
        int n = min(k, (int)left.size());
        for (int i = 0; i < n; ++i) {
            right.push_back(left.back());
            left.pop_back();
        }
        int start = max(0, (int)left.size() - 10);
        return left.substr(start);
    }
    
    string cursorRight(int k) {
        int n = min(k, (int)right.size());
        for (int i = 0; i < n; ++i) {
            left.push_back(right.back());
            right.pop_back();
        }
        int start = max(0, (int)left.size() - 10);
        return left.substr(start);
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