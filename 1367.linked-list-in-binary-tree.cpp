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
    // Helper function to check if linked list starting from head matches
    // the downward path starting from root
    bool dfs(ListNode* head, TreeNode* root) {
        if (!head) return true;  // Matched all nodes in linked list
        if (!root) return false; // Tree ended but linked list didn't
        if (root->val != head->val) return false; // Values don't match
        
        // Check if rest of linked list matches left or right subtree
        return dfs(head->next, root->left) || dfs(head->next, root->right);
    }
    
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false; // Empty tree
        
        // Check if path starts from current root, or from left/right subtree
        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
};
# @lc code=end