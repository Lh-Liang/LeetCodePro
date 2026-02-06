#
# @lc app=leetcode id=3530 lang=java
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
class Solution {
    public int maxProfit(int n, int[][] edges, int[] score) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            inDegree[edge[1]]++;
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>((a, b) -> Integer.compare(score[b], score[a]));
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        int position = 1; // start position from 1 as per problem statement
        int maxProfit = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            maxProfit += position * score[node];
            position++; // increment position for next node in topological order
            for (int neighbor : graph.get(node)) {
                if (--inDegree[neighbor] == 0) { // reduce in-degree and check if it becomes zero to add to queue. 
                    queue.offer(neighbor); 
                } 
            } 
        } 
        return maxProfit; 
    } 
} 
# @lc code=end