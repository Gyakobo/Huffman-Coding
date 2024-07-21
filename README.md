# Huffman Coding

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

>[!NOTE]
>Please feel free to make pull requests and edit this project to your will.

## Introduction

[**Huffman Coding**](https://en.wikipedia.org/wiki/Huffman_coding) is a widely used method of lossless data compression. It was developed by [David A. Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) while he was a Ph.D. student at MIT, and it was published in his seminal paper in 1952. The algorithm is used to compress data by assigning variable-length codes to characters based on their frequencies. Characters that occur more frequently are given shorter codes, while less frequent characters are assigned longer codes. This approach reduces the overall size of the encoded data.

### The process of Huffman Coding involves:

1. *Frequency Analysis*: Calculate the frequency of each character in the input data.

1. *Building a Huffman Tree*: Create a binary tree where each leaf node represents a character and its frequency. The tree is built by repeatedly merging the two nodes with the lowest frequencies until only one node remains (the root of the tree).

1. *Generating Codes*: Assign binary codes to characters by traversing the Huffman Tree. Each left edge represents `0`, and each right edge represents a `1`.

Huffman Coding is optimal for symbol-by-symbol encoding and is widely used in various applications such as file compression (e.g., [ZIP](https://en.wikipedia.org/wiki/ZIP_(file_format)) files), image compression (e.g., [JPEG](https://en.wikipedia.org/wiki/JPEG)), and multimedia codecs (e.g., [MP3](https://en.wikipedia.org/wiki/MP3)).

### Introduction to David A. Huffman

[David A. Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) (August 9, 1925 - October 7, 1999) was an American computer scientist and professor, known for his pioneering work in the field of information theory and data compression. Huffman was in Ohio and went on to study at the Massachussets Institute of Technology (MIT), where he completed his Ph.D. in electrical engineering.

While still a graduate student, Huffman devised the [Huffman Coding algorithm](https://en.wikipedia.org/wiki/Huffman_coding) as part of a term paper for a course on information theory taught by [Robert M. Fano](https://en.wikipedia.org/wiki/Huffman_coding). His algorithm quickly became a fundamental technique in the field of data compression due to its efficiency and simplicity.

Throughout his career, Huffman made significant contributions to various areas of computer science and engineering. He was a professor at MIT and later at the University of California, Santa Cruz, where he helped establish the Computer Science Department.

David Huffman's work has had a lasting impact on how data is efficiently stored and quickly transmitted, and his legacy continues to influence modern computing and telecommunications.

## Methodology

### Step 1: Frequency Table of English Letters

First, we need a frequency table for the English letters. Here's a commonly used table based on large corpora of English texts. Below is a representation in Python code:

```python3
# Frequency table of English letters (including space)
frequency_table = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
    'Z': 0.074, ' ': 18.29
}
```

<table>

<thead>
<td>Letter</td>
<td>Frequency (%)</td>
<td>Letter</td>
<td>Frequency (%)</td>
</thead>

<tr>
<td>A</td><td>8.167</td>
<td>B</td><td>1.492</td>
</tr>

<tr>
<td>C</td><td>2.782</td>
<td>D</td><td>4.253</td>
</tr>

<tr>
<td>E</td><td>12.702</td>
<td>F</td><td>2.228</td>
</tr>

<tr>
<td>G</td><td>2.015</td>
<td>H</td><td>6.094</td>
</tr>

<tr> 
<td>I</td><td>6.966</td>
<td>J</td><td>0.153</td>
</tr>

<tr>
<td>K</td><td>0.772</td>
<td>L</td><td>4.025</td>
</tr>

<tr>
<td>M</td><td>2.406</td>
<td>N</td><td>6.749</td>
</tr>

<tr>
<td>O</td><td>7.507</td>
<td>P</td><td>1.929</td>
</tr>

<tr> 
<td>Q</td><td>0.095</td>
<td>R</td><td>5.987</td>
</tr>

<tr>
<td>S</td><td>6.327</td>
<td>T</td><td>9.056</td>
</tr>

<tr>
<td>U</td><td>2.758</td>
<td>V</td><td>0.978</td>
</tr>

<tr>
<td>W</td><td>2.36</td>
<td>X</td><td>0.15</td>
</tr>

<tr>
<td>Y</td><td>1.974</td>
<td>Z</td><td>0.074</td>
</tr>

<tr>
<td>SPACE</td><td>18.29</td>
</tr>

</table>

### Step 2: Build a Huffman Code for English

We still use the frequency table to build a Huffman Tree and derive the Huffman codes for each character. Here's a simplified version of the process:

1. **Initialize**: Create a leaf node for each character and add it to a priority queue based on frequency. 

```python
# Count frequency of each character in the sample text
sample_freq = Counter(sample_text.upper())
```

2. **Build the Tree**:
* Extract two nodes with the lowest frequency.
* Create a new internal node with these two nodes as children and the sum of their frequencies as the new frequency.
* Insert the new node back into the priority queue.
* Repeat until only one node (the root) remains.

```python
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
```

3. **Generate Codes**: Traverse the tree to assign codes to each character.

```python
# Generate Huffman codes
huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

# Calculate the number of bits needed using Huffman coding
huffman_bits = sum(sample_freq[char] * len(code) for char, code in huffman_codes if char in sample_freq)
```

To run the final program please just run the [main file](https://github.com/Gyakobo/Huffman-Coding/blob/main/main.py). I also wrote a sample encoder that encodes any input with arbitrary bits just for you, my dear reader, to compare their inherit weights. 

## Conclusion

David A. Huffman, though his groundbreaking development of Huffman Coding, revolutionized the field of data compression. His algorithm, created during his time as a Ph.D. student at MIT, stands as a testament to the power of innovative thinking in solving practical problems. Huffman Coding's efficient method of variable-length encoding based on character frequency not only optimizes data storage and transmission but also underpins many modern compression techniques used in everyday digital media. Huffman's work exemplifies the profound impact that a single, elegant solution can have on technology, shaping the way we manage and process information in the digital age.

## License
MIT
