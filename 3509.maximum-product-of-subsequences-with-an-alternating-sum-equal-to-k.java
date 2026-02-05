# @lc code=start
class Solution {
    public int maxProduct(int[] nums, int k, int limit) {
        int[] maxProduct = {-1};
        findMaxProduct(nums, k, limit, 0, 0, 1, maxProduct);
        return maxProduct[0];
    }

    private void findMaxProduct(int[] nums, int targetSum, int limit, int index, int currentSum, int currentProduct, int[] maxProduct) {
        if (index == nums.length) {
            if (currentSum == targetSum && currentProduct <= limit) {
                maxProduct[0] = Math.max(maxProduct[0], currentProduct);
            }
            return;
        }

        // Include current element with proper sign based on position
        findMaxProduct(nums, targetSum, limit,
                       index + 1,
                       index % 2 == 0 ? currentSum + nums[index] : currentSum - nums[index],
                       currentProduct * nums[index],
                       maxProduct);

        // Exclude current element from subsequence
        findMaxProduct(nums, targetSum, limit,
                       index + 1,
                       currentSum,
                       currentProduct,
                       maxProduct);
    }
}
# @lc code=end