#
# @lc app=leetcode id=3785 lang=cpp
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        // Step 1: Feasibility Check
        // We need to ensure that for every value 'v' present in nums,
        // there are enough valid positions in the array (indices i where forbidden[i] != v).
        // If count(v in nums) + count(v in forbidden) > n, it's impossible.
        
        int n = nums.size();
        map<int, int> num_counts;
        map<int, int> forbid_counts;
        
        for (int x : nums) num_counts[x]++;
        for (int x : forbidden) forbid_counts[x]++;
        
        for (auto const& [val, count] : num_counts) {
            // Use long long to prevent overflow, though n <= 10^5 fits in int.
            if ((long long)count + forbid_counts[val] > n) {
                return -1;
            }
        }
        
        // Step 2: Identify Conflicts
        // A conflict exists at index i if nums[i] == forbidden[i].
        // We group conflicts by the value involved.
        
        map<int, int> conflict_counts;
        int total_conflicts = 0;
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                conflict_counts[nums[i]]++;
                total_conflicts++;
            }
        }
        
        // Step 3: Calculate Minimum Swaps
        // Strategy:
        // 1. Swapping two conflicts with DIFFERENT values (e.g., val A and val B) resolves both conflicts in 1 swap.
        //    (Index i has A, forbids A; Index j has B, forbids B. Swap -> i has B, j has A. valid since A!=B).
        // 2. Swapping a conflict with a non-conflict index resolves 1 conflict in 1 swap.
        
        // We want to maximize strategy 1. This is a matching problem.
        // If we have a "dominant" conflict group (size > sum of all others), we can't match all of them.
        // Otherwise, we can match almost all (maybe 1 left over).
        
        int max_conflict = 0;
        for (auto const& [val, count] : conflict_counts) {
            max_conflict = max(max_conflict, count);
        }
        
        int others = total_conflicts - max_conflict;
        
        if (max_conflict > others) {
            // Dominant case:
            // We can pair all 'others' with 'max_conflict' group. Cost = others.
            // Remaining 'max_conflict - others' items must be swapped with non-conflict indices. Cost = remaining.
            // Total = others + (max_conflict - others) = max_conflict.
            return max_conflict;
        } else {
            // Non-dominant case:
            // We can pair up conflicts nearly perfectly.
            // Each swap resolves 2 conflicts.
            // If odd total, 1 swap resolves the last one.
            // Formula: ceil(total / 2)
            return (total_conflicts + 1) / 2;
        }
    }
};
# @lc code=end