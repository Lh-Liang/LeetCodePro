#
# @lc app=leetcode id=3435 lang=java
#
# [3435] Frequencies of Shortest Supersequences
#
# @lc code=start
import java.util.*;
class Solution {
    public List<List<Integer>> supersequences(String[] words) {
        // Step 1: Get all unique characters
        Set<Character> chars = new HashSet<>();
        for (String w : words) for (char c : w.toCharArray()) chars.add(c);
        List<Character> alphabet = new ArrayList<>(chars);
        // Step 2: BFS for SCSs
        Set<String> scsSet = new HashSet<>();
        Queue<State> queue = new LinkedList<>();
        queue.offer(new State(new int[words.length], new StringBuilder()));
        int minLen = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            State cur = queue.poll();
            if (cur.isDone(words)) {
                if (cur.sb.length() < minLen) {
                    scsSet.clear(); minLen = cur.sb.length();
                }
                if (cur.sb.length() == minLen) scsSet.add(cur.sb.toString());
                continue;
            }
            for (char c : alphabet) {
                int[] nextIdx = Arrays.copyOf(cur.idx, words.length);
                boolean advanced = false;
                for (int i = 0; i < words.length; ++i) {
                    if (nextIdx[i] < words[i].length() && words[i].charAt(nextIdx[i]) == c) {
                        nextIdx[i]++; advanced = true;
                    }
                }
                if (advanced) {
                    StringBuilder nsb = new StringBuilder(cur.sb);
                    nsb.append(c);
                    queue.offer(new State(nextIdx, nsb));
                }
            }
        }
        // Step 3: Get unique frequency arrays
        Set<List<Integer>> freqset = new HashSet<>();
        for (String s : scsSet) {
            int[] freq = new int[26];
            for (char c : s.toCharArray()) freq[c-'a']++;
            List<Integer> freqList = new ArrayList<>();
            for (int i=0;i<26;++i) freqList.add(freq[i]);
            freqset.add(freqList);
        }
        return new ArrayList<>(freqset);
    }
    static class State {
        int[] idx; StringBuilder sb;
        State(int[] idx, StringBuilder sb) { this.idx=idx; this.sb=sb; }
        boolean isDone(String[] words) {
            for (int i=0;i<words.length;++i) if (idx[i]!=words[i].length()) return false;
            return true;
        }
    }
}
# @lc code=end