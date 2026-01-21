#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#
# @lc code=start
class TextEditor {
private:
    string left;  // characters to the left of cursor
    string right; // characters to the right of cursor (stored in reverse order)
    
    string getLeft10() {
        int len = left.size();
        if (len <= 10) return left;
        return left.substr(len - 10);
    }
    
public:
    TextEditor() {
    }
    
    void addText(string text) {
        left += text;
    }
    
    int deleteText(int k) {
        int deleted = min(k, (int)left.size());
        left.resize(left.size() - deleted);
        return deleted;
    }
    
    string cursorLeft(int k) {
        int moves = min(k, (int)left.size());
        for (int i = 0; i < moves; i++) {
            right.push_back(left.back());
            left.pop_back();
        }
        return getLeft10();
    }
    
    string cursorRight(int k) {
        int moves = min(k, (int)right.size());
        for (int i = 0; i < moves; i++) {
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