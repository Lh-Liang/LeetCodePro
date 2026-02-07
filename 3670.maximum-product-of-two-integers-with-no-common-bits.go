#
# @lc app=leetcode id=3670 lang=golang
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
func maxProduct(nums []int) int64 {
    type pair struct{first, second int}
    maskMax := make(map[int]pair) // mask -> top 2 values
    for _, num := range nums {
        mask := num
        if curr, ok := maskMax[mask]; ok {
            if num > curr.first {
                maskMax[mask] = pair{num, curr.first}
            } else if num > curr.second {
                maskMax[mask] = pair{curr.first, num}
            }
        } else {
            maskMax[mask] = pair{num, 0}
        }
    }
    masks := make([]int, 0, len(maskMax))
    for m := range maskMax {
        masks = append(masks, m)
    }
    maxProd := int64(0)
    // Compare different masks
    for i := 0; i < len(masks); i++ {
        for j := i + 1; j < len(masks); j++ {
            if masks[i]&masks[j] == 0 {
                a, b := maskMax[masks[i]].first, maskMax[masks[j]].first
                prod := int64(a) * int64(b)
                if prod > maxProd {
                    maxProd = prod
                }
            }
        }
    }
    // For same mask, check if there are at least two numbers
    for _, p := range maskMax {
        if p.second > 0 {
            prod := int64(p.first) * int64(p.second)
            if prod > maxProd {
                maxProd = prod
            }
        }
    }
    return maxProd
}
# @lc code=end