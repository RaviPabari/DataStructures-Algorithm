# Linear Time Selection
Problem of computing the ith smallest element of an input array (e.g., the median). It's easy to solve this problem in O(n log n) time using sorting, but we can do better! This is a super-practical randomized algorithm, very much in the spirit of QuickSort, that has *linear* expected running time. Don't forget that it takes linear time just to read the input! Basically, there's a cool way to think about the progress the algorithm makes in terms of a simple coin-flipping experiment.<br><hr>
# Running Time
If we are very very unlucky then worst case running time = O(n^2) [ for example if pivot is chosen as minimum element every time ]<br>
Otherwise the average running time is O(n) with high probability. 
