#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.left = []  # Characters to the left of the cursor
        self.right = []  # Characters to the right of the cursor
    
    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)
    
    def deleteText(self, k: int) -> int:
        delete_count = min(k, len(self.left))
        while delete_count > 0:
            self.left.pop()
            delete_count -= 1
        return k - delete_count
    
    def cursorLeft(self, k: int) -> str:
        move_count = min(k, len(self.left))
        while move_count > 0:
            self.right.append(self.left.pop())
            move_count -= 1
        return ''.join(self.left[-10:]) if len(self.left) > 10 else ''.join(self.left)
    
    def cursorRight(self, k: int) -> str:
        move_count = min(k, len(self.right))
        while move_count > 0:
            self.left.append(self.right.pop())
            move_count -= 1
        return ''.join(self.left[-10:]) if len(self.left) > 10 else ''.join(self.left)