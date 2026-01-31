#
# @lc app=leetcode id=3765 lang=cpp
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution {
public:
    /**
     * Standard primality test using trial division up to sqrt(n).
     * Time complexity: O(sqrt(n))
     */
    bool isPrime(long long n) {
        if (n < 2) return false;
        if (n == 2 || n == 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (long long i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    bool completePrime(int num) {
        // The number itself must be prime (it's both the longest prefix and suffix)
        if (!isPrime(num)) return false;

        // Check all other prefixes by removing digits from the right
        int prefix = num / 10;
        while (prefix > 0) {
            if (!isPrime(prefix)) return false;
            prefix /= 10;
        }

        // Check all other suffixes by keeping digits from the right
        long long mod = 10;
        while (mod < num) {
            if (!isPrime(num % mod)) return false;
            mod *= 10;
        }

        return true;
    }
};
# @lc code=end