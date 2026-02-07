# @lc code=start
type TextEditor struct {
    left, right []rune
}

func Constructor() TextEditor {
    return TextEditor{left: []rune{}, right: []rune{}}
}

func (this *TextEditor) AddText(text string) {
    for _, c := range text {
        this.left = append(this.left, c)
    }
}

func (this *TextEditor) DeleteText(k int) int {
    deleteCount := min(k, len(this.left))
    this.left = this.left[:len(this.left)-deleteCount]
    return deleteCount
}

func (this *TextEditor) CursorLeft(k int) string {
    moveCount := min(k, len(this.left))
    this.right = append(this.right, this.left[len(this.left)-moveCount:]...)
    this.left = this.left[:len(this.left)-moveCount]
    return getLastTenChars(this.left)
}

func (this *TextEditor) CursorRight(k int) string {
    moveCount := min(k, len(this.right))
    this.left = append(this.left, this.right[len(this.right)-moveCount:]...)
    this.right = this.right[:len(this.right)-moveCount]
    return getLastTenChars(this.left)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func getLastTenChars(s []rune) string {
    if len(s) <= 10 {
        return string(s)
    }
    return string(s[len(s)-10:])
}
# @lc code=end