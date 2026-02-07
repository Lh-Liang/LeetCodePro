#
# @lc app=leetcode id=1670 lang=golang
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
type FrontMiddleBackQueue struct {
    data []int
}

func Constructor() FrontMiddleBackQueue {
    return FrontMiddleBackQueue{data: []int{}}
}

func (this *FrontMiddleBackQueue) PushFront(val int)  {
    this.data = append([]int{val}, this.data...)
}

func (this *FrontMiddleBackQueue) PushMiddle(val int)  {
    middle := len(this.data) / 2
    this.data = append(this.data[:middle], append([]int{val}, this.data[middle:]...)...)
}

func (this *FrontMiddleBackQueue) PushBack(val int)  {
    this.data = append(this.data, val)
}

func (this *FrontMiddleBackQueue) PopFront() int {
    if len(this.data) == 0 { return -1 }
    val := this.data[0]
    this.data = this.data[1:]
    return val
}

func (this *FrontMiddleBackQueue) PopMiddle() int {
    if len(this.data) == 0 { return -1 }
    middle := (len(this.data)-1) / 2
    val := this.data[middle]
    this.data = append(this.data[:middle], this.data[middle+1:]...)
    return val
}

func (this *FrontMiddleBackQueue) PopBack() int {
    if len(this.data) == 0 { return -1 }
    val := this.data[len(this.data)-1]
    this.data = this.data[:len(this.data)-1]
    return val
}
/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * param_4 := obj.PopFront();
 * param_5 := obj.PopMiddle();
 * param_6 := obj.PopBack();
 */
# @lc code=end