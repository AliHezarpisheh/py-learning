"""
Queues are fundamental data structure used in computer science. They follow the
First-In-First-Out (FIFO) principle, meaning that the first element added to the queue
will be the first one to be removed. Think of it like a queue of people waiting in line
at a ticket counter or a cashier in a supermarket. The person who arrives first gets
served first.

### Basic Operations:
1. **Enqueue**: Adding an element to the rear end of the queue.
                This operation is also known as "push."
2. **Dequeue**: Removing an element from the front end of the queue.
                This operation is also known as "pop."
3. **Front**: Getting the element at the front end of the queue without removing it.
4. **Rear**: Getting the element at the rear end of the queue without removing it.
5. **IsEmpty**: Checking if the queue is empty.
6. **Size**: Getting the number of elements in the queue.

### Implementation:
Queues can be implemented using various data structures such as arrays, linked lists, or
other collections. Arrays are often used for simple implementations, but they may have
limitations in dynamic resizing. Linked lists provide better flexibility for dynamic
resizing but may have slightly higher overhead due to the need for node structures.

### Applications:
Queues are used in various applications, including:
- **Process Scheduling**: CPU scheduling in operating systems often involves queues to
                          manage processes.
- **Breadth-First Search (BFS)**: In graph algorithms, queues are used to implement BFS
                                  traversal.
- **Print Queue**: Managing documents waiting to be printed.
- **Message Queues**: Communication between different parts of a system or between
                      systems often involves message queues.
- **Task Scheduling**: In multitasking environments, queues can be used to manage tasks
                       waiting to be executed.

### Variants:
- **Priority Queue**: A queue where elements are dequeued based on their priority rather
                      than their arrival time.
- **Circular Queue**: A queue where the rear end wraps around to the front end,
                    effectively forming a circular structure. This can be useful in
                    scenarios where space is limited or when you want to reuse freed-up
                    space.

Queues are a versatile data structure and are widely used in various domains of computer
science and software engineering. Their simplicity and efficiency make them a
fundamental building block in algorithm design and system implementation.
"""