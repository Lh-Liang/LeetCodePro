# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        long long deficit = 0;
        int negativeIndex = -1;
        
        // Find the negative balance and calculate its absolute value
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) {
                deficit = -balance[i];
                negativeIndex = i;
                break;
            }
        }

        // If no negative balance is found, return 0 as no moves are needed
        if (negativeIndex == -1) return 0;

        long long moves = 0;
        int left = (negativeIndex + n - 1) % n;
        int right = (negativeIndex + 1) % n;

        // Try balancing from both sides of the negative index
        while (deficit > 0 && left != right) {
            if (balance[left] > 0) {
                long long transferLeft = min(deficit, static_cast<long long>(balance[left]));
                deficit -= transferLeft;
                balance[left] -= transferLeft;
                moves += transferLeft * ((negativeIndex + n - left) % n);
            }
            left = (left + n - 1) % n;

            if (balance[right] > 0) {
                long long transferRight = min(deficit, static_cast<long long>(balance[right]));
                deficit -= transferRight;
                balance[right] -= transferRight;
                moves += transferRight * ((right + n - negativeIndex) % n);
            }
            right = (right + 1) % n;
        }

        // Verify if all balances are non-negative after processing
        for(int i=0; i<n; i++) {\