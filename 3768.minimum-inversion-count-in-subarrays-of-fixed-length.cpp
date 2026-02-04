# @lc app=leetcode id=3768 lang=cpp
# [3768] Minimum Inversion Count in Subarrays of Fixed Length

#include <vector>
#include <algorithm>
using namespace std;

class FenwickTree {
public:
    vector<int> tree;
    int size;

    FenwickTree(int n) : size(n) {
        tree.resize(n + 1, 0);
    }

    void update(int index, int delta) {
        for (; index <= size; index += index & -index) {
            tree[index] += delta;
        }
    }

    int query(int index) const {
        int sum = 0;
        for (; index > 0; index -= index & -index) {
            sum += tree[index];
        }
        return sum;
    }
};

class Solution {
public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        long long min_inversions = LLONG_MAX;

        // Coordinate compression to fit within Fenwick Tree range
        vector<int> sorted_nums(nums.begin(), nums.end());
        sort(sorted_nums.begin(), sorted_nums.end());
        for (int& num : nums) {
            num = lower_bound(sorted_nums.begin(), sorted_nums.end(), num) - sorted_nums.begin() + 1;
        }

        // Use Fenwick Tree for inversion counting within window size k
        FenwickTree fenwick_tree(n);

        // Initial calculation for first window
        long long current_inversions = 0;
        for (int i = 0; i < k; ++i) {
            current_inversions += i - fenwick_tree.query(nums[i]);
            fenwick_tree.update(nums[i], 1);
        }
        min_inversions = min(min_inversions, current_inversions);

        // Slide window across entire array and update inversions accordingly
        for (int i = k; i < n; ++i) {
            // Remove influence of element going out of window from fenwick tree & inversions count
            fenwick_tree.update(nums[i - k], -1);
            current_inversions -= fenwick_tree.query(nums[i - k] - 1);

            // Add influence of new element into window
            current_inversions += (k - 1) - fenwick_tree.query(nums[i]);
            fenwick_tree.update(nums[i], 1);

            min_inversions = min(min_inversions, current_inversions);
        }

         return min_inversions;
     }
};