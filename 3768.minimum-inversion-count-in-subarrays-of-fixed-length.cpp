#
# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#
# @lc code=start
class Solution {
public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        unordered_map<int, int> rank_map;
        for (int i = 0; i < n; ++i) {
            rank_map[sorted_nums[i]] = i + 1; // Rank starts from 1
        }
        
        vector<int> bit(n + 1, 0);
        auto update = [&](int index, int value) {
            while (index <= n) {
                bit[index] += value;
                index += index & -index;
            }
        };
        
        auto query = [&](int index) {
            int sum = 0;
            while (index > 0) {
                sum += bit[index];
                index -= index & -index;
            }
            return sum;
        };

        long long current_inversions = 0;

        // Initial window setup
        for (int i = 0; i < k; ++i) {
            int rank = rank_map[nums[i]];
            current_inversions += query(n) - query(rank);
            update(rank, 1);
        }

        long long min_inversions = current_inversions;

        // Sliding window
        for (int i = k; i < n; ++i) {
            int rank_outgoing = rank_map[nums[i-k]];
            update(rank_outgoing, -1);
            current_inversions -= query(n) - query(rank_outgoing);

            int rank_incoming = rank_map[nums[i]];
            current_inversions += query(n) - query(rank_incoming);
            update(rank_incoming, 1);

            min_inversions = min(min_inversions, current_inversions);
        }

        return min_inversions;
    }
};
# @lc code=end