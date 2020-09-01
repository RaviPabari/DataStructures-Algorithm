# Inversion Count
`This problem is related to measuring similarity between two ranked lists, 
which in turn is relevant for making good recommendations to someone based on your knowledge of their and others' preferences ("collaborative filtering").` <hr>
Most answers are based on MergeSort but it isn't the only way to solve this is in O(nlogn)

I'll discuss a few approaches.

1). Use a Balanced Binary Search Tree

Augment your tree to store frequencies for duplicate elements.
The idea is to keep counting greater nodes when the tree is traversed from root to a leaf for insertion.
Something like this.
```
Node *insert(Node* root, int data, int& count){
    if(!root) return new Node(data);
    if(root->data == data){
        root->freq++;
        count += getSize(root->right);
    }
    else if(root->data > data){
        count += getSize(root->right) + root->freq;
        root->left = insert(root->left, data, count);
    }
    else root->right = insert(root->right, data, count);
    return balance(root);
}

int getCount(int *a, int n){
    int c = 0;
    Node *root = NULL;
    for(auto i=0; i<n; i++) root = insert(root, a[i], c);
    return c;
}
```
<hr>
2). Use a Binary Indexed Tree
 Create a summation BIT.
Loop from the end and start finding the count of greater elements.

```
int getInversions(int[] a) {
    int n = a.length, inversions = 0;
    int[] bit = new int[n+1];
    compress(a);
    BIT b = new BIT();
    for (int i=n-1; i>=0; i--) {
         inversions += b.getSum(bit, a[i] - 1);
         b.update(bit, n, a[i], 1);
     }
     return inversions;
}
```
<hr>
3). Use a Segment Tree 
Create a summation segment Tree.
Loop from the end of the array and query between [0, a[i]-1] and update a[i] with

```
int getInversions(int *a, int n) {
    int N = n + 1, c = 0;
    compress(a, n);
    int tree[N<<1] = {0};
    for (int i=n-1; i>=0; i--) {
        c+= query(tree, N, 0, a[i] - 1);
        update(tree, N, a[i], 1);
    }
    return c;
}
```

<hr>
Also, when using BIT or Segment-Tree a good idea is to do Coordinate compression

```
void compress(int *a, int n) {
    int temp[n];
    for (int i=0; i<n; i++) temp[i] = a[i];
    sort(temp, temp+n);
    for (int i=0; i<n; i++) a[i] = lower_bound(temp, temp+n, a[i]) - temp + 1;
}
```

`This was taken from stackoverflow just for information purpose, I do not own this explanation`
