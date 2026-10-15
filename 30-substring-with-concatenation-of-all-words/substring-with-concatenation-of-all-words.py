from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        s_len = len(s)
        
        # Frequency map for the target words
        word_freq = Counter(words)
        result = []
        
        # Run sliding window for each offset from 0 up to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()
            words_matched = 0
            
            # Slide the window across the string
            while right + word_len <= s_len:
                # Extract the next word candidate from the right
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_freq[word] += 1
                    words_matched += 1
                    
                    # If we have too many occurrences of 'word', shift left pointer
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        words_matched -= 1
                        left += word_len
                        
                    # If all words are perfectly matched, we found a valid index
                    if words_matched == word_count:
                        result.append(left)
                        
                else:
                    # Invalid word: clear the window state and jump past it
                    current_freq.clear()
                    words_matched = 0
                    left = right
                    
        return result
