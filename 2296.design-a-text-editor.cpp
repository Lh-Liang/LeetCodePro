#include <string>
#include <algorithm>

#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
private:
    std::string left;
    std::string right;

public:
    TextEditor() {
        left = "";
        right = "";
    }
    
    void addText(std::string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int toDelete = std::min(k, (int)left.size());
        left.resize(left.size() - toDelete);
        return toDelete;
    }
    
    std::string cursorLeft(int k) {
        int toMove = std::min(k, (int)left.size());
        for (int i = 0; i < toMove; ++i) {
            right.push_back(left.back());
            left.pop_back();
        }
        int start = (left.size() > 10) ? (left.size() - 10) : 0;
        return left.substr(start);
    }
    
    std::string cursorRight(int k) {
        int toMove = std::min(k, (int)right.size());
        for (int i = 0; i < toMove; ++i) {
            left.push_back(right.back());
            right.pop_back();
        }
        int start = (left.size() > 10) ? (left.size() - 10) : 0;
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