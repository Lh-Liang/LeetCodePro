func lastInteger(n int64) int64 {
    if n == 1 {
        return 1
    }
    return 2 * (n/2 + 1 - lastInteger(n/2))
}