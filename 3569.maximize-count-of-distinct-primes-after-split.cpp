#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        const int MAX_N = 100005;
        vector<bool> is_prime(MAX_N, true);
        is_prime[0] = is_prime[1] = false;
        for(int i = 2; i * i < MAX_N; ++i) {
            if(is_prime[i])
                for(int j = i * i; j < MAX_N; j += i)
                    is_prime[j] = false;
        }
        int n = nums.size();
        vector<int> res;
        vector<int> arr = nums;
        for(auto& q : queries) {
            arr[q[0]] = q[1];
            // Count distinct primes in prefix and suffix for each k
            unordered_set<int> left, right;
            vector<int> prefix(n), suffix(n);
            for(int i=0; i<n; ++i) {
                if(is_prime[arr[i]]) left.insert(arr[i]);
                prefix[i] = left.size();
            }
            right.clear();
            for(int i=n-1; i>=0; --i) {
                if(is_prime[arr[i]]) right.insert(arr[i]);
                suffix[i] = right.size();
            }
            int mx = 0;
            for(int k=1; k<n; ++k) {
                int left_cnt = prefix[k-1];
                int right_cnt = suffix[k];
                mx = max(mx, left_cnt + right_cnt);
            }
            res.push_back(mx);
        }
        return res;
    }
};
# @lc code=end