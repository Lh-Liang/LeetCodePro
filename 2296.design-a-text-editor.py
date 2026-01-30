#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.left = []  # stack for text to the left of cursor
        self.right = []  # stack for text to the right of cursor

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        count = 0
        while self.left and count < k:
            self.left.pop()
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        return ''.join(self.left[-10:])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end