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

Huffman Coding is optimal for symbol-by-symbol encoding and is widely used in various applications such as file compression (e.g., [ZIP](https://en.wikipedia.org/wiki/ZIP_(file_format)) files), image compression (e.g., [JPEG](https://en.wikipedia.org/wiki/JPEG)), and multimedia codecs (e.g., [MP3](https://en.wikipedia.org/wiki/MP3)).

### Introduction to David A. Huffman

[David A. Huffman](https://en.wikipedia.org/wiki/David_A._Huffman) (August 9, 1925 - October 7, 1999) was an American computer scientist and professor, known for his pioneering work in the field of information theory and data compression. Huffman was in Ohio and went on to study at the Massachussets Institute of Technology (MIT), where he completed his Ph.D. in electrical engineering.

While still a graduate student, Huffman devised the [Huffman Coding algorithm](https://en.wikipedia.org/wiki/Huffman_coding) as part of a term paper for a course on information theory taught by [Robert M. Fano](https://en.wikipedia.org/wiki/Huffman_coding). His algorithm quickly became a fundamental technique in the field of data compression due to its efficiency and simplicity.

Throughout his career, Huffman made significant contributions to various areas of computer science and engineering. He was a professor at MIT and later at the University of California, Santa Cruz, where he helped establish the Computer Science Department.

David Huffman's work has had a lasting impact on how data is efficiently stored and transmitted, and his legacy continues to influence modern computing and telecommunications.

## Methodology

### **Step 1: Frequency Table of English Letters**

First, we need a frequency table for the English letters. Here's a commonly used table based on large corpora of English texts:

<table>

<thead>
<td>Letter</td>
<td>Frequency (%)</td>
</thead>

<tr>
<td>A</td><td>8.167</td>
</tr>

<tr>
<td>B</td><td>1.492</td>
</tr>

<tr>
<td>C</td><td>2.782</td>
</tr>

<tr>
<td>D</td><td>4.253</td>
</tr>

<tr>
<td>E</td><td>12.702</td>
</tr>

<tr>
<td>F</td><td>2.228</td>
</tr>

<tr>
<td>G</td><td>2.015</td>
</tr>

<tr>
<td>H</td><td>6.094</td>
</tr>

<tr> 
<td>I</td><td>6.966</td>
</tr>

<tr>
<td>J</td><td>0.153</td>
</tr>

<tr>
<td>K</td><td>0.772</td>
</tr>

<tr>
<td>L</td><td>4.025</td>
</tr>

<tr>
<td>M</td><td>2.406</td>
</tr>

<tr>
<td>N</td><td>6.749</td>
</tr>

<tr>
<td>O</td><td>7.507</td>
</tr>

<tr>
<td>P</td><td>1.929</td>
</tr>

<!-- Remaining rows -->

<tr> 
<td>Q</td><td>0.095</td>
</tr>

<tr>
<td>R</td><td>5.987</td>
</tr>

<tr>
<td>S</td><td>6.327</td>
</tr>

<tr>
<td>T</td><td>9.056</td>
</tr>

<tr>
<td>U</td><td>2.758</td>
</tr>

<tr>
<td>V</td><td>0.978</td>
</tr>

<tr>
<td>W</td><td>2.36</td>
</tr>

<tr>
<td>X</td><td>0.15</td>
</tr>

<tr>
<td>Y</td><td>1.974</td>
</tr>

<tr>
<td>Z</td><td>0.074</td>
</tr>

<tr>
<td>SPACE</td><td>18.29</td>
</tr>

</table>

## License
MIT