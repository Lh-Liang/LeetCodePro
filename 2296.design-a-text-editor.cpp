#\n# @lc app=leetcode id=2296 lang=cpp\n#\n# [2296] Design a Text Editor\n#\n# @lc code=start\nclass TextEditor {\npublic:\n    std::string leftText;\n    std::string rightText;\n    \n    TextEditor() {}\n    \n    void addText(std::string text) {\n        leftText += text;\n    }\n    \n    int deleteText(int k) {\n        int count = std::min(k, static_cast<int>(leftText.size()));\n        leftText.erase(leftText.end() - count, leftText.end());\n        return count;\n    }\n    \n    std::string cursorLeft(int k) {\n        int moveCount = std::min(k, static_cast<int>(leftText.size()));\n        rightText.insert(rightText.begin(), leftText.end() - moveCount, leftText.end());\n        leftText.erase(leftText.end() - moveCount, leftText.end());\n        return getLeftContext();   \nn}\nnstd::string cursorRight(int k) {nnint moveCount = std::min(k, static_cast<int>(rightText.size()));nnleftText.append(rightText.begin(), rightText.begin() + moveCount);nnrightText.erase(rightText.begin(), rightText.begin() + moveCount);nnreturn getLeftContext();   \nn}nnprivate:nnstd::string getLeftContext() const {nnint len = std::min(10, static_cast<int>(leftText.size()));nnreturn leftText.substr(leftText.size() - len); nn}\nn};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * std::string param_3 = obj->cursorLeft(k);
 * std::string param_4 = obj->cursorRight(k);
 */
# @lc code=end