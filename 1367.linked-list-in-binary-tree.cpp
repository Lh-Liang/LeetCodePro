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
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false;
        // Step 1: Check if the sequence starts at the current node
        // Step 2: If not, recursively try starting the sequence from left or right children
        return check(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }

private:
    bool check(ListNode* head, TreeNode* node) {
        // Base Case: If we reached the end of the linked list, the path exists
        if (!head) return true;
        // Base Case: If the tree path ends or values don't match, the path is invalid
        if (!node || head->val != node->val) return false;
        
        // Recursive Step: Try to match the next list node in either child of the tree
        return check(head->next, node->left) || check(head->next, node->right);
    }
};
# @lc code=end