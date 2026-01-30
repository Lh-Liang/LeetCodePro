#
# @lc app=leetcode id=2296 lang=python3
#
# [2296] Design a Text Editor
#

# @lc code=start
class TextEditor:
    def __init__(self):
        self.left = []  # stack to store characters on the left of the cursor
        self.right = []  # stack to store characters on the right of the cursor

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)  # add characters to the left stack
        
    def deleteText(self, k: int) -> int:
        delete_count = 0
        while k > 0 and self.left:
            self.left.pop()  # remove characters from left stack
            delete_count += 1
            k -= 1
        return delete_count
    
    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.append(self.left.pop())  # move character from left stack to right stack
            k -= 1
        return ''.join(self.left[-10:])  # return last up to 10 chars from left stack as string
    
    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.pop())  # move character from right stack to left stack
            k -= 1
        return ''.join(self.left[-10:])  # return last up to 10 chars from left stack as string
# @lc code=end