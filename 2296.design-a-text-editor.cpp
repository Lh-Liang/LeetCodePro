#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
public:
    std::stack<char> left, right;
    TextEditor() {
    }
    void addText(std::string text) {
        for(char c : text) left.push(c);
    }
    int deleteText(int k) {
        int cnt = 0;
        while(!left.empty() && k--) {
            left.pop();
            ++cnt;
        }
        return cnt;
    }
    std::string cursorLeft(int k) {
        while(k-- && !left.empty()) {
            right.push(left.top());
            left.pop();
        }
        return getLast10();
    }
    std::string cursorRight(int k) {
        while(k-- && !right.empty()) {
            left.push(right.top());
            right.pop();
        }
        return getLast10();
    }
private:
    std::string getLast10() {
        std::string res;
        std::stack<char> tmp;
        int cnt = 0;
        // move up to 10 chars to tmp to reverse, and restore afterward
        while(cnt < 10 && !left.empty()) {
            tmp.push(left.top());
            left.pop();
            cnt++;
        }
        while(!tmp.empty()) {
            res.push_back(tmp.top());
            left.push(tmp.top()); // restore
            tmp.pop();
        }
        return res;
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