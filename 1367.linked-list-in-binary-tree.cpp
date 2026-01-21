#
# @lc app=leetcode id=1367 lang=cpp
#
# [1367] Linked List in Binary Tree
#
# @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // Check if linked list matches a path starting from current tree node
    bool dfs(ListNode* head, TreeNode* root) {
        // If we've matched all nodes in the linked list
        if (head == nullptr) return true;
        
        // If tree node is null but list still has nodes
        if (root == nullptr) return false;
        
        // If values don't match
        if (head->val != root->val) return false;
        
        // Continue matching in left or right subtree
        return dfs(head->next, root->left) || dfs(head->next, root->right);
    }
    
    bool isSubPath(ListNode* head, TreeNode* root) {
        // If tree is empty
        if (root == nullptr) return false;
        
        // Try to match starting from current root,
        // or try starting from left subtree,
        // or try starting from right subtree
        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
};
# @lc code=end