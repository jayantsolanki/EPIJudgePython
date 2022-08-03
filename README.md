# EPI Judge

## Beta 5

## Introduction

EPI Judge is meant to serve as a companion to our book Elements of Programming Interviews. Specifically, this project consists of the following:

- **Stub programs** for each problem in our book in Python, Java, and C++
- **Test-cases** that cover common corner-case and performance bugs
- A **framework** for running these tests on your implementation on your machine

## Installation

Here's how to download the judge:

    $ git clone https://github.com/adnanaziz/EPIJudge.git
If you do not have `git`, here's a good [tutorial](https://www.atlassian.com/git/tutorials/install-git) on installing git itself.

## Running the judge using IDEs

Check out these one minute videos to see how easy it is to get started with the judge.

### Python

[PyCharm](https://youtu.be/ImD_iI-uGYo), [Eclipse](https://youtu.be/rZ1qqwEXwQY), [NetBeans](https://youtu.be/Z41jW1TyZwY)

### Java

[IntelliJ IDEA](https://youtu.be/1BzHUpluQHM), [Eclipse](https://youtu.be/i9uz9Zazo0A)

### C++

[CLion](https://youtu.be/aHPDApyyYEg), [Visual Studio 2017](https://youtu.be/hgd8IIQpBEE)


## Running the judge from the command line

### Python

    $ python3 <program_name>.py

#### Java

Use the [`Makefile`](https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_java/Makefile). 

Compile and run a specific program:

    $ make <program_name> 
Example:

    $ make Anagrams
Compile and run the last program that you edited:

	$ make

### C++

You can manually compile and run all programs by directly invoking GCC and Clang. 

    $ g++ -pthread -std=c++14 -O3 -o anagrams anagrams.cc
You can also use the provided Makefile: `make <program_name>`. You can also use CMake with the provided CMakeLists.txt file. 

	$ make 
The default Makefile target is the last edited file.

    $ make anagrams


## FAQ

- How can I contact the authors? 

Please feel free to send us questions and feedback -  `adnan.aziz@gmail.com` and `tsung.hsien.lee@gmail.com`

- Help, my EPIJudge is not working, what should I do?

If you do have issues, e.g., with install or with buggy tests, feel free to reach out to us via email. Please be as detailed as you can: the ideal is if you can upload a screencast video of the issue to youtube; failing that, please upload screenshots.  The more detailed the description of the problem and your environment (OS, language version, IDE and version), the easier it’ll be for us to help you.

- I'm new to programming, and don't have any kind of development environment, what should I do?

The IntelliJ Integrated Development environments described above are best-in-class, and have free versions that will work fine for the EPI Judge. They do not include the compilers. You can get the Java development environment from [Oracle](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html), and the Python development environment from [Python.org](https://www.python.org/downloads/). For C++, you have multiple options. The simplest is to install [VisualStudio](https://code.visualstudio.com/download), which includes both the IDE and the compiler. Google is a good resource for installation help.

- What compilers are supported for judge?
  - C++
    - Linux
      - **GCC** 5.4.1 and newer
      - **Clang** 4.0 and newer
    - OS X  
      - **Apple LLVM Clang** 9.0.0 and newer
    - Windows
      - **Visual Studio** 2017 and newer
      - **MinGW** GCC 5.4.0 and newer
      - **LXSS** (Windows Subsystem for Linux) GCC 5.4.0 and newer
  - Java     
    - **Java** 9 and newer
  - Python
    - **Python** 3.7 and newer
   

- What compilers are supported for solutions?
  - C++
      - Linux
        - **GCC** 7.0.0 and newer
        - **Clang** 5.0 and newer
      - OS X  
        - **Apple LLVM Clang** 9.0.0 and newer
      - Windows
      - **Visual Studio** 2017 and newer
        - **MinGW** GCC 7.2.0 and newer
        - **LXSS** (Windows Subsystem for Linux) GCC 7.2.0 and newer
    - Java     
      - **Java** 9 and newer
    - Python
      - **Python** 3.6 and newer 

Let us know if you managed to compile with an older version.

- What does the UI look like?

Take a look at this screenshot.

<img src="http://elementsofprogramminginterviews.com/img/judge-ide-example.png" width="600px"></img>

- How can I understand the test framework better?

The judge harness is fairly complex (but does not use nonstandard language features or libraries). You are welcome to study it, but we’d advise you against making changes to it (since it will lead to nasty merge conflicts when you update).

- How do I import the C++ project?

If you want to import the project into your favourite IDE, you probably need to create IDE project with [CMake](https://cmake.org/) (no need to do it for CLion, it supports CMake out-of-the-box).

Here is an example recipe for generationg Visual Studio project ([list](https://cmake.org/cmake/help/v3.10/manual/cmake-generators.7.html) of all CMake supported IDEs).
After installing CMake, open your terminal, go to `epi_judge_cpp` folder and run following commands:

    mkdir vs
    cd vs
    cmake -G "Visual Studio 15 2017" ..

Then just open `epi_judge_cpp/vs/epi_judge_cpp.sln` solution with Visual Studio and it will load all EPI programs.

## Tracking your progress

The file [index.html](https://github.com/adnanaziz/EPIJudge/blob/master/index.html) in the root of this project tracks your progress through the problems. Specifically, there's an expanding tab for each chapter. Click on it, and you will see your progress, e.g., as below. This file gets updated each time you execute a program. You can **use this file to map book problems to stub programs**.

<img src="https://i.imgur.com/xjf7Z32.png" width="600px"></img>

## Acknowledgments

A big shout-out to the hundreds of users who tried out the release over the past couple of months. As always, we never fail to be impressed by the enthusiasm and commitment our readers have; it has served to bring out the best in us.
We all thank [Viacheslav Kroilov](https://github.com/metopa), for applying his exceptional software engineering skills to make EPI Judge a reality.

Mappings for:
* Java edition &copy; 2019
* Python edition &copy; 2019
* C++ edition &copy; 2018

# Study guides for shortened time frames

<table>
  <thead>
    <tr>
      <th colspan="2">3 days</th>
      <th>7 days</th>
      <th>1 month</th>
      <th>4 months</th>
    </tr>
  </thead>
  <tbody>
    <tr>
	    <td>C0</td>
	    <td>C1</td>
	    <td>C2</td>
	    <td>C3</td>
	    <td>C4</td>
    </tr>
        <tr>
    <td><a href="">4.1</a></td>
    <td><a href="https://leetcode.com/problems/powx-n/">4.7</a></td>
    <td><a href="">4.8</a></td>
    <td><a href="https://leetcode.com/problems/reverse-bits/">4.3</a>, <a href="https://leetcode.com/problems/rectangle-overlap/">4.11</a></td>
    <td><a href="https://leetcode.com/problems/palindrome-number/">4.9</a></td>
    </tr>
    <tr>
    <td><a href="https://leetcode.com/problems/sort-colors/">5.1</a>, <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">5.6</a></td>
    <td><a href="">5.12</a>, <a href="">5.18</a></td>
    <td><a href="https://leetcode.com/problems/plus-one/">5.2</a>, <a href="https://leetcode.com/problems/valid-sudoku/">5.17</a></td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/">5.5</a>, <a href="https://leetcode.com/problems/count-primes">5.9</a></td>
    <td><a href="">5.3</a>, <a href="">5.10</a>, <a href="">5.15</a></td>
    </tr>
        <tr>
    <td><a href="https://leetcode.com/problems/string-to-integer-atoi/">6.1</a></td>
    <td><a href="">6.2</a>, <a href="">6.4</a></td>
    <td><a href="https://leetcode.com/problems/valid-palindrome/">6.5</a>, <a href="https://leetcode.com/problems/reverse-words-in-a-string-ii">6.6</a></td>
    <td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/">6.7</a>, <a href="https://leetcode.com/problems/count-and-say/">6.8</a></td>
    <td><a href="https://leetcode.com/problems/roman-to-integer">6.9</a>, <a href="">6.11</a></td>
    </tr>
     <tr>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists">7.1</a></td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list">7.2</a>, <a href="https://leetcode.com/problems/linked-list-cycle-ii/">7.3</a></td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-linked-lists/">7.4</a>, <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">7.7</a></td>
    <td><a href="https://leetcode.com/problems/odd-even-linked-list/">7.10</a></td>
    <td> <a href="https://leetcode.com/problems/palindrome-linked-list/">7.11</a></td>
    </tr>
    <tr>
    <td><a href="https://leetcode.com/problems/min-stack/">8.1</a></td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/">8.6</a></td>
    <td><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/">8.2</a>, <a href="https://leetcode.com/problems/design-circular-queue/">8.7</a></td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/">8.3</a>, <a href="https://leetcode.com/problems/implement-queue-using-stacks/">8.8</a></td>
    <td><a href="https://leetcode.com/problems/simplify-path/">8.4</a></td>
    </tr>
            <tr>
    <td><a href="https://leetcode.com/problems/balanced-binary-tree/">9.1</a></td>
    <td><a href="">9.4</a></td>
    <td><a href="https://leetcode.com/problems/symmetric-tree/">9.2</a>, <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/">9.12</a></td>
    <td><a href="https://leetcode.com/problems/binary-tree-inorder-traversal/">9.11</a></td>
    <td><a href="https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/">9.13</a>, <a href="">9.16</a></td>
    </tr>
            <tr>
    <td><a href="">10.1</a></td>
    <td><a href="https://leetcode.com/problems/k-closest-points-to-origin/">10.4</a></td>
    <td><a href="">10.3</a></td>
    <td><a href="https://leetcode.com/problems/find-median-from-data-stream/">10.5</a></td>
    <td><a href="">10.6</a></td>
    </tr>
            <tr>
    <td><a href="">11.1</a></td>
    <td><a href="https://leetcode.com/problems/sqrtx/">11.4</a>, <a href="https://leetcode.com/problems/kth-largest-element-in-an-array">11.8</a></td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array">11.3</a>, <a href="">11.9</a></td>
    <td><a href="">11.5</a>, <a href="">11.10</a></td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix-ii/">11.6</a>, <a href="">11.7</a></td>
    </tr>
            <tr>
    <td><a href="https://leetcode.com/problems/group-anagrams/">12.0</a></td>
    <td><a href="https://leetcode.com/problems/ransom-note/">12.2</a></td>
    <td><a href="">12.3</a>, <a href="">12.5</a></td>
    <td><a href="https://leetcode.com/problems/palindrome-permutation">12.1</a>, <a href="">12.5</a></td>
    <td><a href="">12.4</a>, <a href="https://leetcode.com/problems/minimum-window-substring">12.6</a></td>
    <td><a href="">12.9</a></td>
    </tr>
            <tr>
    <td><a href="">13.1</a></td>
    <td><a href="https://leetcode.com/problems/merge-sorted-array">13.2</a></td>
    <td><a href="">13.6</a></td>
    <td><a href="">13.8</a>, <a href="">13.11</a></td>
    <td><a href="">13.9</a></td>
    </tr>
            <tr>
    <td><a href="https://leetcode.com/problems/validate-binary-search-tree">14.1</a></td>
    <td><a href="https://leetcode.com/problems/inorder-successor-in-bst">14.2</a>, <a href="">14.3</a></td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">14.4</a></td>
    <td><a href="">14.5</a>, <a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree">14.8</a></td>
    <td><a href="">14.7</a></td>
    </tr>
            <tr>
    <td><a href="">15.1</a></td>
    <td><a href="https://leetcode.com/problems/n-queens/">15.3</a></td>
    <td><a href="https://leetcode.com/problems/permutations/">15.4</a></td>
    <td><a href="https://leetcode.com/problems/subsets/">15.5</a>, <a href="https://leetcode.com/problems/sudoku-solver">15.10</a></td>
    <td><a href="">15.7</a>, <a href="https://leetcode.com/problems/gray-code/">15.11</a></td>
    </tr>
    <tr>
    <td><a href="">16.1</a></td>
    <td><a href="https://leetcode.com/problems/edit-distance/">16.2</a></td>
    <td><a href="https://leetcode.com/problems/unique-paths/">16.3</a>, <a href="">16.6</a></td>
    <td><a href="">16.5</a>, <a href="https://leetcode.com/problems/word-break-ii/">16.7</a></td>
    <td><a href="https://leetcode.com/problems/longest-increasing-subsequence/">16.12</a></td>
    </tr>
    <tr>
    <td><a href="https://leetcode.com/problems/3sum">17.4</a></td>
    <td><a href="https://leetcode.com/problems/gas-station/">17.6</a></td>
    <td><a href="https://leetcode.com/problems/majority-element/">17.5</a></td>
    <td><a href="https://leetcode.com/problems/container-with-most-water/">17.7</a></td>
    <td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/">17.8</a></td>
    </tr>
     <tr>
    <td><a href="https://leetcode.com/problems/the-maze-ii">18.1</a></td>
    <td><a href="">18.7</a></td>
    <td><a href="https://leetcode.com/problems/flood-fill/">18.2</a></td>
    <td><a href="https://leetcode.com/problems/number-of-enclaves/">18.3</a></td>
    <td><a href="">18.5</a></td>
    </tr>
     <tr>
    <td><a href="">19.3</a></td>
    <td><a href="">19.6</a></td>
    <td><a href="">19.8</a></td>
    <td><a href="">19.9</a></td>
    <td><a href="">20.9</a></td>
    </tr>
     <tr>
    <td><a href="">20.13</a></td>
    <td><a href="">20.15</a></td>
    <td><a href="">20.16</a></td>
    <td><a href="">20.1</a></td>
    <td><a href="">20.2</a></td>
    </tr>
  </tbody>
</table>

# Primitive Types

| Problem | LeetCode |
|---------|----------|
| 4.1       | []() |
| 4.2 | []() |
| 4.3 | [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) |
| 4.4 | []() |
| 4.5 | []() |
| 4.6 | []() |
| 4.7 | [50. Pow(x,n)](https://leetcode.com/problems/powx-n/) |
| 4.8 | []() |
| 4.9 | [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) |
| 4.10 | [470. Implement Rand10() using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) note: book is implement Rand6() with Rand2() |
| 4.11 | [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) note: book asks to determine overlapping area where it exists |

# Arrays

| Problem | LeetCode |
|---------|----------|
| 5.1       | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) |
| 5.2       | [66. Plus One](https://leetcode.com/problems/plus-one/) |
| 5.3       | []() |
| 5.4       | [55. Jump Game](https://leetcode.com/problems/jump-game/) |
| 5.5       | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |
| 5.6       | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 5.7 | [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |
| 5.8 | [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort) |
| 5.9 | [204. Count Primes](https://leetcode.com/problems/count-primes) note: book asks to return a list of the primes |
| 5.10 | []() |
| 5.11 | [31. Next Permutation](https://leetcode.com/problems/next-permutation/) |
| 5.12 | []() |
| 5.13 | []() |
| 5.14 | [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) |
| 5.15 | []() |
| 5.16 | []() |
| 5.17 | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) |
| 5.18 | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) |
| 5.19 | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) |
| 5.20 | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) |

# Strings

| Problem | LeetCode |
|---------|----------|
| 6.1       | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) note: book asks for Integer to String (itoa) as well |
| 6.2 | []() |
| 6.3 | [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) |
| 6.4 | []() |
| 6.5 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |
| 6.6 | [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii) |
| 6.7 | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 6.8 | [38. Count and Say](https://leetcode.com/problems/count-and-say/) |
| 6.9 | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer) |
| 6.10 | [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) |
| 6.11 | []() |
| 6.12 | [443. String Compression](https://leetcode.com/problems/string-compression/) |
| 6.13 | [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/) |

# Linked Lists

| Problem | LeetCode |
|---------|----------|
| 7.1       | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) |
| 7.2 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) |
| 7.3 | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) |
| 7.4 | [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) |
| 7.5 | []() |
| 7.6 | [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) |
| 7.7 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) |
| 7.8 | [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) |
| 7.9 | [61. Rotate List](https://leetcode.com/problems/rotate-list/) |
| 7.10 | [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) note: odd first instead of even |
| 7.11 | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) |
| 7.12 | [86. Partition List](https://leetcode.com/problems/partition-list/) |
| 7.13 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |

# Stacks and Queues

| Problem | LeetCode |
|---------|----------|
| 8.1       | [155. Min Stack](https://leetcode.com/problems/min-stack/) note: min instead of max |
| 8.2 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |
| 8.3 | [20. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/) |
| 8.4 | [71. Simplify Path](https://leetcode.com/problems/simplify-path/) |
| 8.5 | []() |
| 8.6 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| 8.7 | [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) |
| 8.8 | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) |
| 8.9 | []() |

# Binary Trees
| Problem | LeetCode |
|---------|----------|
| 9.1       | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) |
| 9.2 | [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) |
| 9.3 | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 9.4 | []() |
| 9.5 | [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) |
| 9.6 | [112. Path Sum](https://leetcode.com/problems/path-sum/) |
| 9.7 | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) note: solve without recursion |
| 9.8 | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) note: solve without recursion |
| 9.9 | []() |
| 9.10 | []() |
| 9.11 | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) note: solve with constant space |
| 9.12 | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 9.13 | [1028. Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) |
| 9.14 | []() |
| 9.15 | [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree) |
| 9.16 | []() |

# Heaps

| Problem | LeetCode |
|---------|----------|
| 10.1       | []() |
| 10.2 | []() |
| 10.3 | []() |
| 10.4 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) |
| 10.5 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |
| 10.6 | []() |

# Searching

| Problem | LeetCode |
|---------|----------|
| 11.1       | []() |
| 11.2 | []() |
| 11.3 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) |
| 11.4 | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) |
| 11.5 | []() |
| 11.6 | [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) |
| 11.7 | []() |
| 11.8 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array) |
| 11.9 | []() |
| 11.10 | []() |

# Hash Tables

| Problem | LeetCode |
|---------|----------|
| 12.0       | [49. Anagrams](https://leetcode.com/problems/group-anagrams/) |
| 12.1       | [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation) |
| 12.2 | [383. Ransom Note](https://leetcode.com/problems/ransom-note/) |
| 12.3 | []() |
| 12.4 | []() |
| 12.5 | []() |
| 12.6 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) note: strings instead of arrays |
| 12.7 | [727. Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence) note: strings instead of arrays |
| 12.8 | []() |
| 12.9 | []() |
| 12.10 | []() |
| 12.11 | []() |
| 12.12 | []() |

# Sorting

| Problem | LeetCode |
|---------|----------|
| 13.1    | []() |
| 13.2 | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array) |
| 13.3 | [274. H-Index](https://leetcode.com/problems/h-index/) |
| 13.4 | []() |
| 13.5 | []() |
| 13.6 | []() |
| 13.7 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) |
| 13.8 | []() |
| 13.9 | []() |
| 13.10 | []() |
| 13.11 | [148. Sort List](https://leetcode.com/problems/sort-list/) |
| 13.12 | []() |

# Binary Search Trees

| Problem | LeetCode |
|---------|----------|
| 14.1       | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree) |
| 14.2 | [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst) |
| 14.3 | []() |
| 14.4 | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| 14.5 | []() |
| 14.6 | []() |
| 14.7 | []() |
| 14.8 | [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) |
| 14.9 | []() |
| 14.10 | []() |
| 14.11 | []() |

# Recursion

| Problem | LeetCode |
|---------|----------|
| 15.1 | []() |
| 15.2 | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 15.3 | [51. N-Queens](https://leetcode.com/problems/n-queens/) |
| 15.4 | [46. Permutations](https://leetcode.com/problems/permutations/) |
| 15.5 | [78. Subsets](https://leetcode.com/problems/subsets/) |
| 15.6 | [77. Combinations](https://leetcode.com/problems/combinations/) |
| 15.7 | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses) |
| 15.8 | [131. Palindrome Partioning](https://leetcode.com/problems/palindrome-partitioning/) |
| 15.9 | []() |
| 15.10 | [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver) |
| 15.11 | [89. Gray Code](https://leetcode.com/problems/gray-code/) |

# Dynamic Programming

| Problem | LeetCode |
|---------|----------|
| 16.1       | [518. Coin Change 2](https://leetcode.com/problems/coin-change-2) |
| 16.2 | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) |
| 16.3 | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) |
| 16.4 | []() |
| 16.5 | []() |
| 16.6 | []() |
| 16.7 | [140. Word Break II](https://leetcode.com/problems/word-break-ii/) |
| 16.8 | [120. Triangle](https://leetcode.com/problems/triangle/) |
| 16.9 | [877. Stone Game](https://leetcode.com/problems/stone-game/) |
| 16.10 | [70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |
| 16.11 | []() |
| 16.12 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) |

# Greedy Algorithms and Invariants

| Problem | LeetCode |
|---------|----------|
| 17.1       | []() |
| 17.2 | []() |
| 17.3 | [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) |
| 17.4 | [15. 3Sum](https://leetcode.com/problems/3sum) |
| 17.5 | [169. Majority Element](https://leetcode.com/problems/majority-element/) |
| 17.6 | [134. Gas Station](https://leetcode.com/problems/gas-station/) |
| 17.7 | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| 17.8 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

# Graphs

| Problem | LeetCode |
|---------|----------|
| 18.1       | [505. The Maze II](https://leetcode.com/problems/the-maze-ii) note: shortest path instead of any path |
| 18.2 | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) |
| 18.3 | [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) |
| 18.4 | []() |
| 18.5 | []() |
| 18.6 | []() |
| 18.7 | []() |
| 18.8 | []() |

