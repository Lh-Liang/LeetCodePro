class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        int n = s.length();
        int[] answer = new int[queries.length];
        char[] arr = s.toCharArray();
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            if (query[0] == 1) { // Flip operation
                int j = query[1];
                arr[j] = arr[j] == 'A' ? 'B' : 'A';
            } else if (query[0] == 2) { // Compute operation
                int l = query[1], r = query[2];
                answer[i] = minDeletionsForAlternating(arr, l, r);
            }
        }
        return answer;
    }
    
    private int minDeletionsForAlternating(char[] arr, int l, int r) {
        int deletions1 = 0; // For pattern ABAB...
        int deletions2 = 0; // For pattern BABA...
        for (int i = l; i <= r; i++) {
            if ((i % 2 == 0 && arr[i] != 'A') || (i % 2 == 1 && arr[i] != 'B')) {
                deletions1++;
            } else if ((i % 2 == 0 && arr[i] != 'B') || (i % 2 == 1 && arr[i] != 'A')) {
                deletions2++;
            }
        }
        return Math.min(deletions1, deletions2);
    }
}