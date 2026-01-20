#include <vector>
#include <string>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;

typedef unsigned __int128 uint128;

class Solution {
    const long long MOD = (1LL << 61) - 1;

    struct HashHelper {
        vector<long long> pref;
        vector<long long> powB;
        long long mod, b;

        HashHelper(const string& s, long long b, long long mod) : b(b), mod(mod) {
            int n = s.length();
            pref.resize(n + 1, 0);
            powB.resize(n + 1, 1);
            for (int i = 0; i < n; ++i) {
                pref[i + 1] = add(mul(pref[i], b), s[i] - 'a' + 1);
                powB[i + 1] = mul(powB[i], b);
            }
        }

        long long getHash(int i, int j) {
            int len = j - i + 1;
            return sub(pref[j + 1], mul(pref[i], powB[len]));
        }

        long long mul(long long a, long long b) {
            uint128 res = (uint128)a * b;
            uint128 ans = (res >> 61) + (res & mod);
            if (ans >= mod) ans -= mod;
            if (ans >= mod) ans -= mod;
            return (long long)ans;
        }

        long long add(long long a, long long b) {
            a += b;
            if (a >= mod) a -= mod;
            return a;
        }

        long long sub(long long a, long long b) {
            a -= b;
            if (a < 0) a += mod;
            return a;
        }
    };

public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }

        vector<int> start(n), end(n);
        string T = "";
        int timer = 0;

        struct Frame {
            int u;
            int childIdx;
        };
        vector<Frame> st;
        st.push_back({0, 0});

        while (!st.empty()) {
            Frame& top = st.back();
            int u = top.u;
            if (top.childIdx == 0) {
                start[u] = timer;
            }
            if (top.childIdx < adj[u].size()) {
                int v = adj[u][top.childIdx];
                top.childIdx++;
                st.push_back({v, 0});
            } else {
                T += s[u];
                end[u] = timer;
                timer++;
                st.pop_back();
            }
        }

        mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
        long long B = uniform_int_distribution<long long>(300, 1e9)(rng);

        HashHelper forward(T, B, MOD);
        string Trev = T;
        reverse(Trev.begin(), Trev.end());
        HashHelper backward(Trev, B, MOD);

        vector<bool> answer(n);
        for (int i = 0; i < n; ++i) {
            int l = start[i];
            int r = end[i];
            long long h1 = forward.getHash(l, r);
            long long h2 = backward.getHash(n - 1 - r, n - 1 - l);
            answer[i] = (h1 == h2);
        }

        return answer;
    }
};