class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def has_all_prefixes(self, word):
        current = self.root
        for char in word:
            if char not in current.children or not current.children[char].is_end_of_word:
                return False
            current = current.children[char]
        return True

def longest_string_with_all_prefixes(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)

    result = ""
    for string in strings:
        if trie.has_all_prefixes(string):
            if len(string) > len(result) or (len(string) == len(result) and string < result):
                result = string
    return result

# Example Usage:
strings = ["a", "ap", "app", "appl", "apple", "appli"]
print(longest_string_with_all_prefixes(strings))  # Output: "apple"
