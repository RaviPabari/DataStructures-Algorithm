# Linear Time Selection
Problem of computing the ith smallest element of an input array (e.g., the median). It's easy to solve this problem in O(n log n) time using sorting, but we can do better! This is a super-practical randomized algorithm, very much in the spirit of QuickSort, that has *linear* expected running time. Don't forget that it takes linear time just to read the input! Basically,
there's a cool way to think about the progress the algorithm makes in terms of a simple coin-flipping experiment.<br>

`There are 2 ways we can solve this problem :`<br>
    - Involving Randomization (which is more efficient practically)<br>
    - One which does not involves randomization at all also called `Deterministic` 

<hr>

# Running Time For Randomized Algorithm
If we are very very unlucky then worst case running time = O(n^2) [ for example if pivot is chosen as minimum element every time ]<br>
Otherwise the average running time is O(n) with high probability.<hr>

# Running Time For Deterministic Algorithm
 Running time for deterministic algo in worst case in O(n), but the constansts which are hidden here are big compare to randomized version so this is not as fast as the randomized version, and this uses a method called
 median of medians.

<hr>

# About Median Of Medians 
 The median of medians is an approximate (median) selection algorithm, frequently used to supply a good pivot for an exact selection algorithm, mainly the quickselect, that selects the kth largest element of an initially 
 unsorted array. Median of medians finds an approximate median in linear time only, which is limited but an additional overhead for quickselect. When this approximate median is used as an improved pivot, the worst-case
 complexity of quickselect reduces significantly from quadratic to linear, which is also the asymptotically optimal worst-case complexity of any selection algorithm. In other words, the median of medians is an approximate median-selection algorithm
 that helps building an asymptotically optimal, exact general selection algorithm (especially in the sense of worst-case complexity), by producing good pivot elements.

