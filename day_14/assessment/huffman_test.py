import heapq
import os
from collections import Counter, namedtuple

# Define a simple Node class for Huffman Tree
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, freq_val, None, None) for char, freq_val in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node is None:
        return codebook
    if node.char is not None:
        codebook[node.char] = prefix
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_encode(text, codebook):
    return "".join(codebook[ch] for ch in text)


def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for _ in range(extra_padding):
        encoded_text += "0"
    padded_info = "{0:08b}".format(extra_padding)
    return padded_info + encoded_text


def get_byte_array(padded_encoded_text):
    if len(padded_encoded_text) % 8 != 0:
        raise ValueError("Encoded text not padded properly")
    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b


def compress(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    huffman_tree = build_huffman_tree(text)
    codebook = generate_codes(huffman_tree)
    encoded_text = huffman_encode(text, codebook)
    padded_encoded_text = pad_encoded_text(encoded_text)
    byte_array = get_byte_array(padded_encoded_text)

    with open(output_file, 'wb') as output:
        output.write(bytes(byte_array))

    print(f" Compression complete: {input_file} → {output_file}")
    return codebook, len(encoded_text), len(byte_array) * 8


def remove_padding(padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    encoded_text = padded_encoded_text[8:]
    return encoded_text[:-extra_padding]


def decompress(input_file, output_file, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}

    with open(input_file, 'rb') as file:
        bit_string = ""
        byte = file.read(1)
        while byte:
            bits = bin(ord(byte))[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

    actual_text = remove_padding(bit_string)

    current_code = ""
    decoded_chars = []  # Use a list (faster than string concatenation)
    for bit in actual_text:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_chars.append(reverse_codebook[current_code])
            current_code = ""

    decoded_text = ''.join(decoded_chars)  # Join once at the end

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(decoded_text)

    print(f"✅ Decompression complete: {input_file} → {output_file}")



def compare_files(file1, file2):
    """Compare two text files for integrity."""
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        return f1.read() == f2.read()


def compression_ratio(original_bits, compressed_bits):
    return original_bits / compressed_bits


if __name__ == "__main__":
    # Step 1: Generate or use an existing text file
    input_file = "large_text.txt"       # You can replace this with your Gutenberg file
    compressed_file = "compressed.bin"
    decompressed_file = "decompressed.txt"

    # Step 2: Compress
    codebook, original_bits, compressed_bits = compress(input_file, compressed_file)

    # Step 3: Decompress
    decompress(compressed_file, decompressed_file, codebook)

    # Step 4: Compare integrity
    if compare_files(input_file, decompressed_file):
        print(" File integrity check PASSED — files are identical.")
    else:
        print(" File integrity check FAILED — files differ.")

    # Step 5: Print compression ratio
    ratio = compression_ratio(original_bits, compressed_bits)
    print(f" Compression Ratio: {ratio:.2f} (Original/Compressed)")
