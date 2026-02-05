class Solution {
    public long countSubstrings(String s) {
        long count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            int num = 0;
            for (int j = i; j < n; j++) {
                num = num * 10 + (s.charAt(j) - '0');
                int lastDigit = s.charAt(j) - '0';
                if (lastDigit != 0 && num % lastDigit == 0) {
                    count++;
                }
            }
        }
        return count;
    }
}