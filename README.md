# Huffman Coding

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Introduction

[**Huffman Coding**](https://en.wikipedia.org/wiki/Huffman_coding) is a widely used method of lossless data compression. It was developed by [David A. Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) while he was a Ph.D. student at MIT, and it was published in his seminal paper in 1952. The algorithm is used to compress data by assigning variable-length codes to characters based on their frequencies. Characters that occur more frequently are given shorter codes, while less frequent characters are assigned longer codes. This approach reduces the overall size of the encoded data.

### The process of Huffman Coding involves:

1. *Frequency Analysis*: Calculate the frequency of each character in the input data.

1. *Building a Huffman Tree*: Create a binary tree where each leaf node represents a character and its frequency. The tree is built by repeatedly merging the two nodes with the lowest frequencies until only one node remains (the root of the tree).

1. *Generating Codes*: Assign binary codes to characters by traversing the Huffman Tree. Each left edge represents `0`, and each right edge represents a `1`.

Huffman Coding is optimal for symbol-by-symbol encoding and is widely used in various applications such as file compression (e.g., ZIP files), image compression (e.g., JPEG), and multimedia codecs (e.g., MP3).

### Introduction to David A. Huffman

[David A. Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) (August 9, 1925 - October 7, 1999) was an American computer scientist and professor, known for his pioneering work in the field of information theory and data compression. Huffman was in Ohio and went on to study at the Massachussets Institute of Technology (MIT), where he completed his Ph.D. in electrical engineering.

While still a graduate student, Huffman devised the [Huffman Coding algorithm](https://en.wikipedia.org/wiki/Huffman_coding) as part of a term paper for a course on information theory taught by [Robert M. Fano](https://en.wikipedia.org/wiki/Huffman_coding). His algorithm quickly became a fundamental technique in the field of data compression due to its efficiency and simplicity.

Throughout his career, Huffman made significant contributions to various areas of computer science and engineering. He was a professor at MIT and later at the University of California, Santa Cruz, where he helped establish the Computer Science Department.

David Huffman's work has had a lasting impact on how data is efficiently stored and transmitted, and his legacy continues to influence modern computing and telecommunications.

## License
MIT