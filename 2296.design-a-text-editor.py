#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#
# @lc code=start
class TextEditor:

    def __init__(self):
        # Use two stacks to represent left and right parts of cursor
        # left stack: characters to the left of cursor
        # right stack: characters to the right of cursor (in reverse order)
        self.left = []   # Stack for characters to the left of cursor
        self.right = []  # Stack for characters to the right of cursor

    def addText(self, text: str) -> None:
        # Add all characters to the left stack
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # Delete at most k characters from left stack
        deleted = 0
        while deleted < k and self.left:
            self.left.pop()
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        # Move cursor left by moving characters from left to right stack
        moves = 0
        while moves < k and self.left:
            char = self.left.pop()
            self.right.append(char)
            moves += 1
        
        # Return last min(10, len) characters to the left of cursor
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move cursor right by moving characters from right to left stack
        moves = 0
        while moves < k and self.right:
            char = self.right.pop()
            self.left.append(char)
            moves += 1
        
        # Return last min(10, len) characters to the left of cursor
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end