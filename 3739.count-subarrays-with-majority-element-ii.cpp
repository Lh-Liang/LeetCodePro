#
# @lc app=leetcode id=3739 lang=cpp
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution {
public:
    // Fenwick Tree (Binary Indexed Tree) implementation
    vector<int> bit;
    int n_size;

    void update(int idx, int val) {
        for (; idx < n_size; idx += idx & -idx)
            bit[idx] += val;
    }

    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx)
            sum += bit[idx];
        return sum;
    }

    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        // The range of prefix sums is [-n, n].
        // We map this to [1, 2*n + 1] for 1-based indexing in BIT.
        // Offset = n + 1.
        // Value x maps to x + n + 1.
        n_size = 2 * n + 2;
        bit.assign(n_size + 1, 0);

        long long count = 0;
        int current_sum = 0;
        int offset = n + 1;

        // Add the initial prefix sum 0 (which conceptually is at index -1)
        update(0 + offset, 1);

        for (int x : nums) {
            if (x == target) {
                current_sum += 1;
            } else {
                current_sum -= 1;
            }
            
            // We want to find number of previous prefix sums P_prev such that P_prev < current_sum.
            // Mapped index is current_sum + offset.
            // We query for counts at indices strictly less than current_sum + offset.
            count += query(current_sum + offset - 1);
            
            // Add current prefix sum to the BIT
            update(current_sum + offset, 1);
        }

        return count;
    }
};
# @lc code=end