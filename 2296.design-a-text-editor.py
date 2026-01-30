#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.before = []  # Stack for characters before the cursor
        self.after = []   # Stack for characters after the cursor (reversed)

    def addText(self, text: str) -> None:
        self.before.extend(text)  # Add new text at cursor position

    def deleteText(self, k: int) -> int:
        deleted_count = min(k, len(self.before))  # Ensure we don't delete more than exists
        for _ in range(deleted_count):
            self.before.pop()  # Remove characters from before stack (backspace behavior)
        return deleted_count  # Return actual number of deleted characters

    def cursorLeft(self, k: int) -> str:
        move_count = min(k, len(self.before))  # Move left but not more than available characters
        for _ in range(move_count):
            self.after.append(self.before.pop())  # Move character to after stack (left movement)
        return ''.join(self.before[-10:])  # Return last up to 10 chars from before stack as string

    def cursorRight(self, k: int) -> str:
        move_count = min(k, len(self.after))  # Move right but not more than available characters in after stack
        for _ in range(move_count):
            self.before.append(self.after.pop())  # Move character to before stack (right movement)
        return ''.join(self.before[-10:])  # Return last up to 10 chars from before stack as string\@lc code=end