
class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')] = node
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    def containskey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        n=self.root
        for ch in word:
            if not n.containskey(ch):
                n.put(ch,Node())
            n=n.get(ch)
        n.setEnd()
    def search(self,word):
        n=self.root
        for ch in word:
            if not n.containskey(ch):
                return False
            n=n.get(ch)
        return n.isEnd()
    def startsWith(self,word):
        n = self.root
        for ch in word:
            if not n.containskey(ch):
                return False
            n = n.get(ch)
        return True
if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert("striver")
    trie.insert("striving")
    trie.insert("string")
    trie.insert("strike")

    print("Search if Strawberry exists in trie: " +
          ("True" if trie.search("strawberry") else "False"))

    print("Search if Strike exists in trie: " +
          ("True" if trie.search("strike") else "False"))

    print("If words in Trie start with Stri: " +
          ("True" if trie.startsWith("stri") else "False"))
