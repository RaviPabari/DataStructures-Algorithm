# Karger's Minimum Cut Algorithm For Undirected Graph
**The random contraction algorithm, discovered by Karger only 20ish years ago (while a PhD student at Stanford). This algorithm solves the minimum cut problem --- given an undirected graph, separate the vertices into two non-empty groups to minimize the number of "crossing edges". Such problems come up when reasoning about, for example, physical networks, social networks, and images.<br> 
This algorithm was perhaps the first strong evidence that graph problems could be added to the long list of killer applications of random sampling**
<br>
**This algorithm is totally randomized and does not always guarantees to find the minimum cut so we can use a simple but useful trick for transforming an algorithm that almost always fails into one that almost always succeeds, that we will run the algorithm many times with different random seeds, and will store all the minimum cuts returned and will finally return the minimum of all that min cuts as our final min cut.**
<hr>
The txt file contains the adjacency list representation of a simple undirected graph. 
There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, 
and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : 6 155 56 52 120 ....... This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with 
labels 155,56,52,120,...etc

