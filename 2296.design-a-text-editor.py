#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:

    def __init__(self):
        # Left holds characters to the left of cursor
        # Right holds characters to the right of cursor
        # Both are lists used as stacks
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        # Add each character to the end of left
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k: int) -> int:
        # Delete up to k characters from the end of left
        cnt = min(k, len(self.left))
        for _ in range(cnt):
            self.left.pop()
        return cnt

    def _last_chars(self) -> str:
        # Return up to last ten characters currently in left
        n = len(self.left)
        start = max(0, n - 10)
        return ''.join(self.left[start:])

    def cursorLeft(self, k: int) -> str:
        # Move k steps to the left
        steps = min(k, len(self.left))
        for _ in range(steps):
            ch = self.left.pop()
            self.right.append(ch)
        # Return last up to ten characters
        return self._last_chars()

    def cursorRight(self, k: int) -> str:
        # Move k steps to the right
        steps = min(k, len(self.right))
        for _ in range(steps):
            ch = self.right.pop()
            self.left.append(ch)
        # Return last up to ten characters
        return self._last_chars()

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end