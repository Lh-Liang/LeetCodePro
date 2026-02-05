import java.util.*;
class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        int n = intervals.size();
        int[][] arr = new int[n][4]; // [start, end, weight, original_idx]
        for (int i = 0; i < n; ++i) {
            List<Integer> curr = intervals.get(i);
            arr[i][0] = curr.get(0);
            arr[i][1] = curr.get(1);
            arr[i][2] = curr.get(2);
            arr[i][3] = i;
        }
        Arrays.sort(arr, Comparator.comparingInt(a -> a[1]));
        int[] prev = new int[n];
        Arrays.fill(prev, -1);
        for (int i = 0; i < n; ++i) {
            int lo = 0, hi = i - 1, p = -1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid][1] < arr[i][0]) {
                    p = mid; lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            prev[i] = p;
        }
        class State {
            long score;
            ArrayList<Integer> indices;
            State(long s, ArrayList<Integer> idxs) { score = s; indices = idxs; }
        }
        State[][] dp = new State[n + 1][5];
        for (int i = 0; i <= n; ++i) {
            for (int k = 0; k <= 4; ++k) {
                dp[i][k] = new State(0, new ArrayList<>());
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k <= 4; ++k) {
                State notPick = dp[i-1][k];
                State pick = null;
                int pre = prev[i-1];
                if (pre >= 0) pick = dp[pre+1][k-1];
                else if (k == 1) pick = new State(0, new ArrayList<>());
                if (pick != null) {
                    long newScore = pick.score + arr[i-1][2];
                    ArrayList<Integer> newIdx = new ArrayList<>(pick.indices);
                    newIdx.add(arr[i-1][3]);
                    if (newScore > notPick.score) {
                        dp[i][k] = new State(newScore, newIdx);
                    } else if (newScore == notPick.score) {
                        if (compare(newIdx, notPick.indices) < 0) {
                            dp[i][k] = new State(newScore, newIdx);
                        } else {
                            dp[i][k] = notPick;
                        }
                    } else {
                        dp[i][k] = notPick;
                    }
                } else {
                    dp[i][k] = notPick;
                }
            }
        }
        State best = dp[n][1];
        for (int k = 2; k <= 4; ++k) {
            State cur = dp[n][k];
            if (cur.score > best.score) best = cur;
            else if (cur.score == best.score && compare(cur.indices, best.indices) < 0) best = cur;
        }
        int[] res = new int[best.indices.size()];
        for (int i = 0; i < res.length; ++i) res[i] = best.indices.get(i);
        return res;
    }
    private int compare(List<Integer> a, List<Integer> b) {
        int n = Math.min(a.size(), b.size());
        for (int i = 0; i < n; ++i) {
            if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
        }
        return a.size() - b.size();
    }
}