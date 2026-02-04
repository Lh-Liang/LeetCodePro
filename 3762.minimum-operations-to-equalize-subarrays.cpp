#
# @lc app=leetcode id=3762 lang=cpp
#
# [3762] Minimum Operations to Equalize Subarrays
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<long long> answers;
        for (auto& query : queries) {
            int li = query[0];
            int ri = query[1];
            vector<int> subarray(nums.begin() + li, nums.begin() + ri + 1);
            sort(subarray.begin(), subarray.end());
            // Check if all differences are divisible by k
            bool possible = true;
            int base = subarray[0];
            for (int num : subarray) {
                if ((num - base) % k != 0) {
                    possible = false;
                    break;
                }
            }
            if (!possible) {
                answers.push_back(-1);
                continue;
            }
            // Use median as a potential optimal target
            int median = subarray[subarray.size() / 2];
            long long totalOps = 0;
            for (int num : subarray) {
                totalOps += abs(num - median) / k;
            }
            answers.push_back(totalOps);
        }
        return answers;
    }
};
# @lc code=end