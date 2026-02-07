#
# @lc app=leetcode id=2296 lang=cpp
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor {
public:
    std::deque<char> left; // Characters to the left of the cursor
    std::deque<char> right; // Characters to the right of the cursor
    
    TextEditor() {
        // Initially, both sides are empty
    }
    
    void addText(std::string text) {
        for (char c : text) {
            left.push_back(c); // Add each character to the left deque where the cursor is
        }
    }
    
    int deleteText(int k) {
        int count = 0;
        while (k > 0 && !left.empty()) {
            left.pop_back(); // Remove characters from left of cursor up to k times or until empty
            k--; count++;
        }
        return count; // Return number of characters actually deleted
    }
    
    std::string cursorLeft(int k) {
        while (k > 0 && !left.empty()) {
            right.push_front(left.back()); // Move characters from left to right up to k times or until left is empty
            left.pop_back(); k--; 
        }
        return getLeftView(); // Return viewable string from left deque after moving cursor left
    }
    
    std::string cursorRight(int k) {
        while (k > 0 && !right.empty()) {
            left.push_back(right.front()); // Move characters from right to left up to k times or until right is empty
            right.pop_front(); k--; 
        }  	     	     	     	     	       	     	       return getLeftView(); // Return viewable string from left deque after moving cursor right   	     	}         	     	               std::string getLeftView() {       int len = std::min(10, (int)left.size()); return std::string(left.end() - len, left.end());   }   }; /* Your TextEditor object will be instantiated and called as such: TextEditor* obj = new TextEditor(); obj->addText(text); int param_2 = obj->deleteText(k); std::string param_3 = obj->cursorLeft(k); std::string param_4 = obj->cursorRight(k); */ # @lc code=end