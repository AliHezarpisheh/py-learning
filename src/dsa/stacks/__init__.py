"""
Stacks are another essential data structure, following the Last-In-First-Out (LIFO)
principle. In a stack, the last element added is the first one to be removed. Picture a
stack of plates in a cafeteria. You add plates to the top of the stack, and when you
need to remove one, you take the top one off.

### Basic Operations:
1. **Push**: Adding an element to the top of the stack.
2. **Pop**: Removing the top element from the stack.
3. **Peek**: Viewing the top element of the stack without removing it.
4. **IsEmpty**: Checking if the stack is empty.
5. **Size**: Getting the number of elements in the stack.

### Implementation:
Stacks can be implemented using various data structures, including arrays and linked
lists. Arrays offer a simple implementation, but resizing can be inefficient if the
stack grows or shrinks frequently. Linked lists provide better flexibility for dynamic
resizing but may have slightly higher overhead due to node structures.

### Applications:
Stacks are used in various applications, including:
- **Function Calls**: In programming languages, the call stack is used to manage
                      function calls and returns.
- **Expression Evaluation**: Stacks can be used to evaluate postfix, prefix, or infix
                             expressions.
- **Undo Mechanisms**: Many applications implement undo functionality using a stack to
                       store previous states or actions.
- **Backtracking Algorithms**: Stacks are used in backtracking algorithms to store the
                               path taken so far.

### Variants:
- **Min Stack**: A stack that supports an additional operation to retrieve the minimum
                 element in constant time.
- **Max Stack**: Similar to a min stack, but it retrieves the maximum element instead.
- **Deque (Double-Ended Queue)**: A hybrid data structure that supports stack-like and
                                  queue-like operations. Elements can be added or
                                  removed from both ends.

### Language Support:
Many programming languages provide built-in support for stacks. For example, in Python,
you can use lists as stacks by using the `append()` method to push elements onto the
stack and the `pop()` method to remove elements from the top.

Stacks are a fundamental concept in computer science and are widely used in algorithm
design, data processing, and system implementation. Their simplicity and efficiency
make them invaluable in various domains of computer science and software engineering.
"""
