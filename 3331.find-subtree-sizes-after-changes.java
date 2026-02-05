#
# @lc app=leetcode id=3331 lang=java
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        // Step 1: Build initial tree
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) tree[parent[i]].add(i);
        
        // Step 2: Find new parents
        int[] newParent = parent.clone();
        Map<Character, Deque<Integer>> charStack = new HashMap<>();
        for (char c = 'a'; c <= 'z'; ++c) charStack.put(c, new ArrayDeque<>());
        
        dfsAssign(0, s, parent, newParent, charStack, tree);

        // Step 3: Build final tree
        List<Integer>[] finalTree = new ArrayList[n];
        for (int i = 0; i < n; ++i) finalTree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) finalTree[newParent[i]].add(i);

        // Step 4: Validate the tree structure (optional, but recommended)
        // e.g., check for cycles, all nodes have one parent, etc. (omitted for brevity)

        // Step 5: Compute subtree sizes
        int[] answer = new int[n];
        computeSizes(0, finalTree, answer);

        // Step 6: Self-checks
        if (answer.length != n) throw new RuntimeException("Incorrect answer array length");
        int total = 0;
        for (int v : answer) total += v;
        if (total != n * 1) throw new RuntimeException("Total node counts mismatch after transformation");
        return answer;
    }
    
    private void dfsAssign(int node, String s, int[] parent, int[] newParent, Map<Character, Deque<Integer>> charStack, List<Integer>[] tree) {
        char c = s.charAt(node);
        charStack.get(c).push(node);
        for (int child : tree[node]) {
            char childChar = s.charAt(child);
            Deque<Integer> stack = charStack.get(childChar);
            if (!stack.isEmpty() && stack.peek() != child) {
                newParent[child] = stack.peek();
            }
            dfsAssign(child, s, parent, newParent, charStack, tree);
        }
        charStack.get(c).pop();
    }

    private int computeSizes(int node, List<Integer>[] tree, int[] answer) {
        int size = 1;
        for (int child : tree[node]) {
            size += computeSizes(child, tree, answer);
        }
        answer[node] = size;
        return size;
    }
}
# @lc code=end