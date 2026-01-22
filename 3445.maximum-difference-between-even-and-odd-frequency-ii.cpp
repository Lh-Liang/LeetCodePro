#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        int result = INT_MIN;
        
        // Try all pairs (a, b) where a has odd freq and b has non-zero even freq
        for (char a = '0'; a <= '4'; a++) {
            for (char b = '0'; b <= '4'; b++) {
                if (a == b) continue;
                
                // Compute prefix sums
                vector<int> pref_a(n + 1, 0), pref_b(n + 1, 0);
                for (int i = 0; i < n; i++) {
                    pref_a[i + 1] = pref_a[i] + (s[i] == a ? 1 : 0);
                    pref_b[i + 1] = pref_b[i] + (s[i] == b ? 1 : 0);
                }
                
                // lists[pa][pb] stores (prefix_b_val, min_diff_up_to_here)
                vector<vector<vector<pair<int, int>>>> lists(2, vector<vector<pair<int, int>>>(2));
                
                for (int i = k; i <= n; i++) {
                    // Release j = i - k
                    int j = i - k;
                    int dj = pref_a[j] - pref_b[j];
                    int pa_j = pref_a[j] % 2;
                    int pb_j = pref_b[j] % 2;
                    int v_j = pref_b[j];
                    
                    auto& lst = lists[pa_j][pb_j];
                    if (lst.empty()) {
                        lst.push_back({v_j, dj});
                    } else if (v_j > lst.back().first) {
                        lst.push_back({v_j, min(lst.back().second, dj)});
                    } else {
                        lst.back().second = min(lst.back().second, dj);
                    }
                    
                    // Query at i
                    int di = pref_a[i] - pref_b[i];
                    int pa_i = pref_a[i] % 2;
                    int pb_i = pref_b[i] % 2;
                    int target_pa = 1 - pa_i;
                    int target_pb = pb_i;
                    int threshold = pref_b[i] - 2;
                    
                    if (threshold >= 0) {
                        auto& target_lst = lists[target_pa][target_pb];
                        if (!target_lst.empty()) {
                            // Find the largest index where first <= threshold
                            auto it = upper_bound(target_lst.begin(), target_lst.end(), threshold,
                                                  [](int val, const pair<int, int>& p) { return val < p.first; });
                            if (it != target_lst.begin()) {
                                --it;
                                int min_j_diff = it->second;
                                result = max(result, di - min_j_diff);
                            }
                        }
                    }
                }
            }
        }
        
        return result;
    }
};
# @lc code=end