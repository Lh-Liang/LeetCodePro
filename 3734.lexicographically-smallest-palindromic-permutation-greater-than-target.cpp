# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        unordered_map<char, int> char_count;
        for (char c : s) {
            char_count[c]++;
        }
        
        int odd_count = 0;
        for (auto &pair : char_count) {
            if (pair.second % 2 != 0) odd_count++;
        }

        if (odd_count > 1 || (odd_count == 1 && s.size() % 2 == 0)) {
            return ""; // No palindromic permutation possible
        }

        string half = "", middle = "";
        for (auto &pair : char_count) {
            if (pair.second % 2 != 0) {
                middle += pair.first; // Middle character for odd-length palindrome
            }
            half += string(pair.second / 2, pair.first);
        }

        sort(half.begin(), half.end());
        
        string best_palindrome = "";
        do {
            string candidate = half + middle + string(half.rbegin(), half.rend());
            if (candidate > target && (best_palindrome.empty() || candidate < best_palindrome)) {
                best_palindrome = candidate;
            }
        } while (next_permutation(half.begin(), half.end()));

        return best_palindrome;
    }
};
# @lc code=end