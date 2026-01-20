#include <cmath>

class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        long long csx = sx, csy = sy, ctx = tx, cty = ty;
        long long moves = 0;

        while (true) {
            if (ctx == csx && cty == csy) return (int)moves;
            if (ctx < csx || cty < csy) return -1;

            if (ctx > cty) {
                if (ctx >= 2 * cty && cty > 0) {
                    if (ctx % 2 != 0) return -1;
                    ctx /= 2;
                    moves++;
                } else if (ctx > cty) {
                    ctx -= cty;
                    moves++;
                } else {
                    // This case is handled by ctx == cty
                    break;
                }
            } else if (cty > ctx) {
                if (cty >= 2 * ctx && ctx > 0) {
                    if (cty % 2 != 0) return -1;
                    cty /= 2;
                    moves++;
                } else if (cty > ctx) {
                    cty -= ctx;
                    moves++;
                } else {
                    break;
                }
            } else {
                // ctx == cty and ctx > 0
                if (csx == 0 && csy > 0) {
                    if (cty % csy == 0) {
                        long long ratio = cty / csy;
                        if ((ratio & (ratio - 1)) == 0) {
                            return (int)(moves + 1 + log2(ratio));
                        }
                    }
                }
                if (csy == 0 && csx > 0) {
                    if (ctx % csx == 0) {
                        long long ratio = ctx / csx;
                        if ((ratio & (ratio - 1)) == 0) {
                            return (int)(moves + 1 + log2(ratio));
                        }
                    }
                }
                return -1;
            }
        }
        return -1;
    }

private:
    int log2(long long n) {
        int res = 0;
        while (n > 1) {
            n >>= 1;
            res++;
        }
        return res;
    }
};