#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = (int)str1.size();
        int m = (int)str2.size();
        int L = n + m - 1;

        // Step 1: apply forced letters from 'T' windows
        vector<char> fixed(L, '?');
        for (int i = 0; i < n; ++i) {
            if (str1[i] != 'T') continue;
            for (int j = 0; j < m; ++j) {
                int p = i + j;
                char need = str2[j];
                if (fixed[p] == '?' || fixed[p] == need) fixed[p] = need;
                else return "";
            }
        }

        // Step 2: KMP prefix function
        vector<int> pi(m, 0);
        for (int i = 1; i < m; ++i) {
            int j = pi[i - 1];
            while (j > 0 && str2[i] != str2[j]) j = pi[j - 1];
            if (str2[i] == str2[j]) ++j;
            pi[i] = j;
        }

        // Step 3: Precompute transitions for states 0..m-1 and chars a..z.
        vector<array<int, 26>> go(m);
        vector<array<unsigned char, 26>> isMatch(m);
        for (int st = 0; st < m; ++st) {
            for (int c = 0; c < 26; ++c) {
                char ch = char('a' + c);
                int k = st;
                while (k > 0 && str2[k] != ch) k = pi[k - 1];
                if (str2[k] == ch) ++k;

                bool matched = false;
                if (k == m) {
                    matched = true;
                    k = pi[m - 1];
                }
                go[st][c] = k;
                isMatch[st][c] = (unsigned char)matched;
            }
        }

        auto idx = [m](int pos, int st) { return pos * m + st; };

        // dp[pos][st]: can we finish from pos with current KMP state st?
        vector<unsigned char> dp((L + 1) * m, 0);
        for (int st = 0; st < m; ++st) dp[idx(L, st)] = 1;

        for (int pos = L - 1; pos >= 0; --pos) {
            int need = -1;
            if (pos >= m - 1) {
                need = (str1[pos - (m - 1)] == 'T') ? 1 : 0;
            }

            if (fixed[pos] != '?') {
                int c = fixed[pos] - 'a';
                for (int st = 0; st < m; ++st) {
                    if (need != -1 && (int)isMatch[st][c] != need) continue;
                    int nst = go[st][c];
                    if (dp[idx(pos + 1, nst)]) dp[idx(pos, st)] = 1;
                }
            } else {
                for (int st = 0; st < m; ++st) {
                    unsigned char ok = 0;
                    for (int c = 0; c < 26; ++c) {
                        if (need != -1 && (int)isMatch[st][c] != need) continue;
                        int nst = go[st][c];
                        if (dp[idx(pos + 1, nst)]) {
                            ok = 1;
                            break;
                        }
                    }
                    dp[idx(pos, st)] = ok;
                }
            }
        }

        if (!dp[idx(0, 0)]) return "";

        // Reconstruct lexicographically smallest answer
        string ans;
        ans.reserve(L);
        int st = 0;
        for (int pos = 0; pos < L; ++pos) {
            int need = -1;
            if (pos >= m - 1) {
                need = (str1[pos - (m - 1)] == 'T') ? 1 : 0;
            }

            bool chosen = false;
            if (fixed[pos] != '?') {
                int c = fixed[pos] - 'a';
                if (need == -1 || (int)isMatch[st][c] == need) {
                    int nst = go[st][c];
                    if (dp[idx(pos + 1, nst)]) {
                        ans.push_back(fixed[pos]);
                        st = nst;
                        chosen = true;
                    }
                }
            } else {
                for (int c = 0; c < 26; ++c) {
                    if (need != -1 && (int)isMatch[st][c] != need) continue;
                    int nst = go[st][c];
                    if (dp[idx(pos + 1, nst)]) {
                        ans.push_back(char('a' + c));
                        st = nst;
                        chosen = true;
                        break;
                    }
                }
            }

            if (!chosen) return ""; // should not happen if dp[0][0] is true
        }

        return ans;
    }
};
// @lc code=end
