class TextEditor:

    def __init__(self):
        # Characters to the left of the cursor
        self.left = []
        # Characters to the right of the cursor (top of stack is closest to cursor)
        self.right = []

    def addText(self, text: str) -> None:
        # Add characters to the left stack
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        # Delete characters to the left of the cursor
        num_to_delete = min(k, len(self.left))
        for _ in range(num_to_delete):
            self.left.pop()
        return num_to_delete

    def cursorLeft(self, k: int) -> str:
        # Move cursor left: move characters from left stack to right stack
        num_to_move = min(k, len(self.left))
        for _ in range(num_to_move):
            self.right.append(self.left.pop())
        # Return the last 10 characters to the left of the cursor
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # Move cursor right: move characters from right stack to left stack
        num_to_move = min(k, len(self.right))
        for _ in range(num_to_move):
            self.left.append(self.right.pop())
        # Return the last 10 characters to the left of the cursor
        return "".join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)