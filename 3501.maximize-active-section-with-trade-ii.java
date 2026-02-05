import java.util.*;
class Solution {
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int l = q[0], r = q[1];
            String t = "1" + s.substring(l, r + 1) + "1";
            int len = t.length();
            List<Block> blocks = new ArrayList<>();
            int i = 0;
            while (i < len) {
                int j = i;
                char c = t.charAt(i);
                while (j < len && t.charAt(j) == c) j++;
                blocks.add(new Block(i, j - 1, c));
                i = j;
            }
            int currActive = 0;
            for (int k = 1; k < blocks.size() - 1; ++k) {
                if (blocks.get(k).type == '1') currActive++;
            }
            int maxActive = currActive;
            for (int k = 1; k < blocks.size() - 1; ++k) {
                if (blocks.get(k).type == '1' && blocks.get(k-1).type == '0' && blocks.get(k+1).type == '0') {
                    List<Block> newBlocks = new ArrayList<>();
                    for (int m = 0; m < blocks.size(); ++m) {
                        if (m == k) {
                            newBlocks.add(new Block(blocks.get(m).start, blocks.get(m).end, '0'));
                        } else {
                            newBlocks.add(blocks.get(m).clone());
                        }
                    }
                    List<Block> merged = new ArrayList<>();
                    for (Block b : newBlocks) {
                        if (merged.isEmpty() || merged.get(merged.size()-1).type != b.type) {
                            merged.add(b.clone());
                        } else {
                            merged.get(merged.size()-1).end = b.end;
                        }
                    }
                    boolean flip = false;
                    for (int y = 1; y < merged.size() - 1; ++y) {
                        if (merged.get(y).type == '0' && merged.get(y-1).type == '1' && merged.get(y+1).type == '1') {
                            flip = true;
                            int newActive = 0;
                            for (int z = 1; z < merged.size() - 1; ++z) {
                                char ch = merged.get(z).type;
                                if (z == y) ch = '1';
                                if (ch == '1') newActive++;
                            }
                            maxActive = Math.max(maxActive, newActive);
                        }
                    }
                    if (!flip) {
                        int newActive = 0;
                        for (int z = 1; z < merged.size() - 1; ++z) {
                            if (merged.get(z).type == '1') newActive++;
                        }
                        maxActive = Math.max(maxActive, newActive);
                    }
                }
            }
            ans.add(maxActive);
        }
        return ans;
    }
    static class Block implements Cloneable {
        int start, end;
        char type;
        Block(int s, int e, char t) { start = s; end = e; type = t; }
        public Block clone() { return new Block(start, end, type); }
    }
}