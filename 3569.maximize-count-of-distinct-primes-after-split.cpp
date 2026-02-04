//
// @lc app=leetcode id=3569 lang=cpp
//
// [3569] Maximize Count of Distinct Primes After Split
//
// @lc code=start
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        const int MAXV = 100005;
        vector<bool> is_prime(MAXV, true);
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i < MAXV; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j < MAXV; j += i)
                    is_prime[j] = false;
            }
        }
        int n = nums.size();
        vector<int> res;
        for (auto& q : queries) {
            int idx = q[0], val = q[1];
            nums[idx] = val;
            unordered_set<int> prefix_set, suffix_set;
            vector<int> prefix_count(n, 0), suffix_count(n, 0);
            for (int i = 0; i < n; ++i) {
                if (is_prime[nums[i]]) prefix_set.insert(nums[i]);
                prefix_count[i] = prefix_set.size();
            }
            for (int i = n - 1; i >= 0; --i) {
                if (is_prime[nums[i]]) suffix_set.insert(nums[i]);
                suffix_count[i] = suffix_set.size();
            }
            int max_sum = 0;
            for (int k = 1; k < n; ++k) {
                int left = prefix_count[k - 1];
                int right = suffix_count[k];
                max_sum = max(max_sum, left + right);
            }
            res.push_back(max_sum);
        }
        return res;
    }
};
// @lc code=end