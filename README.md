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

##Weighted Graph
- **Module:** weighted_graph.py
- **Tests:** test_weighted_graph.py

Our weighted graph implementation supports the following methods:

- **nodes()** - return a list of all nodes in the graph.
- **edges()** - return a list of all edges in the graph.
- **add_node(n)** - adds a new node n to the graph.
- **add_edge(n1, n2, weight)** - adds a new edge to the graph connecting n1 and n2,
if either n1 or n2 are not already present in the graph, they should be added. Adds numerical weight to the edge which is by default 1.
- **del_node(n)** - deletes the node n from the graph, raises an error if no such node exists
- **del_edge(n1, n2)** - deletes the edge connecting n1 and n2 from the graph, raises an error if no such edge exists
- **has_node(n)** - True if node n is contained in the graph, False if not.
- **neighbors(n)** - returns the list of all nodes connected to n by edges, raises an error if n is not in g
- **adjacent(n1, n2)** - returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
- **g.depth_first_traversal(start)** - Perform a full depth-first traversal ofthe graph beginning at start. Return the full visited path when traversal is complete.
- **g.breadth_first_traversal(start)** - Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.


#Testing Coverage:
```
---------- coverage: platform darwin, python 2.7.11-final-0 ----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue.py                    19      0   100%
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     154      0   100%
src/weighted_graph.py           77     27    65%   121-127, 131-140, 144-157
----------------------------------------------------------
TOTAL                         1054     48    95%


==================================================== 171 passed in 0.54 seconds 


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/deque.py                    30      0   100%
src/dll.py                      77      2    97%   16-17
src/heap.py                     25      2    92%   15-16
src/linked_list.py              58      3    95%   16, 26, 34
src/queue.py                    19      0   100%
src/simple_graph.py             71     11    85%   136-149
src/stack.py                    13      0   100%
src/test_deque.py               82      0   100%
src/test_dll.py                 82      0   100%
src/test_heap.py                37      0   100%
src/test_linked_list.py         74      0   100%
src/test_queue.py               60      0   100%
src/test_simple_graph.py       147      0   100%
src/test_stack.py               48      3    94%   88-90
src/test_weighted_graph.py     154      0   100%
src/weighted_graph.py           77     27    65%   121-127, 131-140, 144-157
----------------------------------------------------------
TOTAL                         1054     48    95%


==================================================== 171 passed in 0.77 seconds 

```
