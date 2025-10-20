class Solution:
    def generateTag(self, caption: str) -> str:
        words = [word for word in caption.split() if word]
        for i in range(len(words)):
            if i == 0:
                words[i] = words[i][0].lower() + words[i][1:].lower()
            else:
                words[i] = words[i][0].upper() + words[i][1:].lower()
        
        result = '#' + ''.join(words)[:99]
        return result