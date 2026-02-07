//
// @lc app=leetcode id=3768 lang=golang
//
// [3768] Minimum Inversion Count in Subarrays of Fixed Length
//

// @lc code=start
func minInversionCount(nums []int, k int) int64 {
    n := len(nums)
    if k == 1 {
        return 0 // No inversions possible in single-element subarrays
    }
    
    // Define a Fenwick Tree structure
    type FenwickTree struct {
        tree []int64
        size int
    }
    
    // Initialize Fenwick Tree
    func (ft *FenwickTree) init(size int) {
        ft.tree = make([]int64, size+1)
        ft.size = size
    }
    
    // Update function for Fenwick Tree
    func (ft *FenwickTree) update(index int, delta int64) {
        for i := index; i <= ft.size; i += i & (-i) {
            ft.tree[i] += delta
        }
    }
    
    // Prefix sum query for Fenwick Tree
    func (ft *FenwickTree) query(index int) int64 {
        var sum int64 = 0
        for i := index; i > 0; i -= i & (-i) {
            sum += ft.tree[i]
        }
        return sum
    }
    
    // Coordinate compression map to ensure indices fit within tree size limits
    coordinateMap := make(map[int]int)
    sortedNums := make([]int, n)
    copy(sortedNums, nums)
    sort.Ints(sortedNums)
    idx := 1 // Start indices from 1 for Fenwick Tree compatibility
    for _, num := range sortedNums {
        if _, exists := coordinateMap[num]; !exists {
            coordinateMap[num] = idx
            idx++
        }
    }
    
    fenwickTree := FenwickTree{}
    fenwickTree.init(len(coordinateMap))
    															minInversions := int64(^uint64(0) >> 1) // Max integer value as initial min inversion count// Sliding Window Algorithm with Inversion Counting using a Fenwick Tree.for startIdx := 0; startIdx+k <= n; startIdx++ {if startIdx > 0 { prevIndexMapped := coordinateMap[nums[startIdx-1]] fenwickTree.update(prevIndexMapped, -1)} inversionsInWindow := int64(0)	for j := startIdx; j < startIdx+k; j++ {indexMapped := coordinateMap[nums[j]]inversionsInWindow += fenwickTree.query(fenwickTree.size) - fenwickTree.query(indexMapped)	fenwickTree.update(indexMapped, 1)}if inversionsInWindow < minInversions {minInversions = inversionsInWindow}}return minInversions}// @lc code=end