class Solution:
    def fullJustify(self, words, maxWidth):
        parent_pointers = {}
        memo = {}
        self.dp(0, words, maxWidth, memo, parent_pointers)
        
        i = 0
        result = []
        while i < len(words):
            _next = parent_pointers[i]
            
            line = words[i:_next]
            result.append(line)
            i = _next
                                    
        spaced_result = []
        for line in result[:-1]:
            spaced_result.append(self.make_space(line, maxWidth))
            
        last_line = " ".join(result[-1])
        n_spaces = maxWidth - sum(len(word) for word in last_line)
        for _ in range(n_spaces):
            last_line += " "
        
        spaced_result.append(last_line)
        
        return spaced_result
                
                    
    def calcBadness(self, subArray, pageWidth):
        subArray = [x + " " for x in subArray]
        totalWidth = sum(len(word) for word in subArray)
        if totalWidth > pageWidth + 1:
            return float('inf')
        return (pageWidth - totalWidth) ** 3
    
    def dp(self, i, wordsList, pageWidth, memo, parent_pointers): # solution to the suffix - words[i:]
        n = len(wordsList)
        
        if i in memo:
            return memo[i]
        
        if i == n:
            memo[i] = 0
            return 0
        
        minBadness = float('inf')
        for j in range(i+1, n+1):
            current_badness = self.dp(j, wordsList, pageWidth, memo, parent_pointers) + self.calcBadness(wordsList[i:j], pageWidth)
            if current_badness < minBadness:
                minBadness = current_badness
                parent_pointers[i] = j
        
        memo[i] = minBadness
        return minBadness
        
    def make_space(self, line, maxWidth):
        spaced_line = []
        
        charCount = sum(len(word) for word in line)
        n_spaces = maxWidth - charCount
        
        if len(line) == 1:
            spaced_line = line
            for i in range(n_spaces):
                spaced_line += " "
            return "".join(spaced_line)
        
        n_blocks =  n_spaces // (len(line) - 1) 
        remaining = n_spaces % (len(line) - 1) 
                
        for idx, word in enumerate(line[:-1]):
            spaced_line.append(word)
            spaces = " " * (n_blocks)
            if remaining > 0:
                spaces = " " * (n_blocks+1)
                remaining -= 1

            spaced_line.append(spaces)
            
        spaced_line.append(line[-1])
        
        return "".join(spaced_line)    

            