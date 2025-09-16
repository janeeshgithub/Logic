
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