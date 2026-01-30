#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:

    def __init__(self):
        self.left = []  # stack for text to the left of the cursor
        self.right = []  # stack for text to the right of the cursor

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while self.left and deleted < k:
            self.left.pop()
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        moved = 0
        while self.left and moved < k:
            self.right.append(self.left.pop())
            moved += 1
        # Return last min(10, len(self.left)) chars as a string
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        moved = 0
        while self.right and moved < k:
            self.left.append(self.right.pop())
            moved += 1
        return ''.join(self.left[-10:])

# @lc code=end