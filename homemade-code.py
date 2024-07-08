import string

# Sample text (replace this with a real sample text)
sample_text = "HELLO WORLD!"

# Define the homemade code (5 bits per character)
homemade_code = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100',
    'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001',
    'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110',
    'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000',
    'Z': '11001', ' ': '11010', ',': '11011', '.': '11100', '?': '11101',
    '!': '11110', '$': '11111'
}

# Encode the sample text using homemade code
encoded_homemade = ''.join(homemade_code[char] for char in sample_text.upper() if char in homemade_code)

# Calculate the number of bits
homemade_bits = len(encoded_homemade)

# Output the results
print(f"Sample text: {sample_text}")
print(f"Encoded with homemade code: {encoded_homemade}")
print(f"Number of bits using homemade code: {homemade_bits}")

# Calculate the number of bits using 8-bit ASCII
ascii_bits = len(sample_text) * 8

# Output the results for 8-bit ASCII
print(f"Number of bits using 8-bit ASCII: {ascii_bits}")

# Note: For Huffman coding, refer to the previous implementation steps.
