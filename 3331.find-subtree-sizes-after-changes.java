#\n# @lc app=leetcode id=3331 lang=java\n#\n# [3331] Find Subtree Sizes After Changes\n#\n\n# @lc code=start\nclass Solution {\n    public int[] findSubtreeSizes(int[] parent, String s) {\n        int n = parent.length;\n        Map<Integer, List<Integer>> tree = new HashMap<>();\n        for (int i = 0; i < n; i++) {\n            tree.put(i, new ArrayList<>());\n        }\n        for (int i = 1; i < n; i++) {\n            tree.get(parent[i]).add(i);\n        }\n        int[] answer = new int[n];\n        Arrays.fill(answer, 1); // Initial subtree size is 1 for each node.\n        Map<Integer, Integer> pendingChanges = new HashMap<>(); // Store all pending changes.\n        \n        // Step to identify all changes first before applying them simultaneously.\n        for (int x = 1; x < n; x++) {\n            char currentChar = s.charAt(x);\n            int y = parent[x]; \t
            while (y != -1 && s.charAt(y) != currentChar) { \t
                y = parent[y]; // Move up to find matching character ancestor. \t
            } \t
            if (y != -1 && y != parent[x]) { \t
                pendingChanges.put(x, y); // Store change if a valid ancestor is found and it differs from current parent. \t
            } \t
        } \t
        \t
        // Apply stored changes simultaneously. \t
        for (Map.Entry<Integer, Integer> entry : pendingChanges.entrySet()) { \t
            int child = entry.getKey(); \t
            int newParent = entry.getValue(); \t
            tree.get(parent[child]).remove((Integer) child); // Remove child from old parent's list. \t
            parent[child] = newParent; // Update child's parent. \t
            tree.get(newParent).add(child); // Add child to new parent's list. \t
        } \t
        calculateSubtreeSizes(tree, answer, 0); // Calculate subtree sizes starting from root node 0. \t
        return answer; \t
    } \\\ \\\ private void calculateSubtreeSizes(Map<Integer, List<Integer>> tree, int[] answer, int node) { \\\ \\\ int size = 1; // Include the current node itself. \\\ \\\ for (int child : tree.get(node)) { \\\ \\\ size += calculateSubtreeSizes(tree, answer, child); // Accumulate sizes of subtrees recursively. \\\ \\\ } \\\ \\\ answer[node] = size; // Store calculated size in answer array. \\\ return size; // Return size for parent's calculation. \\\ } \\\ } # @lc code=end