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
        # Characters to the right of the cursor (top of stack is closest to cursor)
        self.right = []

    def addText(self, text: str) -> None:
        # O(L) where L is length of text
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # O(k)
        count = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        # O(k) - shift characters from left stack to right stack
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # Return last min(10, len) characters to the left of cursor
        # Slicing the last 10 elements takes O(1) time
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # O(k) - shift characters from right stack to left stack
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # Return last min(10, len) characters to the left of cursor
        return "".join(self.left[-10:])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end