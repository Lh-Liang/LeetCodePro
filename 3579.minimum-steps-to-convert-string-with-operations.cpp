#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.length();
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;

        auto get_cost = [&](string s1, string s2) {
            auto solve = [&](string a, string b) {
                if (a == b) return 0;
                map<char, int> countA, countB;
                for (char c : a) countA[c]++;
                for (char c : b) countB[c]++;
                
                int replacements = 0;
                for (char c = 'a'; c <= 'z'; ++c) {
                    if (countB[c] > countA[c]) {
                        replacements += countB[c] - countA[c];
                    }
                }
                
                bool needs_swap = false;
                if (replacements < a.length()) {
                    // If after replacements, the string isn't already equal to target
                    // we check if the remaining characters are in the right place.
                    // However, the rule says we can swap any two characters in the substring once.
                    // This effectively means one swap operation allows any permutation.
                    if (a != b) {
                        // Check if characters match after hypothetical replacements
                        // Actually, if multiset doesn't match, we replace. 
                        // If multiset matches but string doesn't, 1 swap.
                        // If multiset doesn't match, we replace then potentially 1 swap.
                        needs_swap = false;
                        map<char, int> tempA = countA;
                        int r = replacements;
                        // This is a simplification: if any char differs, and we have chars to swap
                        needs_swap = true;
                    }
                }
                
                // Re-evaluating logic based on "each character used at most once"
                // If multisets match: 0 if a==b, else 1 swap.
                // If multisets don't match: 'replacements' replaces, then if still not equal, 1 swap.
                // But can we replace and swap the same index? Yes.
                
                // Let's refine: 
                // 1. If a == b, cost = 0
                // 2. Calculate replacements R to make multisets match.
                // 3. If R > 0, we perform R replaces. After R replaces, can we make it match B?
                //    Yes, we can choose which indices to replace and what to replace them with.
                //    To minimize swaps, we replace indices where a[i] != b[i].
                // 4. After R replaces, if the string still != b, we need 1 swap.
                
                map<char, int> ca = countA, cb = countB;
                int R = 0;
                for(auto const& [ch, freq] : cb) R += max(0, freq - ca[ch]);
                
                if (R == 0) return (a == b) ? 0 : 1;
                
                // Greedily keep characters that are already in the correct position
                int matches = 0;
                map<char, int> available = ca;
                for(int i=0; i<a.length(); ++i) {
                    if (a[i] == b[i]) {
                        matches++;
                        available[a[i]]--;
                    }
                }
                
                // Remaining positions to fill: n - matches. 
                // We have 'available' chars. We need 'cb' chars (excluding matches).
                // The number of characters we can keep (not replace) is (n - R).
                // If these (n-R) characters can be placed in their correct positions 
                // without a swap, cost is R. Otherwise R + 1.
                if (R == a.length()) return R;
                
                int can_keep_in_place = 0;
                map<char, int> temp_cb = cb;
                for(int i=0; i<a.length(); ++i) {
                    if (a[i] == b[i]) {
                        can_keep_in_place++;
                        temp_cb[b[i]]--;
                    }
                }
                // Total characters to keep is n-R. If we can't keep all in place, we swap.
                return (can_keep_in_place == (int)a.length() - R) ? R : R + 1;
            };

            int cost1 = solve(s1, s2);
            string rs1 = s1;
            reverse(rs1.begin(), rs1.end());
            int cost2 = 1 + solve(rs1, s2);
            return min(cost1, cost2);
        };

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                dp[i] = min(dp[i], dp[j] + get_cost(word1.substr(j, i - j), word2.substr(j, i - j)));
            }
        }

        return dp[n];
    }
};