#
# @lc app=leetcode id=3519 lang=cpp
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution {
public:
    static constexpr int MOD = 1000000007;
    // Convert decimal string to vector of base-b digits (most to least significant)
    vector<int> to_base_b(const string& s, int b) {
        vector<int> res;
        string n = s;
        while (n != "0") {
            int rem = 0;
            string next;
            for (char c : n) {
                int cur = rem * 10 + (c - '0');
                next += (cur / b) + '0';
                rem = cur % b;
            }
            res.push_back(rem);
            // remove leading zeros
            int i = 0;
            while (i < next.size() && next[i] == '0') ++i;
            n = (i == next.size() ? "0" : next.substr(i));
        }
        if (res.empty()) res.push_back(0);
        reverse(res.begin(), res.end());
        return res;
    }

    // Decrement decimal string by 1
    string dec_string_minus_one(string s) {
        int n = s.size(), i = n - 1;
        while (i >= 0 && s[i] == '0') s[i--] = '9';
        if (i >= 0) s[i]--;
        if (s[0] == '0' && s.size() > 1) s = s.substr(1);
        return s == "" ? "0" : s;
    }

    int count_dp(const vector<int>& digits, int b) {
        int n = digits.size();
        vector<vector<vector<int>>> memo(n+1, vector<vector<int>>(b+1, vector<int>(2, -1)));
        function<int(int, int, bool, bool)> dfs = [&](int pos, int prev, bool tight, bool lead_zero) -> int {
            if (pos == n) return lead_zero ? 0 : 1;
            int &res = memo[pos][prev][tight ? 1 : 0];
            if (!lead_zero && res != -1) return res;
            int limit = tight ? digits[pos] : b-1;
            int ans = 0;
            for (int d = 0; d <= limit; ++d) {
                if (!lead_zero && d < prev) continue;
                bool next_lead_zero = lead_zero && d == 0;
                int next_prev = next_lead_zero ? 0 : d;
                bool next_tight = tight && (d == limit);
                ans = (ans + dfs(pos+1, next_prev, next_tight, next_lead_zero)) % MOD;
            }
            if (!lead_zero) res = ans;
            return ans;
        };
        return dfs(0, 0, true, true);
    }

    int countNumbers(string l, string r, int b) {
        vector<int> dr = to_base_b(r, b);
        int cnt_r = count_dp(dr, b);
        string l1 = dec_string_minus_one(l);
        int cnt_l = (l1 == "0") ? 0 : count_dp(to_base_b(l1, b), b);
        int ans = (cnt_r - cnt_l + MOD) % MOD;
        return ans;
    }
};
# @lc code=end