from idlelib.tree import TreeNode


class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,num):
        node=self.root
        for i in str(num):
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.count+=1
    def get_count(self,num):
        node=self.root
        for i in str(num):
            if i not in node.children:
                return 0
            node=node.children[i]
        return node.count
def sas(nums,target):
    trie=Trie()
    ps=0
    r=0
    trie.insert(0)
    for i in nums:
        ps+=i
        r+=trie.get_count(ps-target)
        trie.insert(ps)
    return r

nums = [1, 2, 3, -2, 5]
target = 3
print(sas(nums, target))