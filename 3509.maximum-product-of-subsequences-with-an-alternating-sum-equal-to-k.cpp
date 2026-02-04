class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int max_product = -1;
        // Backtracking function to explore subsequences
        function<void(int, int64_t, int64_t, bool)> dfs = [&](int i, int64_t prod, int64_t alt_sum, bool isEven) {
            // Prune branches where product exceeds limit
            if (prod > limit) return;
            // Base case: check conditions at end of array
            if (i == nums.size()) {
                if (alt_sum == k && prod <= limit)
                    max_product = max(max_product, static_cast<int>(prod));
                return;
            }
            // Include current number in subsequence
            dfs(i + 1, prod * nums[i], alt_sum + (isEven ? nums[i] : -nums[i]), !isEven);
            // Exclude current number from subsequence
            dfs(i + 1, prod, alt_sum, isEven);
        };
        // Start backtracking from index 0 with initial values
        dfs(0, 1LL, 0LL, true);
        return max_product;
    }
};