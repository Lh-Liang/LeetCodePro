#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> permute(int n, long long k) {
        vector<int> nums(n);
        for (int i = 0; i < n; ++i) nums[i] = i + 1;
        vector<int> result;
        long long factorial[101] = {1};
        for (int i = 1; i <= n; ++i) factorial[i] = factorial[i - 1] * i;
        
        // Calculate total valid alternating permutations count here before proceeding.
        long long total_permutations = calculateTotalAlternatingPermutations(n);
        if (k > total_permutations) return {};
        
        --k; // Zero-based index for convenience in calculations
        for (int pos = 0; pos < n && k >= 0; ++pos) {
            for (int i = pos; i < n; ++i) {
                // Ensure alternation between current and previous position
                if (pos > 0 && ((nums[i] % 2) == (nums[pos - 1] % 2))) continue;
                swap(nums[pos], nums[i]);
                long long count = factorial[n - pos - 1];
                if (count <= k) {
                    k -= count;
                    swap(nums[pos], nums[i]); // Backtrack swap if not using this prefix
                } else {
                    result.push_back(nums[pos]);
                    break;
                }
            }
        }
        return result.size() == n ? result : vector<int>{};
    }
    
    long long calculateTotalAlternatingPermutations(int n) {
        // Implement combinatorial logic to calculate total number of valid alternating permutations for n elements.
        // This part is crucial to determine early exit conditions based on k.
    }
};
# @lc code=end