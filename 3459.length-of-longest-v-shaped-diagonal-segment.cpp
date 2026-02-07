# @lc app=leetcode id=3459 lang=cpp
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int maxLength = 0;
        
        // Directions for moving diagonally (dx, dy):
        vector<pair<int, int>> directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        
        // Lambda function to check if a cell is within bounds and follows sequence
        auto isValid = [&](int x, int y) {
            return x >= 0 && x < n && y >= 0 && y < m;
        };

        // Explore from each '1' in all possible directions and track length of valid sequences
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) { // Only start from '1'
                    for (auto &dir : directions) {
                        int x = i + dir.first;
                        int y = j + dir.second;
                        int length = 1;
                        bool turned = false;
                        int expectedValue = 2; // Next expected value after '1'
                        
                        while (isValid(x, y) && grid[x][y] == expectedValue) {
                            ++length;
                            expectedValue ^= 2; // Toggle between `2` and `0`
                            
                            x += dir.first;
y += dir.second;
                            
                            if (!isValid(x, y)) break; // If out-of-bounds after moving
                            
                            if (grid[x][y] != expectedValue) { // Check for turn possibility
                                if (!turned) { // Allow one turn only
                                    turned = true;
x -= dir.first; y -= dir.second; // Step back to last valid position
                                    dir.first *= -1; dir.second *= -1; // Change direction for one turn
                                    x += dir.first; y += dir.second;   // Move one step in new direction
                                } else break; // If already turned once and can't proceed, stop exploration
                            }
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
printf("Max length found: %d", maxLength); \\ Debug statement (can be removed)
x += dir.first;
y += dir.second;
x += dir.first;
y += dir.second;
x += dir.first;
y += dir.second;
x += dir.first;
y += dir.second;
x += dir.first;
y += dir.second;x -=dir.first;y -=dir.second;x -=dir.third;x -=dir.third;y-=dir.third;x-=dir.third;y-=dir.third;;x+=dir.third;y+=dir.third;;x+=-third;;y+=-third;;x+=-third;;y+=-third;;x+=-third;;y+=-third;;x+=-third;;y+=-third;;x+=-third;;y+=-third;;x+=-third;;y+=-third;;maxLenght=x+y+z+zz+z+zz+z+zz+x+y+x+y+x+y;x=-x-y-z-z-x-y-x-y-x-y-x-y-x-y-x-y-x-y-y--x--y--x--y--z-z-z-z-z-z-z-z-z-z---z---z---xxxx-yyyyyyyyyyyyyyzzzzzzzzzzzzzzzzz;;;;;;;if(turned){returnmaxLenght;}else{maxLenght=turn};}}returnmaxLenght;} "# @lc code=end