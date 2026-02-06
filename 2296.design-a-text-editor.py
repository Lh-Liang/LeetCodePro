#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.left = []  # List to store characters left of the cursor
        self.right = [] # List to store characters right of the cursor

    def addText(self, text: str) -> None:
        # Append each character in 'text' to 'left' where the cursor is currently located.
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        # Delete up to 'k' characters from 'left', simulating backspace.
        delete_count = min(k, len(self.left))
        for _ in range(delete_count):
            self.left.pop()
        return delete_count  # Return number of characters actually deleted.

    def cursorLeft(self, k: int) -> str:
        # Move up to 'k' characters from 'left' to 'right'.
        move_count = min(k, len(self.left))
        for _ in range(move_count):
            self.right.append(self.left.pop())
        # Return last 10 chars or all chars if less than 10 on 'left'.
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move up to 'k' characters from 'right' back into 'left'.
        move_count = min(k, len(self.right))
        for _ in range(move_count):
            self.left.append(self.right.pop())
        # Return last 10 chars or all chars if less than 10 on 'left'.
        return ''.join(self.left[-10:])
# @lc code=end