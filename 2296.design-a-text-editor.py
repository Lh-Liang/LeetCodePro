#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:

    def __init__(self):
        # Characters to the left of the cursor
        self.left = []
        # Characters to the right of the cursor (stored in reverse order)
        self.right = []

    def addText(self, text: str) -> None:
        # Add characters to the left stack; cursor ends to the right of text
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # Delete up to k characters to the left of the cursor
        count = 0
        while k > 0 and self.left:
            self.left.pop()
            count += 1
            k -= 1
        return count

    def cursorLeft(self, k: int) -> str:
        # Move cursor left: transfer chars from left to right stack
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # Return last min(10, len) characters to the left of cursor
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move cursor right: transfer chars from right to left stack
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # Return last min(10, len) characters to the left of cursor
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end