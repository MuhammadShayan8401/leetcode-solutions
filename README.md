# 🧠 LeetCode Solutions

![Profile Views](https://komarev.com/ghpvc/?username=MuhammadShayan8401&style=for-the-badge)

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![LeetCode](https://img.shields.io/badge/LeetCode-Practice-orange?style=for-the-badge&logo=leetcode)
![GitHub](https://img.shields.io/badge/GitHub-Active-black?style=for-the-badge&logo=github)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)

---

## 👨‍💻 Author

**Muhammad Shayan Ahmed**
🎓 Bachelor of Software Engineering
🏫 Sir Syed University of Engineering & Technology (SSUET)

---

## 📌 About This Repository

This repository contains my solutions to various **LeetCode problems**, focused on improving my **Data Structures and Algorithms (DSA)** skills.

It serves as a personal coding journal where I regularly practice problems to strengthen my logical thinking and prepare for technical interviews.

---

## 🚀 What You'll Find Here

* Clean and optimized solutions in **Python**
* Focus on **efficient algorithms**
* Practice across multiple DSA topics
* Continuous updates as I solve more problems

---

## 📂 Topics Covered

* Arrays
* Strings
* Hashing
* Linked Lists
* Stacks & Queues
* Trees & Graphs
* Recursion & Backtracking
* Dynamic Programming

---

## 💡 Example Problem

### 🔹 Mirror Pair Minimum Distance

**Problem:**
Find the minimum distance between indices `(i, j)` such that:

* `i < j`
* `reverse(nums[i]) == nums[j]`

---

### ⚡ Solution (Python)

```python
class Solution:
    def minMirrorPairDistance(self, nums):
        index_map = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])

            if num in index_map:
                min_dist = min(min_dist, i - index_map[num])

            index_map[rev] = i

        return min_dist if min_dist != float('inf') else -1
```

---

## ⏱️ Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 📈 Progress

* Problems Solved: **(update as you go e.g. 10+)**
* Active Practice: ✅
* Goal: **100+ LeetCode Problems**

---

## 🎯 Purpose

* Improve problem-solving skills
* Prepare for internships & placements
* Build a strong coding portfolio

---

## 🔗 Connect With Me

* GitHub: https://github.com/MuhammadShayan8401
* LinkedIn: https://www.linkedin.com/in/muhammad-shayan-ahmed-05b847281/

---

⭐ *Feel free to explore, fork, and star the repository!*

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [1886-determine-whether-matrix-can-be-obtained-by-rotation](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/1886-determine-whether-matrix-can-be-obtained-by-rotation/) | Easy |
| [2154-keep-multiplying-found-values-by-two](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2154-keep-multiplying-found-values-by-two/) | Easy |
| [2751-robot-collisions](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2751-robot-collisions/) | Hard |
| [3418-maximum-amount-of-money-robot-can-earn](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3418-maximum-amount-of-money-robot-can-earn/) | Medium |
| [3761-minimum-absolute-distance-between-mirror-pairs](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3761-minimum-absolute-distance-between-mirror-pairs/) | Medium |
## Dynamic Programming
| Problem Name | Difficulty |
| ------- | ------- |
| [3418-maximum-amount-of-money-robot-can-earn](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3418-maximum-amount-of-money-robot-can-earn/) | Medium |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [1886-determine-whether-matrix-can-be-obtained-by-rotation](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/1886-determine-whether-matrix-can-be-obtained-by-rotation/) | Easy |
| [3418-maximum-amount-of-money-robot-can-earn](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3418-maximum-amount-of-money-robot-can-earn/) | Medium |
## Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [2751-robot-collisions](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2751-robot-collisions/) | Hard |
## Sorting
| Problem Name | Difficulty |
| ------- | ------- |
| [2154-keep-multiplying-found-values-by-two](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2154-keep-multiplying-found-values-by-two/) | Easy |
| [2751-robot-collisions](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2751-robot-collisions/) | Hard |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [2154-keep-multiplying-found-values-by-two](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2154-keep-multiplying-found-values-by-two/) | Easy |
| [2751-robot-collisions](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2751-robot-collisions/) | Hard |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [2154-keep-multiplying-found-values-by-two](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/2154-keep-multiplying-found-values-by-two/) | Easy |
| [3761-minimum-absolute-distance-between-mirror-pairs](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3761-minimum-absolute-distance-between-mirror-pairs/) | Medium |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [3761-minimum-absolute-distance-between-mirror-pairs](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/3761-minimum-absolute-distance-between-mirror-pairs/) | Medium |
## Database
| Problem Name | Difficulty |
| ------- | ------- |
| [0175-combine-two-tables](https://github.com/MuhammadShayan8401/leetcode-solutions/tree/main/0175-combine-two-tables/) | Easy |
<!---LeetCode Topics End-->