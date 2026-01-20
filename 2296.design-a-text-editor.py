#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        del_count = min(k, len(self.left))
        for _ in range(del_count):
            self.left.pop()
        return del_count

    def cursorLeft(self, k: int) -> str:
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        n = len(self.left)
        pl = min(10, n)
        return ''.join(self.left[-pl:]) if pl > 0 else ""

    def cursorRight(self, k: int) -> str:
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        n = len(self.left)
        pl = min(10, n)
        return ''.join(self.left[-pl:]) if pl > 0 else ""


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end