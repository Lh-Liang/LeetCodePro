#
# @lc app=leetcode id=2296 lang=golang
#
# [2296] Design a Text Editor
#

# @lc code=start
type TextEditor struct {
    left  []rune // holds characters to the left of the cursor
    right []rune // holds characters to the right of the cursor
}

func Constructor() TextEditor {
    return TextEditor{left: []rune{}, right: []rune{}}
}

func (this *TextEditor) AddText(text string) {
    this.left = append(this.left, []rune(text)...)
}

func (this *TextEditor) DeleteText(k int) int {
    deleteCount := min(k, len(this.left))
    this.left = this.left[:len(this.left)-deleteCount]
    return deleteCount
}

func (this *TextEditor) CursorLeft(k int) string {
    moveCount := min(k, len(this.left))
    this.right = append(this.left[len(this.left)-moveCount:], this.right...)
    this.left = this.left[:len(this.left)-moveCount]
    return string(this.left[max(0, len(this.left)-10):])
}

func (this *TextEditor) CursorRight(k int) string {
    moveCount := min(k, len(this.right))
    this.left = append(this.left, this.right[:moveCount]...)
    this.right = this.right[moveCount:]
    return string(this.left[max(0, len(this.left)-10):])
}
// Helper functions to get min and max of two integers. 
func min(a, b int) int { if a < b { return a } else { return b } } 
func max(a, b int) int { if a > b { return a } else { return b } } 
bject will be instantiated and called as such: obj := Constructor(); obj.AddText(text); param_2 := obj.DeleteText(k); param_3 := obj.CursorLeft(k); param_4 := obj.CursorRight(k);