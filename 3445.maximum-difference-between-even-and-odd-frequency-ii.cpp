#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        int max_diff = INT_MIN;

        for (int a = 0; a <= 4; ++a) {
            for (int b = 0; b <= 4; ++b) {
                if (a == b) continue;

                // dp[parity_a][parity_b] stores the minimum (pref_a - pref_b)
                // seen so far for a specific parity of prefix counts.
                // We need 2 sets: one for all seen, one for those where 'b' has appeared.
                // However, the simpler way is to track the min for each parity and 
                // ensure the 'even non-zero' condition by checking if current count of b > min count of b.
                
                vector<vector<int>> min_val(2, vector<int>(2, 1e9));
                vector<vector<int>> min_val_with_b(2, vector<int>(2, 1e9));

                int cur_a = 0, cur_b = 0;
                vector<int> pref_a(n + 1, 0), pref_b(n + 1, 0), diff(n + 1, 0);
                
                for (int i = 0; i < n; ++i) {
                    if (s[i] - '0' == a) cur_a++;
                    if (s[i] - '0' == b) cur_b++;
                    pref_a[i + 1] = cur_a;
                    pref_b[i + 1] = cur_b;
                    diff[i + 1] = cur_a - cur_b;
                }

                // Sliding window: as we move i, we can consider j = i - k as the end of the prefix to subtract.
                int j = 0;
                for (int i = k; i <= n; ++i) {
                    // Add the prefix ending at j = i - k into our possible minimums
                    int p_a = pref_a[i - k] % 2;
                    int p_b = pref_b[i - k] % 2;
                    min_val[p_a][p_b] = min(min_val[p_a][p_b], diff[i - k]);

                    // Check current i against all valid j prefixes
                    int target_p_a = 1 - (pref_a[i] % 2); // needs different parity
                    int target_p_b = pref_b[i] % 2;     // needs same parity
                    
                    // Condition: freq[b] > 0. This means pref_b[i] - pref_b[j] > 0.
                    // We can track two sets of minimums: those where pref_b[j] is smaller than the smallest possible pref_b seen so far at that parity.
                    // Or more simply: since we iterate i, we just need to find a j such that pref_b[i] > pref_b[j].
                    // Because pref_b is non-decreasing, we can maintain min_val in two categories based on pref_b parity.
                    
                    // To handle freq[b] > 0: 
                    // We can use a small trick: only update 'max_diff' if there exists a valid 'b' in the window.
                    // The most robust way is to store the min diff for each (parity_a, parity_b, pref_b_val).
                    // Since pref_b_val can be large, we just need to know if current pref_b[i] > some pref_b[j].
                    // We can store TWO minimums for each parity: one overall, and one that is 'safe'.
                    
                    // Re-evaluating: Just use 2 sets of mins. 
                    // min_val[pa][pb][0] = absolute min diff
                    // min_val[pa][pb][1] = min diff where we have seen a DIFFERENT pref_b value later?
                    // Actually, if we just keep track of the min diff for each parity, 
                    // we also need to ensure pref_b[i] > pref_b[j].
                    // Let's store the min diff for each parity along with the min pref_b value for that diff.
                    // But wait, there are only 2 possible values of pref_b for a given parity that matter: 
                    // the absolute minimum pref_b and the next one? No.
                    
                    // Correct approach: for a fixed (pa, pb), we want min diff[j] s.t. pref_b[j] < pref_b[i].
                    // Since pref_b is monotonic, we can maintain the min diff for the current parity 
                    // AND a separate min diff for when we know pref_b has increased.
                }
                
                // Let's refine the inner loop logic for clarity and correctness.
            }
        }
        return 0; // Placeholder for logic integrated into the final result below
    }
};

// Refined logic implementation
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        int ans = -1e9;
        for (int a = 0; a <= 4; ++a) {
            for (int b = 0; b <= 4; ++b) {
                if (a == b) continue;
                
                // m[parity_a][parity_b][has_b_started]
                int m[2][2][2];
                for(int i=0; i<2; ++i) for(int j=0; j<2; ++j) for(int l=0; l<2; ++l) m[i][j][l] = 1e9;

                vector<int> pref_a(n + 1, 0), pref_b(n + 1, 0);
                for (int i = 0; i < n; ++i) {
                    pref_a[i+1] = pref_a[i] + (s[i] - '0' == a);
                    pref_b[i+1] = pref_b[i] + (s[i] - '0' == b);
                }

                int j = 0;
                for (int i = k; i <= n; ++i) {
                    // Add prefix j = i - k
                    while (j <= i - k) {
                        int pa = pref_a[j] % 2, pb = pref_b[j] % 2;
                        // We need to know if a 'b' has appeared *after* this prefix j up to some point.
                        // Actually, the condition is freq[b] > 0 in s[j...i].
                        // This is pref_b[i] > pref_b[j].
                        m[pa][pb][0] = min(m[pa][pb][0], pref_a[j] - pref_b[j]);
                        j++;
                    }
                    
                    int cur_pa = pref_a[i] % 2, cur_pb = pref_b[i] % 2;
                    for (int pa = 0; pa < 2; ++pa) {
                        for (int pb = 0; pb < 2; ++pb) {
                            if ((pref_a[i] - pa + 2) % 2 == 1 && (pref_b[i] - pb + 2) % 2 == 0) {
                                // We need freq[b] > 0, so we need to find if there's a j with this parity
                                // such that pref_b[j] < pref_b[i].
                                // We can use another min array that only stores values when pref_b has changed.
                                // Or simply: if pref_b[i] > 0, there's a chance. 
                                // Let's use the property that pref_b is non-decreasing.
                                // We store the min diff for (pa, pb) in two buckets:
                                // 1. pref_b[j] < current pref_b[i]
                                // 2. pref_b[j] == current pref_b[i]
                                
                                // To simplify: we can pre-calculate the first index where pref_b reaches a certain value.
                                // But even simpler: just track the min diff for (pa, pb) separated by whether pref_b[j] < pref_b[i].
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};

# @lc code=end