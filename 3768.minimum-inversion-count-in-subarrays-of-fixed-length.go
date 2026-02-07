#
# @lc app=leetcode id=3768 lang=golang
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
func minInversionCount(nums []int, k int) int64 {
    n := len(nums)
    values := make([]int, n)
    copy(values, nums)
    sort.Ints(values)
    valueToRank := make(map[int]int)
    rank := 1
    for _, v := range values {
        if _, ok := valueToRank[v]; !ok {
            valueToRank[v] = rank
            rank++
        }
    }
    arr := make([]int, n)
    for i, v := range nums {
        arr[i] = valueToRank[v]
    }
    maxRank := rank

    type BIT struct {
        tree []int
        size int
    }
    func newBIT(s int) *BIT {
        return &BIT{make([]int, s+2), s+2}
    }
    func (b *BIT) update(i, delta int) {
        for i < b.size {
            b.tree[i] += delta
            i += i & -i
        }
    }
    func (b *BIT) query(i int) int {
        res := 0
        for i > 0 {
            res += b.tree[i]
            i -= i & -i
        }
        return res
    }

    bit := newBIT(maxRank)
    inv := int64(0)
    // Build initial window
    for i := 0; i < k; i++ {
        inv += int64(i - bit.query(arr[i]))
        bit.update(arr[i], 1)
    }
    minInv := inv
    for i := k; i < n; i++ {
        // Remove arr[i-k]: before removal, subtract its contribution
        removeVal := arr[i-k]
        bit.update(removeVal, -1)
        inv -= int64(bit.query(removeVal-1))
        // Add arr[i]: before insert, add its contribution
        addVal := arr[i]
        inv += int64(bit.query(maxRank-1) - bit.query(addVal))
        bit.update(addVal, 1)
        if inv < minInv {
            minInv = inv
        }
    }
    return minInv
}
# @lc code=end