class Solution {
public long totalWaviness(long num1, long num2) {
    // Iterate through each number in the range
    long totalWaviness = 0;
    for (long i = num1; i <= num2; i++) {
        String numStr = Long.toString(i);
        int length = numStr.length();
        // Waviness is only applicable for numbers with at least 3 digits
        if (length < 3) continue;
        int waviness = 0;
        // Check for peaks and valleys in middle digits
        for (int j = 1; j < length - 1; j++) {
            char prev = numStr.charAt(j - 1);
            char curr = numStr.charAt(j);
            char next = numStr.charAt(j + 1);
            if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
                waviness++;
            }
        }
        totalWaviness += waviness;
    }
    return totalWaviness;
}
}