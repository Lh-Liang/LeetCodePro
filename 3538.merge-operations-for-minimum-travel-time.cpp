#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        unordered_map<string, int> memo;
        return dp(position, time, k, memo);
    }

private:
    // Serialize the times array for memoization
    string serialize(const vector<int>& time) {
        string res;
        for (int t : time) {
            res += to_string(t) +