class Node:
    def __init__(self):
        self.child = {}
        self.isComplete = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] =  Node()
            curr = curr.child[w]
        curr.isComplete = True

    def searchRec(self, curr,i,word):
        while i != len(word):

            if word[i] not in curr.child and word[i] != '.':
                return False
            elif word[i] == '.':
                for c in curr.child.values():
                    if self.searchRec(c,i+1,word):
                        return True
                return False        
            else:
                curr = curr.child[word[i]]
                i+=1

        return  curr.isComplete                    

    def search(self, word: str) -> bool:
        return self.searchRec(self.root,0,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)