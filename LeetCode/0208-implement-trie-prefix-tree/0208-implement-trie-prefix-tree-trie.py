class Trie:
    def __init__(self):
        self.root = {'childs':{}, 'is_word':False}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur['childs']:
                cur['childs'][c] = {'childs':{}, 'is_word':False}
            
            cur = cur['childs'][c]
        
        cur['is_word'] = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur['childs']:
                return False
            
            cur = cur['childs'][c]
        
        return cur['is_word']

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur['childs']:
                return False
            
            cur = cur['childs'][c]
        
        return cur['is_word'] or len(cur['childs'].keys()) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)