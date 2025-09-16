# 60 MAANG DSA Questions

---

**1. Two Sum**  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

**2. Maximum Subarray**  
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**3. Sort Colors**  
Given an array `nums` with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

**4. Container With Most Water**  
You are given an integer array `height` of length n, where there are n vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container that contains the most water. Return the maximum amount of water a container can store.

**5. Best Time to Buy and Sell Stock**  
You are given an array of `prices` where `prices[i]` is the price of a given stock on an `i`th day. Maximize your profit by choosing a single day to buy one stock and a different day in the future to sell it. Return the maximum profit, or 0 if no profit can be achieved.

**6. 4Sum**  
Given an array `nums` of n integers, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that they are distinct, and their sum equals a given `target`.

**7. Reverse String**  
Write a function that reverses a string given as an array of characters. You must modify the input array in-place with O(1) extra memory.

**8. Sort Characters By Frequency**  
Given a string `s`, sort it in decreasing order based on the frequency of its characters. The frequency is the number of times a character appears in the string. Return the sorted string.

**9. Permutation in String**  
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise. In other words, check if one of `s1`'s permutations is a substring of `s2`.

**10. Palindrome Partitioning**  
Given a string `s`, partition it such that every substring of the partition is a palindrome. Return all possible palindrome partitions of `s`.

**11. Longest Repeating Character Replacement**  
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character, at most `k` times.

**12. Valid Palindrome**  
A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forwards and backward. Given a string `s`, return true if it is a palindrome, or false otherwise.

**13. Remove Linked List Elements**  
Given the head of a linked list and an integer `val`, remove all nodes of the linked list that have `Node.val == val`, and return the new head.

**14. Reverse Linked List**  
Given the head of a singly linked list, reverse the list, and return the reversed list.

**15. Subsets**  
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution must not contain duplicate subsets.

**16. Generate Parentheses**  
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**17. LRU Cache**  
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

**18. First Missing Positive**  
Given an unsorted integer array `nums`, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses constant extra space.

**19. Spiral Matrix**  
Given an `m x n` matrix, return all elements of the matrix in spiral order.

**20. Valid Sudoku**  
Determine if a 9x9 Sudoku board is valid. Validation is required for filled cells based on the rule that each row, column, and nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

**21. Word Search**  
Given an `m x n` grid of characters `board` and a string `word`, return true if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically), and the same letter cell may not be used more than once.

**22. Surrounded Regions**  
Given an `m x n` matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.

**23. Flatten Binary Tree to Linked List**  
Given the root of a binary tree, flatten the tree into a "linked list" where the right child pointer points to the next node and the left child pointer is always null. The list should be in the same order as a pre-order traversal of the tree.

**24. Multiply Two Linked Lists**  
Given two linked lists, L1 and L2, multiply the numbers represented by these two linked lists.

**25. Reverse Nodes in k-Group**  
Given the head of a linked list, reverse the nodes of the list `k` at a time and return the modified list. `k` is a positive integer less than or equal to the list's length. If the number of nodes is not a multiple of `k`, the final left-out nodes should remain as they are. Only the nodes themselves may be changed, not their values.

**26. Merge Two Sorted Lists**  
You are given the heads of two sorted linked lists, `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**27. Reorder List**  
You are given the head of a singly linked-list: `L0 → L1 → … → Ln-1 → Ln`. Reorder the list to be: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`. You may not modify the values in the nodes; only the nodes themselves can be changed.

**28. Swap Nodes in Pairs**  
Given a linked list, swap every two adjacent nodes and return its head. This must be solved without modifying the values in the list's nodes.

**29. Missing Number**  
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**30. Counting Bits**  
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= `i` <= `n`), `ans[i]` is the number of 1's in the binary representation of `i`.

**31. Largest Rectangle in Histogram**  
Given an array of integers `heights` representing a histogram's bar height where each bar has a width of 1, return the area of the largest rectangle in the histogram.

**32. Swap Nodes in Pairs (Again)**  
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.

**33. Implement Stack using Queues**  
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

**34. BST Iterator**  
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST).

**35. Trapping Rain Water**  
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**36. Daily Temperatures**  
Given an array of `temperatures`, return an array `answer` where `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If no such future day exists, `answer[i]` should be 0.

**37. Sliding Window Maximum**  
You are given an array of integers `nums` and a sliding window of size `k` moving from left to right. You can only see the `k` numbers in the window. Return the max sliding window.

**38. Min Stack**  
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

**39. Balanced Binary Tree**  
Given a binary tree, determine if it is height-balanced.

**40. Lowest Common Ancestor of a Binary Tree**  
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

**41. Kth Smallest Element in a BST**  
Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

**42. Binary Tree Level Order Traversal**  
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

**43. Sum Root to Leaf Numbers**  
You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number. Return the total sum of all root-to-leaf numbers.

**44. Binary Tree Maximum Path Sum**  
A path in a binary tree is a sequence of nodes where adjacent nodes have an edge connecting them, and a node can only appear once. The path does not need to pass through the root. The path sum is the sum of the node's values in the path.

**45. Implement Trie (Prefix Tree)**  
Implement a Trie (prefix tree), a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

**46. Group Anagrams**  
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**47. Merge k Sorted Lists**  
You are given an array of `k` linked-lists, where each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

**48. Find Median from Data Stream**  
The median is the middle value in an ordered integer list. If the size is even, the median is the mean of the two middle values. Implement the `MedianFinder` class.

**49. 01 Matrix**  
Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell. The distance between two adjacent cells is 1.

**50. Flood Fill**  
An image is represented by an `m x n` integer grid. You are given three integers `sr`, `sc`, and `color`. Perform a flood fill on the image starting from the pixel `image[sr][sc]`.

**51. Number of Islands**  
Given an `m x n` 2D binary grid of '1's (land) and '0's (water), return the number of islands. An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.

**52. Clone Graph**  
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

**53. Longest Increasing Path in a Matrix**  
Given an `m x n` integer matrix, return the length of the longest increasing path in the matrix. You can move in four directions (left, right, up, down) but not diagonally or outside the boundary.

**54. Network Delay Time**  
You are given a network of `n` nodes and a list of travel times as directed edges `(ui, vi, wi)`. If a signal is sent from a given node `k`, return the minimum time it takes for all `n` nodes to receive the signal. If it's impossible, return -1.

**55. Maximum Product Subarray**  
Given an integer array `nums`, find a subarray that has the largest product, and return the product.

**56. Partition Equal Subset Sum**  
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or `false` otherwise.

**57. Unique Paths**  
A robot on an `m x n` grid starts at the top-left corner and tries to move to the bottom-right corner. The robot can only move down or right. Given `m` and `n`, return the number of possible unique paths.

**58. Edit Distance**  
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. The permitted operations are: insert, delete, or replace a character.

**59. Coin Change**  
You are given an array of `coins` of different denominations and an `amount`. Return the fewest number of coins needed to make up that amount. If the amount cannot be made, return -1. Assume an infinite number of each kind of coin.

**60. Partition Equal Subset Sum (Again)**  
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or `false` otherwise.

---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# i want in copiable readme for github

Below is a ready-to-copy **README.md** section. This format is fully compatible with GitHub markdown: just select all, copy, and paste into your repo’s `README.md`. Section links, lists, and headings render natively, and you get automatic code copy buttons for code blocks on GitHub (no extra work needed).[^2][^3][^6]

---

# 20 Essential Coding Patterns for Technical Interviews

Master these **coding patterns** to efficiently solve and recognize major problem types in MAANG and top tech company interviews.

---

## Patterns Overview

### 1. Sliding Window

Efficiently handle subarrays/substrings of fixed or varying length.

- **Data Structures:** Array, String, HashTable
- **Sample Problems:**
  - Longest Substring with 'K' Distinct Characters
  - Fruits into Baskets

### 2. Islands (Matrix Traversal)

Efficiently explore and count components in 2D matrices.

- **Data Structures:** Matrix, Queue
- **Sample Problems:**
  - Number of Islands
  - Flood Fill
  - Cycle in a Matrix

### 3. Two Pointers

Coordinate two iterators, often in different directions or rates.

- **Data Structures:** Array, String, LinkedList
- **Sample Problems:**
  - Squaring a Sorted Array
  - Dutch National Flag Problem
  - Minimum Window Sort

### 4. Fast \& Slow Pointers

Detect cycles or midpoints with two pointers at different speeds.

- **Data Structures:** Array, String, LinkedList
- **Sample Problems:**
  - Middle of the LinkedList
  - Happy Number
  - Cycle in a Circular Array

### 5. Merge Intervals

Process and merge overlapping intervals or ranges efficiently.

- **Data Structures:** Array, Heap
- **Sample Problems:**
  - Conflicting Appointments
  - Minimum Meeting Rooms

### 6. Cyclic Sort

Sort arrays with known, consecutive ranges using index swapping.

- **Data Structures:** Array
- **Sample Problems:**
  - Find all Missing Numbers
  - Find all Duplicate Numbers
  - Find the First K Missing Positive Numbers

### 7. In-place Reversal of a LinkedList

Reverse links between nodes in-place, minimal memory.

- **Data Structures:** LinkedList
- **Sample Problems:**
  - Reverse every K-element Sub-list
  - Rotate a LinkedList

### 8. Breadth-First Search (BFS)

Traverse trees/graphs level by level.

- **Data Structures:** Tree, Graph, Matrix, Queue
- **Sample Problems:**
  - Binary Tree Level Order Traversal
  - Minimum Depth of a Binary Tree
  - Connect Level Order Siblings

### 9. Depth First Search (DFS)

Explore recursive/branching paths fully before backtracking.

- **Data Structures:** Tree, Graph, Matrix
- **Sample Problems:**
  - Path With Given Sequence
  - Count Paths for a Sum

### 10. Two Heaps

Split sets for median/tracking min/max with two heaps.

- **Data Structures:** Heap, Array
- **Sample Problems:**
  - Find the Median of a Number Stream
  - Next Interval

### 11. Subsets

Generate and manage subsets, permutations, and combinations.

- **Data Structures:** Queue, Array, String
- **Sample Problems:**
  - String Permutations by Changing Case
  - Unique Generalized Abbreviations

### 12. Modified Binary Search

Adapt binary search for not-fully-sorted or rotated data.

- **Data Structures:** Array
- **Sample Problems:**
  - Ceiling of a Number
  - Bitonic Array Maximum

### 13. Bitwise XOR

Use XOR operations for bitwise manipulation and property finding.

- **Data Structures:** Array, Bits
- **Sample Problems:**
  - Two Single Numbers
  - Flip and Invert an Image

### 14. Top 'K' Elements

Maintain top/frequent K items with heaps or other structures.

- **Data Structures:** Array, Heap, Queue
- **Sample Problems:**
  - K Closest Points to the Origin
  - Maximum Distinct Elements

### 15. K-way Merge

Merge and find elements across multiple sorted arrays.

- **Data Structures:** Array, Queue, Heap
- **Sample Problems:**
  - Kth Smallest Number in M Sorted Lists
  - Kth Smallest Number in a Sorted Matrix

### 16. Topological Sort

Linear ordering of elements with dependencies (DAGs).

- **Data Structures:** Array, HashTable, Queue, Graph
- **Sample Problems:**
  - Tasks Scheduling
  - Alien Dictionary

### 17. 0/1 Knapsack (DP)

Maximize value within constraints, each item used at most once.

- **Data Structures:** Array, HashTable
- **Sample Problems:**
  - Equal Subset Sum Partition
  - Minimum Subset Sum Difference

### 18. Fibonacci Numbers (DP)

Build solutions where each result uses earlier results (recursion+memoization).

- **Data Structures:** Array, HashTable
- **Sample Problems:**
  - Staircase
  - House Thief

### 19. Palindromic Subsequence (DP)

Find or build palindromic sequences/subsequences.

- **Data Structures:** Array, HashTable
- **Sample Problems:**
  - Longest Palindromic Subsequence
  - Minimum Deletions in a String to Make it a Palindrome

### 20. Longest Common Substring (DP)

Solve substring, subsequence, and sequence alignment problems.

- **Data Structures:** Array, HashTable
- **Sample Problems:**
  - Maximum Sum Increasing Subsequence
  - Edit Distance

---

**Tip:**
Practice each pattern with classic problems to sharpen recognition and application in real interviews.

---

_Credit: Patterns curated from DesignGurus and leading interview resources._

<span style="display:none">[^1][^4][^5][^7][^8]</span>

<div style="text-align: center">⁂</div>

[^1]: https://stackoverflow.com/questions/31908564/easy-way-to-add-copy-to-clipboard-to-github-markdown
[^2]: https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
[^3]: https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet
[^4]: https://community.atlassian.com/forums/Bitbucket-questions/How-to-copy-paste-and-preserve-the-format-from-README-md-to-the/qaq-p/1635156
[^5]: https://forum.gitea.com/t/copy-button-on-code-blocks-in-readme-md/6893
[^6]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github
[^7]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
[^8]: https://euangoddard.github.io/clipboard2markdown/

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# convert to readme

Here is a clean, copy-paste-ready README.md format for GitHub, listing all 50 essential SQL interview queries. Command descriptions and SQL code blocks are included for easy reading and copy-ability.

---

# 50 SQL Interview Queries

A curated list of 50 real-world SQL interview queries asked at companies like Amazon, Microsoft, Google, Meta, Uber, Adobe, Walmart, and PayPal.

---

## Table of Contents

- [Duplicates and Ranking](#duplicates-and-ranking)
- [Joins \& Nulls](#joins--nulls)
- [Aggregations](#aggregations)
- [Date / Time \& Windows](#date--time--windows)
- [Advanced Analytics](#advanced-analytics)

---

## Duplicates and Ranking

**1. Find duplicate records in a table (Amazon)**

```sql
SELECT column1, column2, COUNT(*)
FROM your_table
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```

**2. Retrieve the second highest salary from Employee table (Microsoft)**

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

## Joins \& Nulls

**3. Find employees without a department (Uber)**

```sql
SELECT e.*
FROM Employee e
LEFT JOIN Department d ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

**11. Find products that were never sold (Adobe)**

```sql
SELECT p.product_id
FROM Products p
LEFT JOIN Sales s ON p.product_id = s.product_id
WHERE s.product_id IS NULL;
```

## Aggregations

**4. Calculate total revenue per product**

```sql
SELECT product_id, SUM(quantity * price) AS total_revenue
FROM Sales
GROUP BY product_id;
```

**7. Show the count of orders per customer (Meta)**

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM Orders
GROUP BY customer_id;
```

**9. Calculate the average order value per customer (Microsoft)**

```sql
SELECT customer_id, AVG(total_amount) AS avg_order_value
FROM Orders
GROUP BY customer_id;
```

**10. Get the latest order placed by each customer (Uber)**

```sql
SELECT customer_id, MAX(order_date) AS latest_order_date
FROM Orders
GROUP BY customer_id;
```

**13. Get the total revenue and order count per region**

```sql
SELECT region, SUM(total_amount) AS total_revenue, COUNT(*) AS order_count
FROM Orders
GROUP BY region;
```

**14. Count customers who placed more than 5 orders (Meta)**

```sql
SELECT COUNT(*) AS customer_count
FROM (
  SELECT customer_id FROM Orders
  GROUP BY customer_id
  HAVING COUNT(*) > 5
) AS subquery;
```

**18. Get monthly sales revenue and order count (Google)**

```sql
SELECT FORMAT(date, 'yyyy-MM') AS month,
       SUM(amount) AS total_revenue,
       COUNT(order_id) AS order_count
FROM Orders
GROUP BY FORMAT(date, 'yyyy-MM');
```

**19. Rank employees by salary within each department (Amazon)**

```sql
SELECT employee_id, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rk
FROM Employee;
```

## Date / Time \& Windows

**8. Retrieve all employees who joined in 2023 (Amazon)**

```sql
SELECT *
FROM Employee
WHERE YEAR(hire_date) = 2023;
```

**16. Find all employees hired on weekends (PayPal)**

```sql
SELECT *
FROM Employee
WHERE DATENAME(WEEKDAY, hire_date) IN ('Saturday', 'Sunday');
```

**17. Employees with salary between 50,000 and 100,000 (Microsoft)**

```sql
SELECT *
FROM Employee
WHERE salary BETWEEN 50000 AND 100000;
```

**21. Find moving average of sales over last 3 days**

```sql
SELECT order_date,
       AVG(total_amount) OVER (ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM Orders;
```

**22. First and last order date for each customer**

```sql
SELECT customer_id, MIN(order_date) AS first_order, MAX(order_date) AS last_order
FROM Orders
GROUP BY customer_id;
```

**26. Calculate cumulative revenue by day**

```sql
SELECT order_date,
       SUM(total_amount) OVER (ORDER BY order_date) AS cumulative_revenue
FROM Orders;
```

**27. Top-performing departments by average salary**

```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department_id
ORDER BY avg_salary DESC;
```

## Advanced Analytics

**23. Show product sales distribution (percent of total revenue)**

```sql
WITH TotalRevenue AS (
  SELECT SUM(quantity * price) AS total FROM Sales)
SELECT s.product_id,
       SUM(s.quantity * s.price) AS revenue,
       SUM(s.quantity * s.price) * 100.0 / t.total AS revenue_pct
FROM Sales s
CROSS JOIN TotalRevenue t
GROUP BY s.product_id, t.total;
```

**24. Customers making consecutive purchases (2 days)**

```sql
WITH cte AS (
  SELECT id, order_date,
         LAG(order_date) OVER (PARTITION BY id ORDER BY order_date) AS prev_order_date
  FROM Orders
)
SELECT id, order_date, prev_order_date
FROM cte
WHERE DATEDIFF(DAY, prev_order_date, order_date) = 1;
```

**25. Find churned customers (no orders in the last 6 months)**

```sql
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING MAX(order_date) < DATEADD(MONTH, -6, GETDATE());
```

**28. Customers with orders above average per customer**

```sql
WITH customer_orders AS (
  SELECT customer_id, COUNT(*) AS order_count FROM Orders GROUP BY customer_id
)
SELECT * FROM customer_orders
WHERE order_count > (SELECT AVG(order_count) FROM customer_orders);
```

**29. Revenue from new (first-time) customers**

```sql
WITH first_orders AS (
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM Orders GROUP BY customer_id
)
SELECT SUM(o.total_amount) AS new_revenue
FROM Orders o JOIN first_orders f ON o.customer_id = f.customer_id
WHERE o.order_date = f.first_order_date;
```

**30. Percentage of employees in each department**

```sql
SELECT department_id,
       COUNT(*) AS emp_count,
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employee) AS pct
FROM Employee
GROUP BY department_id;
```

**31. Maximum salary gap within each department**

```sql
SELECT department_id, MAX(salary) - MIN(salary) AS salary_diff
FROM Employee
GROUP BY department_id;
```

**32. Products contributing to 80% of revenue (Pareto)**

```sql
WITH sales_cte AS (
  SELECT product_id, SUM(qty * price) AS revenue FROM Sales GROUP BY product_id
), total_revenue AS (
  SELECT SUM(revenue) AS total FROM sales_cte
)
SELECT s.product_id, s.revenue,
       SUM(s.revenue) OVER (ORDER BY s.revenue DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales_cte s, total_revenue t
WHERE SUM(s.revenue) OVER (ORDER BY s.revenue DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) <= t.total * 0.8;
```

**33. Average time between customer purchases**

```sql
WITH cte AS (
  SELECT customer_id, order_date,
         LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_date
  FROM Orders
)
SELECT customer_id,
       AVG(DATEDIFF(DAY, prev_date, order_date)) AS avg_gap_days
FROM cte
WHERE prev_date IS NOT NULL
GROUP BY customer_id;
```

**34. Last purchase for each customer and amount**

```sql
WITH ranked_orders AS (
  SELECT customer_id, order_id, total_amount,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
  FROM Orders
)
SELECT customer_id, order_id, total_amount
FROM ranked_orders
WHERE rn = 1;
```

**35. Year-over-year growth in revenue (Microsoft)**

```sql
SELECT FORMAT(order_date, 'yyyy') AS year,
       SUM(total_amount) AS revenue,
       SUM(total_amount) - LAG(SUM(total_amount)) OVER (ORDER BY FORMAT(order_date, 'yyyy')) AS yoy_growth
FROM Orders
GROUP BY FORMAT(order_date, 'yyyy');
```

**36. Purchases above customer 90th percentile**

```sql
WITH ranked_orders AS (
  SELECT customer_id, order_id, total_amount,
         NTILE(10) OVER (PARTITION BY customer_id ORDER BY total_amount) AS decile
  FROM Orders
)
SELECT customer_id, order_id, total_amount
FROM ranked_orders
WHERE decile = 10;
```

**37. Longest gap between orders for each customer**

```sql
WITH cte AS (
  SELECT customer_id, order_date,
         LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order_date
  FROM Orders
)
SELECT customer_id, MAX(DATEDIFF(DAY, prev_order_date, order_date)) AS max_gap
FROM cte
WHERE prev_order_date IS NOT NULL
GROUP BY customer_id;
```

**38. Customers with revenue below the 10th percentile (Google)**

```sql
WITH cte AS (
  SELECT customer_id, SUM(total_amount) AS total_revenue
  FROM Orders
  GROUP BY customer_id
)
SELECT customer_id, total_revenue
FROM cte
WHERE total_revenue < (
  SELECT PERCENTILE_CONT(0.1) WITHIN GROUP (ORDER BY total_revenue) FROM cte
);
```

**39. Market basket analysis: Products always sold together (Walmart)**

```sql
SELECT A.product_id AS product_A,
       B.product_id AS product_B,
       COUNT(*) AS count_together
FROM Order_Details A
JOIN Order_Details B
  ON A.order_id = B.order_id AND A.product_id < B.product_id
GROUP BY A.product_id, B.product_id
HAVING COUNT(*) > 10;
```

**40. Calculate income inequality (Gini coefficient, Uber)**

```sql
WITH income_cte AS (
  SELECT salary,
         SUM(salary) OVER (ORDER BY salary) AS cum_income,
         COUNT(*) OVER() AS n,
         ROW_NUMBER() OVER (ORDER BY salary) AS r
  FROM Employee
)
SELECT 1 - (2 * SUM((cum_income) / (SUM(salary) OVER ()) * (1.0 / n))) AS gini_coefficient
FROM income_cte;
```

**41. Median sales day: Revenue first exceeds 50% of total (Adobe)**

```sql
WITH cte AS (
  SELECT order_date, SUM(total_amount) AS daily_rev FROM Orders GROUP BY order_date
), cum_cte AS (
  SELECT order_date, daily_rev, SUM(daily_rev) OVER (ORDER BY order_date) AS cum_rev, SUM(daily_rev) OVER() AS total_rev FROM cte
)
SELECT TOP 1 order_date FROM cum_cte
WHERE cum_rev >= total_rev / 2
ORDER BY order_date;
```

**42. Find percentiles (25th, 50th, 75th) of salaries (Walmart)**

```sql
SELECT
  (SELECT PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) OVER () FROM Employee) AS p25,
  (SELECT PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY salary) OVER () FROM Employee) AS p50,
  (SELECT PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) OVER () FROM Employee) AS p75;
```

**43. Customers with increasing order amounts (last 3 orders)**

```sql
WITH cte AS (
  SELECT customer_id, order_date, total_amount,
         LAG(total_amount, 2) OVER (PARTITION BY customer_id ORDER BY order_date) AS amt_t_minus_2,
         LAG(total_amount, 1) OVER (PARTITION BY customer_id ORDER BY order_date) AS amt_t_minus_1
  FROM Orders
)
SELECT customer_id, order_date, total_amount
FROM cte
WHERE amt_t_minus_2 < amt_t_minus_1
  AND amt_t_minus_1 < total_amount;
```

**44. Conversion funnel between visit → signup → purchase (Microsoft)**

```sql
SELECT
  SUM(CASE WHEN stage = 'visit' THEN 1 ELSE 0 END) AS visits,
  SUM(CASE WHEN stage = 'sign_up' THEN 1 ELSE 0 END) AS sign_ups,
  SUM(CASE WHEN stage = 'purchase' THEN 1 ELSE 0 END) AS purchases
FROM Funnel;
```

**45. Top 10% of customers: Percentage of total sales (Google)**

```sql
WITH cte AS (
  SELECT customer_id, SUM(total_amount) AS revenue
  FROM Orders GROUP BY customer_id
), ranked AS (
  SELECT *, NTILE(10) OVER (ORDER BY revenue DESC) AS decile FROM cte
)
SELECT SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM cte) AS pct_top_10
FROM ranked
WHERE decile = 1;
```

**46. Weekly active users (Uber)**

```sql
SELECT DATEPART(YEAR, login_date) AS year,
       DATEPART(WEEK, login_date) AS week,
       COUNT(DISTINCT user_id) AS wau
FROM Logins
GROUP BY DATEPART(YEAR, login_date), DATEPART(WEEK, login_date);
```

**47. Employees with salary above department average (Amazon)**

```sql
WITH dept_avg AS (
  SELECT department_id, AVG(salary) AS avg_salary FROM Employee GROUP BY department_id
)
SELECT e.*
FROM Employee e
JOIN dept_avg d ON e.department_id = d.department_id
WHERE e.salary > d.avg_salary;
```

**48. Time from user signup to first purchase**

```sql
WITH first_purchase AS (
  SELECT user_id, MIN(purchase_date) AS first_purchase_date FROM Purchases GROUP BY user_id
)
SELECT u.user_id,
       DATEDIFF(DAY, u.signup_date, f.first_purchase_date) AS days_to_purchase
FROM Users u
JOIN first_purchase f ON u.user_id = f.user_id;
```

**49. Longest gap between orders for each customer**

```sql
WITH cte AS (
  SELECT customer_id, order_date,
         LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order_date
  FROM Orders
)
SELECT customer_id, MAX(DATEDIFF(DAY, prev_order_date, order_date)) AS max_gap
FROM cte
WHERE prev_order_date IS NOT NULL
GROUP BY customer_id;
```

**50. Customers with revenue below the 10th percentile**

```sql
WITH cte AS (
  SELECT customer_id, SUM(total_amount) AS total_revenue
  FROM Orders
  GROUP BY customer_id
)
SELECT customer_id, total_revenue
FROM cte
WHERE total_revenue < (
  SELECT PERCENTILE_CONT(0.1) WITHIN GROUP (ORDER BY total_revenue) FROM cte
);
```

---

> **Need more?**
> Follow for more resources and queries for interview prep.

---

<span style="display:none">[^1]</span>

<div style="text-align: center">⁂</div>

[^1]: SQL.pdf
