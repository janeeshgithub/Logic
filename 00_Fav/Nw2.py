class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Tracks the count of prefix sums ending at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.count += 1

    def get_count(self, num):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                return 0
            node = node.children[digit]
        return node.count

def subarray_sum_with_trie(nums, target):
    trie = Trie()
    prefix_sum = 0
    result = 0

    # Initialize the Trie with the prefix sum of 0 (base case)
    trie.insert(0)

    for num in nums:
        # Update the prefix sum
        prefix_sum += num

        # Check if there exists a prefix sum that when removed gives the target sum
        result += trie.get_count(prefix_sum - target)

        # Insert the current prefix sum into the Trie
        trie.insert(prefix_sum)

    return result

# Example Usage
nums = [1, 2, 3, -2, 5]
target = 3
print(subarray_sum_with_trie(nums, target))  # Output: Number of subarrays with sum = target
