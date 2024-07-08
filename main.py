import heapq
from collections import Counter, defaultdict

# Frequency table of English letters (including space)
frequency_table = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
    'Z': 0.074, ' ': 18.29
}

# Sample text (replace this with a real sample text)
sample_text = "this is a sample text to demonstrate huffman coding in action."

# Count frequency of each character in the sample text
sample_freq = Counter(sample_text.upper())

# Build Huffman Tree
heap = [[weight, [char, ""]] for char, weight in frequency_table.items()]
heapq.heapify(heap)

while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Generate Huffman codes
huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

# Calculate the number of bits needed using Huffman coding
huffman_bits = sum(sample_freq[char] * len(code) for char, code in huffman_codes if char in sample_freq)

# Calculate the number of bits needed using 8-bit ASCII
ascii_bits = len(sample_text) * 8

# Calculate the number of bits needed using home-made code (5 bits per character)
home_made_bits = len(sample_text) * 5

# Output the results
print(f"Huffman coding: {huffman_bits} bits")
print(f"8-bit ASCII: {ascii_bits} bits")
print(f"Home-made code: {home_made_bits} bits")

# Huffman Codes for reference
print("Huffman Codes:")
for char, code in huffman_codes:
    print(f"{char}: {code}")
