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

Our queue implementation supports the following methods:

- **push()** - puts a new value into the heap, maintaining the heap property.
- **pop()** - removes the “top” value in the heap, maintaining the heap property.


#Testing Coverage:
```
---------- coverage: platform darwin, python 2.7.11-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 33      6    82%   49-51, 56-58
src/dll.py                   70      1    99%   17
src/heap.py                  47      2    96%   18, 65
src/linked_list.py           58      3    95%   16, 26, 34
src/queue.py                 19      0   100%
src/stack.py                 13      0   100%
src/test_deque.py            68      0   100%
src/test_dll.py              82      0   100%
src/test_heap.py             34      0   100%
src/test_linked_list.py      74      0   100%
src/test_queue.py            64      0   100%
src/test_stack.py            48      3    94%   88-90
-------------------------------------------------------
TOTAL                       610     15    98%


======================================================= 88 passed in 0.43 seconds 
=======
TOTAL                       529     13    98%


========================== 78 passed in 0.21 seconds 


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 33      6    82%   49-51, 56-58
src/dll.py                   70      1    99%   17
<<<<<<< HEAD
src/heap.py                  47      2    96%   18, 65
src/linked_list.py           58      3    95%   16, 26, 34
src/queue.py                 19      0   100%
src/stack.py                 13      0   100%
src/test_deque.py            68      0   100%
src/test_dll.py              82      0   100%
<<<<<<< HEAD
src/test_heap.py             34      0   100%
src/test_linked_list.py      74      0   100%
src/test_queue.py            64      0   100%
src/test_stack.py            48      3    94%   88-90
-------------------------------------------------------
TOTAL                       610     15    98%


======================================================= 88 passed in 0.50 seconds ===
=======
TOTAL                       529     13    98%


========================== 78 passed in 0.27 seconds
```
