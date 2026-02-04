class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();
        int left = 0;
        int count0 = 0, count1 = 0;
        int max_window_size = 0;
        for (int right = 0; right < n; ++right) {
            if (s[right] == '0') count0++;
            else count1++;
            // Check if we need to shrink the window
            while (min(count0, count1) > numOps) {
                if (s[left] == '0') count0--;
                else count1--;
                left++;
            }
            // Calculate maximum size of valid window
            max_window_size = max(max_window_size, right - left + 1);
        }
        return n - max_window_size;
    }
};