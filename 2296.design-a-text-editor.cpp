#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
    std::deque<char> left, right;
public:
    TextEditor() {}
    void addText(std::string text) {
        for (char c : text) left.push_back(c);
    }
    int deleteText(int k) {
        int count = 0;
        while (!left.empty() && k > 0) {
            left.pop_back();
            --k; 
            ++count; 
        } 
        return count; 
    } 
    std::string cursorLeft(int k) { 
        while (k > 0 && !left.empty()) { 
            right.push_front(left.back()); 
            left.pop_back(); 
            --k; 
        } 
        return getLeftContext(); 
    } 
    std::string cursorRight(int k) { 
        while (k > 0 && !right.empty()) { 
            left.push_back(right.front()); 
            right.pop_front(); 
            --k; 
        } 
        return getLeftContext(); 
    } 
private: 
    std::string getLeftContext() { 
        int len = std::min(10, (int)left.size());
        std::string result; result.reserve(len);  for (int i = left.size() - len; i < left.size(); ++i) result += left[i];
 return result;
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