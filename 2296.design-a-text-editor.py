#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

from collections import deque

# @lc code=start
class TextEditor:

    def __init__(self):
        self.left = []
        self.right = deque()

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        cnt = min(k, len(self.left))
        for _ in range(cnt):
            self.left.pop()
        return cnt

    def cursorLeft(self, k: int) -> str:
        cnt = min(k, len(self.left))
        for _ in range(cnt):
            self.right.appendleft(self.left.pop())
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        cnt = min(k, len(self.right))
        for _ in range(cnt):
            self.left.append(self.right.popleft())
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end