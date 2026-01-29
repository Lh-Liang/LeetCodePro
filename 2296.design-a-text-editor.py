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
        # O(len(text)) operation
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # O(k) operation: remove up to k characters from the left stack
        count = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        # O(k) operation: move up to k characters from left to right stack
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # Return last 10 characters to the left of the cursor
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # O(k) operation: move up to k characters from right to left stack
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # Return last 10 characters to the left of the cursor
        return "".join(self.left[-10:])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end