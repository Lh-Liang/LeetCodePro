#
# @lc app=leetcode id=3757 lang=golang
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
func countEffective(nums []int) int {
    mod := int(1e9 + 7)
    n := len(nums)
    totalOR := 0
    for _, x := range nums {
        totalOR |= x
    }
    // Step 2: For each bit in totalOR, find indices that contribute to the bit
    var bitContrib [][]int
    for bit := 0; bit < 21; bit++ {
        if (totalOR>>bit)&1 == 1 {
            var indices []int
            for i, x := range nums {
                if (x>>bit)&1 == 1 {
                    indices = append(indices, i)
                }
            }
            bitContrib = append(bitContrib, indices)
        }
    }
    m := len(bitContrib)
    res := 0
    // Step 4: Inclusion-Exclusion Principle
    for mask := 1; mask < (1<<m); mask++ {
        contribSet := make(map[int]struct{})
        bits := 0
        for j := 0; j < m; j++ {
            if (mask>>j)&1 == 1 {
                bits++
                for _, idx := range bitContrib[j] {
                    contribSet[idx] = struct{}{}
                }
            }
        }
        cnt := len(contribSet)
        if cnt == 0 { continue }
        ways := (powmod(2, cnt, mod) - 1 + mod) % mod
        // Inclusion-Exclusion: add if bits odd, subtract if even
        if bits%2 == 1 {
            res = (res + ways) % mod
        } else {
            res = (res - ways + mod) % mod
        }
    }
    return res
}

func powmod(a, b, mod int) int {
    res := 1
    for b > 0 {
        if b&1 == 1 {
            res = res * a % mod
        }
        a = a * a % mod
        b >>= 1
    }
    return res
}
# @lc code=end