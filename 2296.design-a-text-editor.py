#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.left = []  # Stack for text left of the cursor
        self.right = [] # Stack for text right of the cursor

    def addText(self, text: str) -> None:
        self.left.extend(text)
        # Cursor moves to end of added text (implicit by stack nature)

    def deleteText(self, k: int) -> int:
        count = min(k, len(self.left))
        del self.left[-count:]  # Efficiently remove last `count` elements using slicing
        return count  # Number of actually deleted characters

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop()) # Move character from left stack to right stack
        return ''.join(self.left[-10:])  # Return last 10 chars or fewer from left side

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop()) # Move character from right stack to left stack
        return ''.join(self.left[-10:])  # Return last 10 chars or fewer from left side 
# @lc code=end