func maximumCoins(coins [][]int, k int) int64 {
    events := []struct {pos, change int}{}
    for _, segment := range coins {
        li, ri, ci := segment[0], segment[1], segment[2]
        events = append(events, struct {pos, change int}{li, ci})
        events = append(events, struct {pos, change int}{ri + 1, -ci})
    }
    
    sort.Slice(events, func(i, j int) bool { return events[i].pos < events[j].pos })
    
    currentCoins := int64(0)
    maxCoins := int64(0)
    windowCoins := int64(0)
    deque := []int{} // To maintain indices in a sliding window fashion
    prevPos := -1
    
    for i := 0; i < len(events); {
        pos := events[i].pos
        if prevPos != -1 && pos > prevPos {
            distance := pos - prevPos
            windowCoins += currentCoins * int64(distance)
            while len(deque) > 0 && (events[deque[0]].pos < pos - k + 1) {
                oldIndex := deque[0]
                oldPos := events[oldIndex].pos
                nextPos := events[oldIndex+1].pos
                if nextPos > pos - k + 1 {
                    nextPos = pos - k + 1
                }
                deltaDistance := nextPos - oldPos
                windowCoins -= currentCoins * int64(deltaDistance)
                deque = deque[1:]
            }
            maxCoins = max(maxCoins, windowCoins)
        }
        
        for ; i < len(events) && events[i].pos == pos; i++ {
            currentCoins += int64(events[i].change)
            if events[i].change > 0 {
                deque = append(deque, i)
            }
        }
        prevPos = pos
    }
    
    return maxCoins
}

func max(a, b int64) int64 {
    if a > b { return a }
    return b
}