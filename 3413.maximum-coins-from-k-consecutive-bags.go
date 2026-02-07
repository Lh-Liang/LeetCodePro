#
# @lc app=leetcode id=3413 lang=golang
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
func maximumCoins(coins [][]int, k int) int64 {
    type interval struct {
        l, r int
        val  int
    }
    n := len(coins)
    segs := make([]interval, n)
    minL, maxR := 1<<60, 0
    for i, c := range coins {
        l, r, v := c[0], c[1], c[2]
        segs[i] = interval{l, r, v}
        if l < minL {
            minL = l
        }
        if r > maxR {
            maxR = r
        }
    }
    sort.Slice(segs, func(i, j int) bool { return segs[i].l < segs[j].l })
    intervals := make([]interval, 0, n*2+2)
    last := minL
    idx := 0
    curr := minL
    for idx < n {
        if curr < segs[idx].l {
            intervals = append(intervals, interval{curr, segs[idx].l - 1, 0})
            curr = segs[idx].l
        }
        intervals = append(intervals, interval{segs[idx].l, segs[idx].r, segs[idx].val})
        curr = segs[idx].r + 1
        idx++
    }
    if curr <= maxR {
        intervals = append(intervals, interval{curr, maxR, 0})
    }
    // For k-length window, we can also consider bags before minL or after maxR (zero coins)
    // Extend intervals at both sides if needed
    intervals = append([]interval{{minL - k, minL - 1, 0}}, intervals...)
    intervals = append(intervals, interval{maxR + 1, maxR + k, 0})

    // Build prefix sums for intervals
    psLen := make([]int, len(intervals)+1)
    psCoin := make([]int64, len(intervals)+1)
    for i, it := range intervals {
        l := it.r - it.l + 1
        psLen[i+1] = psLen[i] + l
        psCoin[i+1] = psCoin[i] + int64(l)*int64(it.val)
    }
    // Sliding window over the intervals
    maxSum := int64(0)
    for i := 0; i < len(intervals); i++ {
        // Binary search to find the rightmost interval so that window covers k bags
        lo, hi := i, len(intervals)-1
        need := psLen[i] + k
        for lo < hi {
            mid := (lo + hi) / 2
            if psLen[mid+1] >= need {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        end := lo
        // sum from i to end-1, and partial for end
        sum := psCoin[end] - psCoin[i]
        leftBags := psLen[end] - psLen[i]
        remain := k - leftBags
        if remain > 0 {
            sum += int64(remain) * int64(intervals[end].val)
        }
        if sum > maxSum {
            maxSum = sum
        }
    }
    return maxSum
}
# @lc code=end