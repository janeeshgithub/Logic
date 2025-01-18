import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(data):
    frequencies = {}
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman Tree

def generate_codes(root, current_code, codes):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
        return
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

def huffman_encoding(data):
    if not data:
        return "", None

    frequencies = calculate_frequencies(data)
    root = build_huffman_tree(frequencies)
    codes = {}
    generate_codes(root, "", codes)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or not root:
        return ""

    decoded_data = []
    current = root
    for bit in encoded_data:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_data.append(current.char)
            current = root

    return "".join(decoded_data)

# Example Usage
if __name__ == "__main__":
    data = "HUFFMAN CODING"
    print(f"Original Data: {data}")

    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded Data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded Data: {decoded_data}")
