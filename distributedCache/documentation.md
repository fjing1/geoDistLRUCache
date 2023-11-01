# Documentation
This file the aim to explain the code and missing functionality.

### Node Class
The Node class represents a node in a doubly-linked list, each node contains a key-value pair and pointers to the
previous and next node

### LinkedList Class
The LinkedList class represents a doubly-linked list. It contains methods to add a node to the head of the list and 
to unlink a node from the list.

### LRUCache Class
The LRUCache class represents a Least Recently Used (LRU) cache with expiration. It contains methods to get and put 
items in the cache, remove expired items, evict the least recently used item, and remove an item.

#### Network Class
The Network class is responsible for network communications between different nodes in your system.

### Replication Class
The Replication class is responsible for managing the replication of data across different nodes. I intend to use
the primary-secondary replication here. When the primary is not available, the secondary replicas can be available.

## Missing functionalities
There are many functionalities that I didnt implement, including but not limited to following

1. Network and replication has not been fully tested on different host as well as packet loss and resend. 
2. Distributed caching, the current implementation is a local cache only, didnt support distributed cache
3. Thread safety, if there are multiple threads are accessing the modifying the cache at the same time, there
could be race condition
4. Cache statistics, I would like to add function to get cache usage, hit rate or number of entries
