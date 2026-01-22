//
// @lc app=leetcode id=3519 lang=cpp
//
// [3519] Count Numbers with Non-Decreasing Digits
//
// @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    
    string subtract1(string s) {
        int i = s.length() - 1;
        while (i >= 0 && s[i] == '0') {
            s[i] = '9';
            i--;
        }
        if (i < 0) return "0";
        s[i]--;
        int start = 0;
        while (start < (int)s.length() - 1 && s[start] == '0') start++;
        return s.substr(start);
    }
    
    vector<int> toBase(string s, int b) {
        vector<int> result;
        while (s != "0") {
            string quotient;
            int remainder = 0;
            for (char c : s) {
                int digit = c - '0';
                int value = remainder * 10 + digit;
                quotient += char((value / b) + '0');
                remainder = value % b;
            }
            int start = 0;
            while (start < (int)quotient.length() - 1 && quotient[start] == '0') start++;
            quotient = quotient.substr(start);
            
            result.push_back(remainder);
            s = quotient;
        }
        if (result.empty()) result.push_back(0);
        reverse(result.begin(), result.end());
        return result;
    }
    
    int countNumbers(string l, string r, int b) {
        auto countUpTo = [&](vector<int>& digits) -> long long {
            int n = digits.size();
            map<tuple<int,int,int,int>, long long> memo;
            
            function<long long(int, int, bool, bool)> dp = [&](int pos, int last, bool tight, bool started) -> long long {
                if (pos == n) return 1;
                
                auto key = make_tuple(pos, started ? last : -1, tight ? 1 : 0, started ? 1 : 0);
                if (memo.count(key)) return memo[key];
                
                int upperBound = tight ? digits[pos] : b - 1;
                long long res = 0;
                
                for (int d = 0; d <= upperBound; d++) {
                    if (!started && d == 0) {
                        res = (res + dp(pos + 1, 0, tight && (d == digits[pos]), false)) % MOD;
                    } else if (!started) {
                        res = (res + dp(pos + 1, d, tight && (d == digits[pos]), true)) % MOD;
                    } else if (d >= last) {
                        res = (res + dp(pos + 1, d, tight && (d == digits[pos]), true)) % MOD;
                    }
                }
                
                memo[key] = res;
                return res;
            };
            
            return dp(0, 0, true, false);
        };
        
        vector<int> rBase = toBase(r, b);
        string lMinus1 = subtract1(l);
        vector<int> lBase = toBase(lMinus1, b);
        
        long long countR = countUpTo(rBase);
        long long countL = countUpTo(lBase);
        
        return (int)((countR - countL + MOD) % MOD);
    }
};
// @lc code=end