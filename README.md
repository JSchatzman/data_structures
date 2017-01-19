# Data-Structures

###This repo holds sample code for a number of classic data structures implemented in Python.

##Singly-Linked List in Python
- **Module:** linked_list.py
- **Tests:** test_linked_list.py

Our list implementation supports the following methods:

- **push(val)** will insert the value ‘val’ at the head of the list
- **pop()** will pop the first value off the head of the list and return it.
- **size()** will return the length of the list
- **search(val)** will return the node containing ‘val’ in the list, if present, else None
- **remove(node)** will remove the given node from the list, wherever it might be (node must be an item in the list)
- **display()** will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”


##Stack using Class Composition
- **Module:** stack.py
- **Tests:** test_stack.py
- **Resources Used:** https://codefellows.github.io/sea-python-401d5/lectures/inheritance_v_composition.html

Our stack implementation supports the following methods:

- **push(value)** - Adds a value to the stack. The parameter is the value to be added to the stack.
- **pop()** - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception class.


##Double linked list
- **Module:** dll.py
- **Tests:** test_dll.py
- **Resources Used** https://en.wikipedia.org/wiki/Doubly_linked_list

Our double linked list implementation supports the following methods:

- **push(val)** - will insert the value ‘val’ at the head of the list
- **append(val)** - will append the value ‘val’ at the tail of the list
- **pop()** - will pop the first value off the head of the list and return it.
- **shift()** - will remove the last value from the tail of the list and return it.
- **remove(val)** - will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.


##Queue
- **Module:** queue.py
- **Tests:** test_queue.py
- **Resources Used** http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html

Our queue implementation supports the following methods:

- **enqueue(value)** - adds value to the queue
- **dequeue()** - removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
- **peek()** - returns the next value in the queue without dequeueing it. If the queue is empty, returns None
- **size()** - return the size of the queue. Should return 0 if the queue is empty.

##Deque
- **Module:** deque.py
- **Tests:** deque.py
- **Resources Used** https://codefellows.github.io/sea-python-401d5/lectures/deque.html

Our dequeue implementation supports the following methods:

- **append(val)** - adds value to the end of the deque
- **appendleft(val)** - adds a value to the front of the deque
- **pop()** - removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
- **popleft()** - removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
- **peek()** - returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
- **peekleft()** - returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
- **size()** - returns the count of items in the queue (returns 0 if the queue is empty)


##Heap
- **Module:** heap.py
- **Tests:** test_heap.py
- **Resources Used** https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

Our Binary Heap implementation supports the following methods:

- **push()** - puts a new value into the heap, maintaining the heap property.
- **pop()** - removes the “top” value in the heap, maintaining the heap property.


##Graph
- **Module:** simple_graph.py
- **Tests:** test_simple_graph.py
- **Resources Used:** 
    - https://www.python.org/doc/essays/graphs/
    - https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837#.6xbpr1l6q
    - http://stackoverflow.com/questions/19472530/representing-graphs-data-str
    - http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

Our simple graph implementation supports the following methods:

- **nodes()** - return a list of all nodes in the graph.
- **edges()** - return a list of all edges in the graph.
- **add_node(n)** - adds a new node n to the graph.
- **add_edge(n1, n2)** - adds a new edge to the graph connecting n1 and n2,
if either n1 or n2 are not already present in the graph, they should be added.
- **del_node(n)** - deletes the node n from the graph, raises an error if no such node exists
- **del_edge(n1, n2)** - deletes the edge connecting n1 and n2 from the graph, raises an error if no such edge exists
- **has_node(n)** - True if node n is contained in the graph, False if not.
- **neighbors(n)** - returns the list of all nodes connected to n by edges, raises an error if n is not in g
- **adjacent(n1, n2)** - returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
- **g.depth_first_traversal(start)** - Perform a full depth-first traversal ofthe graph beginning at start. Return the full visited path when traversal is complete.
- **g.breadth_first_traversal(start)** - Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.
- **dijkstra** - If possible, find the shortest path between two nodes in a graph using Dijkstra's algorithm.
- **floyd_warshall** - If possible, find shortest path between two nodes in a graph using the Floyd Warshall algorithm.  This has a consistent complexity of O(V^3).  This has adavantages over Dijkstra's algorithm in certain situations.


##Binary Search Tree
- **Module:** bst.py
- **Tests:** test_bst.py

- **insert(val)** - Insert a new node into the bst.

- **size()** - Return the length of the bst.

- **depth()** - Find all maximum depth of this bst.

- **contains(val)** - Will return True if val is in the BST, False if not.

- **balance()** - Will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

- **search(val)** - Return Node containing the value.

- **in_order()** - In Order method for Binary Search Tree class. Return the values in order from smallest to largest.

- **pre_order()** - Pre_order method for Binary Search Tree class. Return a generator that will return the values in the tree using pre-order traversal, one at a time.

- **post_order()** - Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time.

- **breadth_first()** - Post_order method for Binary Search Tree class. return a generator that will return the values in the tree using post-order traversal, one at a time.

- **delete_node(val)** - Delete the node whose contents are the value given.
    Makes use of hidden methods for deleting a node with no children (barren), a node with one child (single child) and a node with two children (two children).

#Testing Coverage:

```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                     127      5    96%   136, 206-212
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     17    87%   102-108, 112-121, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                116      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1636     94    94%


====================================== 270 passed in 0.97 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                     127      5    96%   136, 206-212
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     18    86%   102-108, 112-121, 135, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                116      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1636     95    94%


====================================== 270 passed in 0.98 seconds
```


```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                      71      1    99%   86
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     18    86%   102-108, 112-121, 135, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                 59      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1523     91    94%


===============================================248 passed in 0.88 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                      71      1    99%   86
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     18    86%   102-108, 112-121, 135, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                 59      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1523     91    94%


==============================================248 passed in 0.97 seconds
```

```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                      69      1    99%   68
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     18    86%   102-108, 112-121, 135, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                 52      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1514     91    94%


============================================245 passed in 0.93 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bst.py                      69      1    99%   68
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue_.py                   19      0   100%
src/shortest_path_graph.py     133     18    86%   102-108, 112-121, 135, 179
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_bst.py                 52      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_shortest_path.py      189      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     151      0   100%
src/warshall.py                 24     24     0%   1-40
src/weighted_graph.py           73     27    63%   117-123, 127-136, 140-153
----------------------------------------------------------
TOTAL                         1514     91    94%


===========================================245 passed in 0.96 seconds


```
---------- coverage: platform darwin, python 2.7.11-final-0 ----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/deque.py                  30      0   100%
src/dll.py                    77      2    97%   16-17
src/heap.py                   25      2    92%   15-16
src/linked_list.py            58      3    95%   16, 26, 34
src/queue.py                  19      0   100%
src/simple_graph.py           66     11    83%   130-143
src/stack.py                  13      0   100%
src/test_deque.py             82      0   100%
src/test_dll.py               82      0   100%
src/test_heap.py              37      0   100%
src/test_linked_list.py       74      0   100%
src/test_queue.py             60      0   100%
src/test_simple_graph.py     147      0   100%
src/test_stack.py             48      3    94%   88-90
--------------------------------------------------------
TOTAL                        818     21    97%


==========================================131 passed in 0.48 


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/deque.py                  30      0   100%
src/dll.py                    77      2    97%   16-17
src/heap.py                   25      2    92%   15-16
src/linked_list.py            58      3    95%   16, 26, 34
src/queue.py                  19      0   100%
src/simple_graph.py           66     11    83%   130-143
src/stack.py                  13      0   100%
src/test_deque.py             82      0   100%
src/test_dll.py               82      0   100%
src/test_heap.py              37      0   100%
src/test_linked_list.py       74      0   100%
src/test_queue.py             60      0   100%
src/test_simple_graph.py     147      0   100%
src/test_stack.py             48      3    94%   88-90
--------------------------------------------------------
TOTAL                        818     21    97%

==========================================131 passed in 0.48 



```
