#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
#include <deque>
#include <string>
#include <algorithm>

class TextEditor {
public:
    TextEditor() {

    }
    
    void addText(std::string text) {
        for (char c : text) {
            left_.push_back(c);
        }
    }
    
    int deleteText(int k) {
        int deleted = 0;
        while (deleted < k && !left_.empty()) {
            left_.pop_back();
            ++deleted;
        }
        return deleted;
    }
    
    std::string cursorLeft(int k) {
        int steps = std::min(k, static_cast<int>(left_.size()));
        for (int i = 0; i < steps; ++i) {
            char c = left_.back();
            left_.pop_back();
            right_.push_front(c);
        }
        return getLeftString();
    }
    
    std::string cursorRight(int k) {
        int steps = std::min(k, static_cast<int>(right_.size()));
        for (int i = 0; i < steps; ++i) {
            char c = right_.front();
            right_.pop_front();
            left_.push_back(c);
        }
        return getLeftString();
    }

private:
    std::deque<char> left_;
    std::deque<char> right_;
    
    std::string getLeftString() {
        size_t len = left_.size();
        size_t m = std::min(10UL, len);
        std::string res;
        res.reserve(m);
        for (size_t i = len - m; i < len; ++i) {
            res += left_[i];
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
