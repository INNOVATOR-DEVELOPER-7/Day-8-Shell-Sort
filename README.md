# Day-8-Shell-Sort
Here Python Program for Shell Sort. Day 8 of Day 365.
- Initial Setup: Start with an array that needs to be sorted.
- Gap Sequence: Choose a gap sequence. A common choice is to start with a large gap and reduce it gradually. The initial gap is usually half the length of the array.
- Sorting by Gap:
  - Compare elements that are a certain gap distance apart.
  - Perform an insertion sort on these elements.
  - Gradually reduce the gap and repeat the process.
- Completion: Continue this process until the gap is reduced to 1 and a final insertion sort is performed.

Here's a visual representation using the example array [12, 34, 54, 2, 3]:

1. Initial Array: [12, 34, 54, 2, 3]
2. Gap = 2:
   - Compare [12, 54], [34, 2]
   - Swap if necessary
   - Result: [12, 2, 54, 34, 3]
3. Next Gap = 1:
   - Perform insertion sort on the entire array
   - Compare [12, 2, 54, 34, 3]
   - Result: [2, 3, 12, 34, 54]
4. Final Sorted Array: [2, 3, 12, 34, 54]

The process ensures that the array is gradually sorted as the gap decreases.
