#
# @lc app=leetcode id=3630 lang=cpp
#
# [3630] Partition Array for Maximum XOR and AND
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <tuple>
using namespace std;

class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        using State = tuple<int, long long, long long, long long, bool>;
        unordered_map<State, long long> memo;
        
        function<long long(int, long long, long long, long long, bool)> dfs = [&](int idx, long long xorA, long long andB, long long xorC, bool bUsed) -> long long {
            if (idx == n) {
                // if B is empty, AND(B) = 0
                return xorA + (bUsed ? andB : 0) + xorC;
            }
            State key = {idx, xorA, andB, xorC, bUsed};
            if (memo.count(key)) return memo[key];
            long long res = 0;
            // Option 1: put in A
            res = max(res, dfs(idx+1, xorA ^ nums[idx], andB, xorC, bUsed));
            // Option 2: put in B
            if (bUsed) {
                res = max(res, dfs(idx+1, xorA, andB & nums[idx], xorC, true));
            } else {
                res = max(res, dfs(idx+1, xorA, nums[idx], xorC, true));
            }
            // Option 3: put in C
            res = max(res, dfs(idx+1, xorA, andB, xorC ^ nums[idx], bUsed));
            memo[key] = res;
            return res;
        };
        return dfs(0, 0, 0, 0, false);
    }
};
# @lc code=end