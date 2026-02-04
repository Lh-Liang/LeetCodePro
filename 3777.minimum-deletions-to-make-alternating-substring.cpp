#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#
# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Result {
    int minDel[2]; // [start with 'A', start with 'B']
    char first[2], last[2];
    int len;
    Result() {
        minDel[0] = minDel[1] = 0;
        first[0] = first[1] = 0;
        last[0] = last[1] = 0;
        len = 0;
    }
    Result(char c) {
        minDel[0] = (c == 'A' ? 0 : 1);
        minDel[1] = (c == 'B' ? 0 : 1);
        first[0] = last[0] = 'A';
        first[1] = last[1] = 'B';
        len = 1;
    }
};

Result merge(const Result &left, const Result &right) {
    Result res;
    res.len = left.len + right.len;
    for (int st = 0; st < 2; ++st) {
        int leftSt = st;
        int rightSt = (left.len % 2 == 0) ? st : 1 - st;
        res.first[st] = left.first[leftSt];
        res.last[st] = right.last[rightSt];
        res.minDel[st] = left.minDel[leftSt] + right.minDel[rightSt];
        if (left.last[leftSt] == right.first[rightSt]) res.minDel[st] += 1;
    }
    return res;
}

class SegmentTree {
    vector<Result> tree;
    int n;
    string &s;
public:
    SegmentTree(string &str): s(str) {
        n = s.size();
        tree.resize(4 * n);
        build(1, 0, n - 1);
    }
    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = Result(s[l]);
            return;
        }
        int m = (l + r) / 2;
        build(node * 2, l, m);
        build(node * 2 + 1, m + 1, r);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }
    void update(int node, int l, int r, int idx) {
        if (l == r) {
            s[idx] = (s[idx] == 'A' ? 'B' : 'A');
            tree[node] = Result(s[idx]);
            return;
        }
        int m = (l + r) / 2;
        if (idx <= m) update(node * 2, l, m, idx);
        else update(node * 2 + 1, m + 1, r, idx);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }
    Result query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return Result();
        if (ql <= l && r <= qr) return tree[node];
        int m = (l + r) / 2;
        Result left = query(node * 2, l, m, ql, qr);
        Result right = query(node * 2 + 1, m + 1, r, ql, qr);
        if (left.len == 0) return right;
        if (right.len == 0) return left;
        return merge(left, right);
    }
    void flip(int idx) { update(1, 0, n - 1, idx); }
    int min_del(int l, int r) {
        Result res = query(1, 0, n - 1, l, r);
        return min(res.minDel[0], res.minDel[1]);
    }
};

class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        SegmentTree seg(s);
        vector<int> ans;
        for (const auto& q : queries) {
            if (q[0] == 1) {
                seg.flip(q[1]);
            } else {
                ans.push_back(seg.min_del(q[1], q[2]));
            }
        }
        return ans;
    }
};
# @lc code=end