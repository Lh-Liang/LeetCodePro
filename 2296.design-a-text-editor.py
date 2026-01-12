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
        # Characters to the right of the cursor (in reverse order)
        self.right = []

    def addText(self, text: str) -> None:
        # O(len(text)) time complexity
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        # O(k) time complexity
        num_to_delete = min(k, len(self.left))
        if num_to_delete > 0:
            del self.left[-num_to_delete:]
        return num_to_delete

    def cursorLeft(self, k: int) -> str:
        # O(k) time complexity
        num_to_move = min(k, len(self.left))
        for _ in range(num_to_move):
            self.right.append(self.left.pop())
        # Return up to last 10 characters to the left of cursor
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # O(k) time complexity
        num_to_move = min(k, len(self.right))
        for _ in range(num_to_move):
            self.left.append(self.right.pop())
        # Return up to last 10 characters to the left of cursor
        return "".join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end