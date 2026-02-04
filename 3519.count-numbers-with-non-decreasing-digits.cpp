#
# @lc app=leetcode id=3519 lang=cpp
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
#include <vector>
#include <string>
#include <cstring>
using namespace std;

class Solution {
    static constexpr int MOD = 1e9 + 7;
public:
    int countNumbers(string l, string r, int b) {
        vector<int> r_digits = to_base_b(r, b);
        vector<int> l_digits = to_base_b(subtract_one(l), b);
        memset(dp, -1, sizeof(dp));
        int cnt_r = dfs(0, 0, 1, 1, r_digits, b);
        memset(dp, -1, sizeof(dp));
        int cnt_l = dfs(0, 0, 1, 1, l_digits, b);
        int ans = (cnt_r - cnt_l + MOD) % MOD;
        return ans;
    }

private:
    int dp[105][11][2][2];
    // pos, prev_digit, tight, leading_zero
    int dfs(int pos, int prev, int tight, int leading_zero, const vector<int>& digits, int b) {
        if (pos == digits.size()) return leading_zero ? 0 : 1;
        int &res = dp[pos][prev][tight][leading_zero];
        if (res != -1) return res;
        res = 0;
        int limit = tight ? digits[pos] : b - 1;
        for (int d = 0; d <= limit; ++d) {
            if (!leading_zero && d < prev) continue;
            int next_leading_zero = leading_zero && d == 0;
            int next_tight = tight && (d == limit);
            int next_prev = next_leading_zero ? 0 : d;
            res = (res + dfs(pos + 1, next_prev, next_tight, next_leading_zero, digits, b)) % MOD;
        }
        return res;
    }
    // Converts decimal string to base-b vector (MSD first)
    vector<int> to_base_b(string s, int b) {
        vector<int> v;
        vector<int> num;
        for(char ch : s) num.push_back(ch - '0');
        while(!num.empty()) {
            int rem = 0;
            vector<int> next;
            for(int d : num) {
                int cur = rem * 10 + d;
                next.push_back(cur / b);
                rem = cur % b;
            }
            v.push_back(rem);
            // Remove leading zeros
            int idx = 0;
            while(idx < next.size() && next[idx] == 0) ++idx;
            num.assign(next.begin() + idx, next.end());
        }
        while(v.size() < s.size()) v.push_back(0);
        reverse(v.begin(), v.end());
        return v;
    }
    // Subtract one from decimal string, handles big numbers
    string subtract_one(const string& s) {
        string res = s;
        int n = res.size();
        int i = n - 1;
        while(i >= 0) {
            if(res[i] > '0') {
                res[i]--;
                break;
            } else {
                res[i] = '9';
                i--;
            }
        }
        // Remove leading zeros
        i = 0;
        while(i < res.size()-1 && res[i] == '0') i++;
        return res.substr(i);
    }
};
# @lc code=end