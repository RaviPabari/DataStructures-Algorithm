# Randomized Quicksort Algorithm Implemented In Python
`One of the greatest algorithms ever and great example of randomized algorithm.`


This folder contains 4 QuickSort implementation and 1 Quick.txt

  - QuickSort1.py -->   First Index Is Pivot
  - QuickSort2.py -->   Pivot Index is **Random**
  - QuickSort3.py -->   Last Index Is Pivot
  - QuicksSort4.py -->  "median-of-three" pivot rule
  - Quick.txt --> txt file containing 10,000 numbers (int)

# "median-of-three" pivot rule

  - `The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.` In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k2k, use the k^{th}k th element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

**EXAMPLE:** For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

**SUBTLE POINT:** A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add m-1m−1 to your running total of comparisons every time you recurse on a subarray with length mm.

**NOTE** Quick.txt file is taken from the course Divide and Conquer, Sorting and Searching, and Randomized Algorithms
by Stanford University, Week-3 Programming Assignment
