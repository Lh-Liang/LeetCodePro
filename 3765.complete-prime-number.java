#
# @lc app=leetcode id=3765 lang=java
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution {
    public boolean completePrime(int num) {
        // Convert num to string for prefix/suffix operations
        String numStr = Integer.toString(num);
        int length = numStr.length();
        
        // Check all prefixes and suffixes for primality
        for (int i = 1; i <= length; i++) {
            int prefix = Integer.parseInt(numStr.substring(0, i));
            int suffix = Integer.parseInt(numStr.substring(length - i));
            
            if (!isPrime(prefix) || !isPrime(suffix)) {
                return false;
            }
        }
        
        return true; // All checks passed, it's a complete prime number. 
    }
    
    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true; // special case for smallest even prime
        if (n % 2 == 0) return false; // eliminate even numbers > 2
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
# @lc code=end