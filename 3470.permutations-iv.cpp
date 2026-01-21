#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#

# @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> permute(int n, long long k) {
        using ll = long long;
        const ll LMAX = 9223372036854775807LL;
        auto safe_fact = [&](int nn) -> ll {
            if (nn <= 1) return 1LL;
            ll res = 1LL;
            for (int i = 2; i <= nn; ++i) {
                if (res > LMAX / i) return LMAX;
                res *= i;
            }
            return res;
        };
        auto get_count = [&](int ao, int ae) -> ll {
            ll f1 = safe_fact(ao);
            ll f2 = safe_fact(ae);
            if (f1 > LMAX / f2) return LMAX;
            return f1 * f2;
        };
        vector<int> res(n);
        vector<bool> used(n + 1, false);
        int cur_ao = (n + 1) / 2;
        int cur_ae = n / 2;
        int pos = 0;
        ll kk = k;
        int last_p = -1;
        while (pos < n) {
            int req_p = (pos == 0 ? -1 : 1 ^ last_p);
            bool found = false;
            for (int num = 1; num <= n; ++num) {
                if (used[num]) continue;
                int p = num % 2;
                if (pos > 0 && p != req_p) continue;
                int ao_a = cur_ao - (p == 1);
                int ae_a = cur_ae - (p == 0);
                int m_a = n - pos - 1;
                int r_odd;
                if (m_a == 0) {
                    r_odd = 0;
                } else {
                    int r_p_next = 1 ^ p;
                    r_odd = (r_p_next == 1 ? (m_a + 1) / 2 : m_a / 2);
                }
                int r_even = m_a - r_odd;
                if (ao_a != r_odd || ae_a != r_even) continue;
                ll cnt = get_count(ao_a, ae_a);
                if (kk <= cnt) {
                    res[pos] = num;
                    used[num] = true;
                    cur_ao = ao_a;
                    cur_ae = ae_a;
                    last_p = p;
                    found = true;
                    break;
                } else {
                    kk -= cnt;
                }
            }
            if (!found) {
                return {};
            }
            ++pos;
        }
        return res;
    }
};
# @lc code=end
