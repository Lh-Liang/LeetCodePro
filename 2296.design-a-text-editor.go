#
# @lc app=leetcode id=2296 lang=golang
#
# [2296] Design a Text Editor
#

# @lc code=start
type TextEditor struct {
    left  []byte // characters to the left of cursor
    right []byte // characters to the right of cursor
}

func Constructor() TextEditor {
    return TextEditor{
        left:  make([]byte, 0),
        right: make([]byte, 0),
    }
}

func (this *TextEditor) AddText(text string)  {
    this.left = append(this.left, text...)
}

func (this *TextEditor) DeleteText(k int) int {
    actual := k
    if len(this.left) < k {
        actual = len(this.left)
    }
    this.left = this.left[:len(this.left)-actual]
    return actual
}

func (this *TextEditor) CursorLeft(k int) string {
    move := k
    if len(this.left) < k {
        move = len(this.left)
    }
    this.right = append(this.right, this.left[len(this.left)-move:]...)
    this.left = this.left[:len(this.left)-move]
    l := len(this.left)
    start := l - 10
    if start < 0 {
        start = 0
    }
    return string(this.left[start:])
}

func (this *TextEditor) CursorRight(k int) string {
    move := k
    if len(this.right) < k {
        move = len(this.right)
    }
    this.left = append(this.left, this.right[len(this.right)-move:]...)
    this.right = this.right[:len(this.right)-move]
    l := len(this.left)
    start := l - 10
    if start < 0 {
        start = 0
    }
    return string(this.left[start:])
}

# @lc code=end