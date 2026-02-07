func maxSubstringLength(s string, k int) bool {
    if k == 0 {
        return true
    }
    
    charFrequency := make(map[rune]int)
    for _, char := range s {
        charFrequency[char]++
    }
    
    potentialStarters := make(map[rune]bool)
    for char, count := range charFrequency {
        if count == 1 {
            potentialStarters[char] = true
        }
    }

    usedChars := make(map[rune]bool)
    specialCount := 0

    for i := 0; i < len(s); i++ {
        ch := rune(s[i])
        if potentialStarters[ch] && !usedChars[ch] {
            j := i
            tempUsedChars := make(map[rune]bool)
            isValid := true
            for j < len(s) && isValid {
                currentChar := rune(s[j])
                if charFrequency[currentChar] > 1 || tempUsedChars[currentChar] {
                    isValid = false
                    break
                }
                tempUsedChars[currentChar] = true
                j++
            }
            if isValid && len(tempUsedChars) > 0 {
                for c := range tempUsedChars {
                    usedChars[c] = true
                }
                specialCount++
                if specialCount >= k {
                    return true
                }
            }
        }
    }
    return false
}