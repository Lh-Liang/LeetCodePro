public int[] resultArray(int[] nums, int k, int[][] queries) {
    int n = nums.length;
    int[] result = new int[queries.length];
    
    // Precompute prefix products modulo k
    int[] prefixProductMod = new int[n + 1];
    prefixProductMod[0] = 1;
    for (int i = 0; i < n; i++) {
        prefixProductMod[i + 1] = (int)(((long)prefixProductMod[i] * nums[i]) % k);
    }

    for (int q = 0; q < queries.length; q++) {
        int index = queries[q][0];
        int value = queries[q][1];
        int start = queries[q][2];
        int x = queries[q][3];
        
        // Update nums at index with value and recompute affected prefix products
        nums[index] = value;
        for (int i = index; i < n; i++) {
            prefixProductMod[i + 1] = (int)(((long)prefixProductMod[i] * nums[i]) % k);
        }

        // Calculate product from start to end modulo k using precomputed prefix products
        long totalProductModFromStart = (prefixProductMod[n] * powMod(prefixProductMod[start], k - 2, k)) % k;

        // Count valid suffixes producing remainder x when taken modulo k
        int count = 0;
        long currentProductMod = totalProductModFromStart;
        for (int i = n - 1; i >= start - 1; i--) { // Consider empty prefix as well
            if (currentProductMod == x) {
                count++; // Valid suffix removal leaving remainder x modulo k
            }
            if (i >= start) { // Update currentProductMod only within valid range
                currentProductMod = (currentProductMod * powMod(nums[i], k - 2, k)) % k;
            } else {
                break;
            }
        }
        result[q] = count;
    }
    return result;
}

// Helper function to compute modular inverse using Fermat's Little Theorem if applicable or alternative direct computation
private long powMod(long base, long exp, long mod) {
    long result = 1;
    while (exp > 0) {
        if ((exp & 1) == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}