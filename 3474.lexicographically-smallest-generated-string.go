func generateString(str1 string, str2 string) string {
    n, m := len(str1), len(str2)
    word := make([]byte, n+m-1)
    for i := range word {
        word[i] = 'a' // Use 'a' as default
    }

    // Process each character in str1
    for i := 0; i < n; i++ {
        if str1[i] == 'T' {
            // Ensure substring matches str2 starting at i
            for j := 0; j < m && (i+j) < len(word); j++ {
                word[i+j] = str2[j]
            }
        } else { // str1[i] == 'F'
            // Ensure no matching substring starts at i
            mismatch := false
            for j := 0; j < m && (i+j) < len(word); j++ {
                if word[i+j] == str2[j] {
                    mismatch = true
                    break
                }
            }
            if !mismatch {
                for j := 0; j < m && (i+j) < len(word); j++ {
                    if word[i+j] == str2[j] {
                        // Change to a non-matching character
                        word[i+j] = byte((int(word[i+j]-'a')+1)%26 + 'a')
                    }
                }
            }
        }
    }
    return string(word)
}