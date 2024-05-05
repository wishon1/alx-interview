# Curriculum: Short Specializations

## 0x01. Lockboxes

### Overview

This short specialization focuses on the topic of Lockboxes. The main project within this specialization involves developing a solution to determine if all the lockboxes provided can be opened. The project provides a hands-on opportunity to apply concepts from algorithms, Python programming, and data structures.

### Average Score: 100.08%

### Must Know

For this project, a solid understanding of several key concepts is necessary to develop an efficient solution. Here’s a list of concepts and resources that will be instrumental:

#### Concepts Needed:
1. **Lists and List Manipulation:** Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
   - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

2. **Graph Theory Basics:** Knowledge of graph theory concepts, especially traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be helpful.
   - [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms)

3. **Algorithmic Complexity:** Understanding the time and space complexity of the solution is crucial for writing efficient algorithms.
   - [Big O Notation](https://www.geeksforgeeks.org/time-complexities-of-searching-algorithms/)

4. **Recursion:** Some solutions might require a recursive approach to traverse through the lockboxes and keys.
   - [Recursion in Python](https://realpython.com/python-recursion/)

5. **Queue and Stack:** Knowledge of using queues and stacks is essential for implementing BFS or DFS algorithms.
   - [Python Queue and Stack](https://www.geeksforgeeks.org/queue-in-python/)

6. **Set Operations:** Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
   - [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

#### Project Description

**0. Lockboxes:**
- **Description:** You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened.
- **Prototype:** `def canUnlockAll(boxes)`
- **Details:**
  - `boxes` is a list of lists.
  - A key with the same number as a box opens that box.
  - You can assume all keys will be positive integers.
  - There can be keys that do not have boxes.
  - The first box `boxes[0]` is unlocked.
- **Return Value:** Return `True` if all boxes can be opened, else return `False`.

### Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)

### Requirements

#### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
