#
# @lc app=leetcode id=3538 lang=golang
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
func minTravelTime(l int, n int, k int, position []int, time []int) int {
    // Initialize total travel time
    totalTime := 0
    
    // Helper function to calculate total travel time given positions and times
    calcTotalTime := func(pos []int, t []int) int {
        tTime := 0
        for i := 0; i < len(pos)-1; i++ {
            distance := pos[i+1] - pos[i]
            tTime += distance * t[i]
        }
        return tTime
    }
    
    // Perform k merges by always merging segments with minimal additional cost
    for m := 0; m < k; m++ {
        minIncrease := int(^uint(0) >> 1) // Maximum possible integer value
        minIndex := -1
        
        // Find the best pair to merge that results in minimal increase of total time 
        for i := 1; i < len(time); i++ {
            newTime := time[i-1] + time[i]
            if newTime < minIncrease {
                minIncrease = newTime – time[i-1]–time[i]–time[i-1] –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i]; –time[i];}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}minIndex = i;}if min:}if min:}if min:}if min:}if min:}if min:}if min:}if min:}if min:}if min:}if min:}if min:}	// Merge signs at position[minIndex-1] and position[minIndex], update times accordingly}	position[minIndex-1] = position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[minIndex]}position[min Index-1] + position[Min index]= position[Min index]= Times[Min index]= Times[Min index]-=-=- + -=-=--=- -=--=- -=--=- -=--=- -=--=- -=--=- +=-=--=- +=-=--=- +=-=--+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-==+==+==+==+==+==+==+==+==+==+==}}}}}}}}return calcTotalTime(position, time)}// @lc code=end