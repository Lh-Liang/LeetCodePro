#
# @lc app=leetcode id=3739 lang=golang
#
# [3739] Count Subarrays With Majority Element II
#
# @lc code=start
func countMajoritySubarrays(nums []int, target int) int64 {
    n := len(nums)
    prefix := make([]int, n+1)
    for i, v := range nums {
        if v == target {
            prefix[i+1] = prefix[i] + 1
        } else {
            prefix[i+1] = prefix[i] - 1
        }
    }
    // To count for each i, number of j < i such that prefix[i] > prefix[j]
    // Use a map to count frequency of prefix sums
    // For efficient counting, use a sorted list of prefix sums
    // But since values can be negative, compress values
    allPrefix := make([]int, n+1)
    copy(allPrefix, prefix)
    // Coordinate compression
    valMap := make(map[int]int)
    uniq := make([]int, 0)
    for _, v := range allPrefix {
        valMap[v] = 1
    }
    for k := range valMap {
        uniq = append(uniq, k)
    }
    sort.Ints(uniq)
    for i, v := range uniq {
        valMap[v] = i
    }
    // Fenwick Tree
    type BIT struct {
        tree []int
    }
    func (b *BIT) add(i, x int) {
        for i < len(b.tree) {
            b.tree[i] += x
            i += i & -i
        }
    }
    func (b *BIT) sum(i int) int {
        res := 0
        for i > 0 {
            res += b.tree[i]
            i -= i & -i
        }
        return res
    }
    size := len(uniq) + 2
    bit := &BIT{tree: make([]int, size)}
    var ans int64 = 0
    for i := 0; i <= n; i++ {
        idx := valMap[prefix[i]] + 1
        // For i, number of prefix[j] < prefix[i] is sum(idx-1)
        ans += int64(bit.sum(idx - 1))
        bit.add(idx, 1)
    }
    return ans
}
# @lc code=end