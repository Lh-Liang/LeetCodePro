#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
public:
    TextEditor() {
        // left and right hold the text to the left and right of the cursor
    }

    void addText(string text) {
        left += text;
    }

    int deleteText(int k) {
        int cnt = min(k, (int)left.size());
        left.erase(left.size() - cnt, cnt);
        return cnt;
    }

    string cursorLeft(int k) {
        int move = min(k, (int)left.size());
        right = left.substr(left.size() - move, move) + right;
        left.erase(left.size() - move, move);
        return left.substr(left.size() - min(10, (int)left.size()));
    }

    string cursorRight(int k) {
        int move = min(k, (int)right.size());
        left += right.substr(0, move);
        right.erase(0, move);
        return left.substr(left.size() - min(10, (int)left.size()));
    }

private:
    string left, right;
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