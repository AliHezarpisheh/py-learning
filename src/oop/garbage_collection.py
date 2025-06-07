"""
Python uses combination of reference counting and cyclic garbage collection.

Reference Counting (Primary Mechanism)
---
Each object keeps track of the number of references to it.
When the count drops to zero, the object is immediately deallocated.
The Problem: Circular References
Reference counting fails with cycles, e.g., a -> b -> a.
To handle this, Python uses:
Cyclic Garbage Collector (Secondary Mechanism)
Periodically finds and breaks cycles of unreachable objects.
Only objects that support cycle tracking (like lists, dicts, classes, etc.) are managed.
"""

import gc

gc.collect()             # Manually trigger collection
gc.disable()             # Turn off GC (not refcounting)
gc.enable()              # Turn it back on
gc.get_stats()           # Returns collection stats (3 gen)
gc.get_count()           # Objects in each generation
gc.get_threshold()       # Current thresholds
