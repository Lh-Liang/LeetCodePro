#
# @lc app=leetcode id=3625 lang=golang
#
# [3625] Count Number of Trapezoids II
#
# @lc code=start
func countTrapezoids(points [][]int) int {
    type Point struct{ x, y int }
    n := len(points)
    pts := make([]Point, n)
    for i, p := range points {
        pts[i] = Point{p[0], p[1]}
    }
    type Slope struct{ dy, dx int }
    gcd := func(a, b int) int {
        if a < 0 { a = -a }
        if b < 0 { b = -b }
        for b != 0 { a, b = b, a%b }
        return a
    }
    slope := func(a, b Point) Slope {
        dx, dy := b.x - a.x, b.y - a.y
        if dx == 0 && dy == 0 {
            return Slope{0, 0}
        }
        g := gcd(dx, dy)
        if g != 0 { dx /= g; dy /= g }
        if dx < 0 || (dx == 0 && dy < 0) {
            dx, dy = -dx, -dy
        }
        return Slope{dy, dx}
    }
    isConvex := func(q []Point) bool {
        n := len(q)
        sign := 0
        for i := 0; i < n; i++ {
            dx1 := q[(i+1)%n].x - q[i].x
            dy1 := q[(i+1)%n].y - q[i].y
            dx2 := q[(i+2)%n].x - q[(i+1)%n].x
            dy2 := q[(i+2)%n].y - q[(i+1)%n].y
            cross := dx1*dy2 - dy1*dx2
            if cross != 0 {
                if sign == 0 {
                    sign = cross
                } else if sign*cross < 0 {
                    return false
                }
            }
        }
        return true
    }
    isTrapezoid := func(q []Point) bool {
        s := make([]Slope, 4)
        for i := 0; i < 4; i++ {
            s[i] = slope(q[i], q[(i+1)%4])
        }
        cnt := 0
        if s[0] == s[2] { cnt++ }
        if s[1] == s[3] { cnt++ }
        return cnt >= 1
    }
    seen := map[[4]int]struct{}{}
    count := 0
    for a := 0; a < n; a++ {
        for b := a+1; b < n; b++ {
            for c := b+1; c < n; c++ {
                for d := c+1; d < n; d++ {
                    idxs := []int{a, b, c, d}
                    ps := []Point{pts[a], pts[b], pts[c], pts[d]}
                    orders := [][]int{
                        {0,1,2,3},{0,1,3,2},{0,2,1,3},{0,2,3,1},{0,3,1,2},{0,3,2,1},
                    }
                    found := false
                    for _, order := range orders {
                        quad := []Point{ps[order[0]], ps[order[1]], ps[order[2]], ps[order[3]]}
                        if isConvex(quad) && isTrapezoid(quad) {
                            arr := []int{idxs[order[0]], idxs[order[1]], idxs[order[2]], idxs[order[3]]}
                            sort.Ints(arr)
                            key := [4]int{arr[0],arr[1],arr[2],arr[3]}
                            if _, ok := seen[key]; !ok {
                                seen[key] = struct{}{}
                                count++
                            }
                            found = true
                            break
                        }
                    }
                }
            }
        }
    }
    return count
}
# @lc code=end