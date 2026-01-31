#
# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    vector<int> bit;
    int bit_size;

    void update(int idx, int val) {
        for (; idx <= bit_size; idx += idx & -idx)
            bit[idx] += val;
    }

    int query(int idx) {
        int res = 0;
        for (; idx > 0; idx -= idx & -idx)
            res += bit[idx];
        return res;
    }

public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        if (k <= 1) return 0;

        // Coordinate compression
        vector<int> coords = nums;
        sort(coords.begin(), coords.end());
        coords.erase(unique(coords.begin(), coords.end()), coords.end());
        
        auto get_rank = [&](int x) {
            return lower_bound(coords.begin(), coords.end(), x) - coords.begin() + 1;
        };

        vector<int> ranks(n);
        for (int i = 0; i < n; ++i) ranks[i] = get_rank(nums[i]);

        bit_size = coords.size();
        bit.assign(bit_size + 1, 0);

        long long current_inv = 0;
        for (int i = 0; i < k; ++i) {
            // Elements > current rank are (elements_processed - elements_<=_current_rank)
            current_inv += (i - query(ranks[i]));
            update(ranks[i], 1);
        }

        long long min_inv = current_inv;

        for (int i = 0; i < n - k; ++i) {
            // Remove nums[i]: it was the first element, so it was greater than query(ranks[i]-1) elements
            current_inv -= query(ranks[i] - 1);
            update(ranks[i], -1);
            
            // Add nums[i+k]: it is the last element, so it is smaller than ((k-1) - query(ranks[i+k])) elements
            current_inv += ((k - 1) - query(ranks[i + k]));
            update(ranks[i + k], 1);
            
            if (current_inv < min_inv) min_inv = current_inv;
        }

        return min_inv;
    }
};
# @lc code=end