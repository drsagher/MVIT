# Lesson 03 Hashing, Storage and Retrieval Properties and Techniques

## Hashing
Hashing is a technique used to map large data sets to a fixed-size index, allowing for efficient storage and retrieval. A hash function takes input data and generates a unique hash code, which is used to index the data.

### Properties of Hashing
1. Deterministic: Hash functions always generate the same hash code for a given input.
2. Non-injective: Different inputs can generate the same hash code (collisions).
3. Fixed output size: Hash functions produce a fixed-size hash code, regardless of the input size.

### Techniques for Hashing
1. Division method: Uses the remainder of the input data divided by a prime number to generate the hash code.
2. Multiplication method: Uses the product of the input data and a prime number to generate the hash code.
3. Folding method: Divides the input data into smaller parts and combines them to generate the hash code.
4. Mid-square method: Uses the middle part of the squared input data to generate the hash code.

## Storage
Storage refers to the way data is organized and stored in memory or on disk. Different data structures have varying storage requirements and techniques.

### Types of Storage
1. Contiguous storage: Stores data in adjacent memory locations (e.g., arrays).
2. Linked storage: Stores data in non-adjacent memory locations, connected by pointers (e.g., linked lists).
3. Indexed storage: Stores data in a table with indexed rows and columns (e.g., databases).

## Retrieval
Retrieval refers to the process of accessing and retrieving stored data.

#### Techniques for Retrieval
1. Linear search: Searches for data by iterating through each element in the data structure.
2. Binary search: Searches for data by dividing the search space in half and searching for the target value.
3. Hashing: Uses a hash function to map the search key to a specific index in the data structure.
4. Indexing: Uses a pre-computed index to quickly locate specific data.

## Data Structures and Their Properties
Here's a brief overview of common data structures, their storage and retrieval properties, and techniques:

### Arrays
- Storage: Contiguous storage
- Retrieval: Linear search, binary search
- Properties: Fixed size, homogeneous elements

### Linked Lists
- Storage: Linked storage
- Retrieval: Linear search
- Properties: Dynamic size, heterogeneous elements

### Stacks and Queues
- Storage: Contiguous storage (stacks), linked storage (queues)
- Retrieval: Last-In-First-Out (LIFO) for stacks, First-In-First-Out (FIFO) for queues
- Properties: LIFO/FIFO ordering, dynamic size

### Trees
- Storage: Linked storage
- Retrieval: Linear search, binary search
- Properties: Hierarchical structure, dynamic size

### Hash Tables
- Storage: Indexed storage
- Retrieval: Hashing
- Properties: Fast lookup, insertion, and deletion, dynamic size

### Graphs
- Storage: Adjacency matrix or adjacency list
- Retrieval: Linear search, graph traversal algorithms
- Properties: Non-linear structure, dynamic size

This note covers the fundamental concepts of hashing, storage, and retrieval, as well as the properties and techniques of various data structures. Understanding these concepts is essential for designing and implementing efficient algorithms and data structures.
