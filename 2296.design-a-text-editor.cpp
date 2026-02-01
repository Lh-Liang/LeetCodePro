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

public:
    TextEditor() {
        left = "";
        right = "";
    }
    
    void addText(string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int toDelete = min(k, (int)left.size());
        left.resize(left.size() - toDelete);
        return toDelete;
    }
    
    string cursorLeft(int k) {
        int toMove = min(k, (int)left.size());
        for (int i = 0; i < toMove; ++i) {
            right.push_back(left.back());
            left.pop_back();
        }
        int len = min(10, (int)left.size());
        return left.substr(left.size() - len);
    }
    
    string cursorRight(int k) {
        int toMove = min(k, (int)right.size());
        for (int i = 0; i < toMove; ++i) {
            left.push_back(right.back());
            right.pop_back();
        }
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