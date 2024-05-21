"""
A hash table, also known as a hash map, is a data structure that implements an
associative array, a structure that can map keys to values. It uses a hash
function to compute an index into an array of buckets or slots, from which the
desired value can be found.

**Key Concepts:**

1. **Hash Function**: This function takes an input (or 'key') and returns an
   integer called a hash code. The hash code is used to index the array where
   the value will be stored. A good hash function minimizes collisions and
   distributes keys uniformly.

2. **Buckets**: These are the slots in the array where values are stored. Each
   bucket corresponds to a computed hash code. Ideally, each key will map to a
   unique bucket, but in practice, multiple keys may hash to the same bucket.

3. **Collisions**: When two keys hash to the same bucket, a collision occurs.
   There are several strategies to handle collisions:
   - **Chaining**: Each bucket contains a linked list (or another structure)
     that holds all the values that hash to the same bucket.
   - **Open Addressing**: When a collision occurs, the algorithm searches for
     the next empty bucket according to a probing sequence (e.g., linear,
     quadratic, or double hashing).

4. **Load Factor**: This is the ratio of the number of elements in the hash
   table to the number of buckets. A high load factor indicates that many
   buckets are being shared, increasing the likelihood of collisions. Hash
   tables are often resized when the load factor exceeds a certain threshold.

5. **Operations**:
   - **Insertion**: To insert a key-value pair, compute the hash code of the
     key, find the corresponding bucket, and add the value. If the bucket is
     occupied, handle the collision appropriately.
   - **Lookup**: To find the value associated with a key, compute the hash
     code, locate the corresponding bucket, and retrieve the value. If
     collisions are handled by chaining, search the linked list in that bucket.
   - **Deletion**: To remove a key-value pair, find the key using the hash
     code, and then remove the value from the bucket.

**Advantages**:
- Average-case time complexity for insertion, deletion, and lookup is O(1),
  making hash tables very efficient.

**Disadvantages**:
- Performance can degrade with a poor hash function or high load factor.
- Requires resizing and rehashing when the load factor becomes too high.

Hash tables are widely used for fast data retrieval, such as in databases,
caches, and sets.
"""
