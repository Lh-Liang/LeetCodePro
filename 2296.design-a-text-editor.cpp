#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class TextEditor {
private:
    string left;
    string right;

public:
    TextEditor() {
        // Initializes with empty text
    }
    
    void addText(string text) {
        // Appends text to where the cursor is (end of 'left')
        left += text;
    }
    
    int deleteText(int k) {
        // Deletes k characters to the left of the cursor
        int count = min((int)left.size(), k);
        left.resize(left.size() - count);
        return count;
    }
    
    string cursorLeft(int k) {
        // Moves cursor left k times
        // Move characters from 'left' end to 'right' end
        int count = min((int)left.size(), k);
        for (int i = 0; i < count; ++i) {
            right.push_back(left.back());
            left.pop_back();
        }
        return getLeftString();
    }
    
    string cursorRight(int k) {
        // Moves cursor right k times
        // Move characters from 'right' end to 'left' end
        int count = min((int)right.size(), k);
        for (int i = 0; i < count; ++i) {
            left.push_back(right.back());
            right.pop_back();
        }
        return getLeftString();
    }

private:
    string getLeftString() {
        // Returns the last min(10, len) characters to the left of the cursor
        int len = left.size();
        int start = max(0, len - 10);
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