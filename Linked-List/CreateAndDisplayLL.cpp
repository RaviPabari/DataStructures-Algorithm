#include<iostream>
using namespace std;
//function to create a node
//A node contains 2 things, DATA and pointer to next node
struct Node{
	int data;
	Node *next;
};
//creating a global variable of type Node and setting it to NULL
Node *first = NULL; 

//function to create linked-list from the array
void create(int A[] , int n){
	int i;
//now we will scan through the array and take one element at a time and create linked-list
//*t is a temporary pointer and will help to create list
//*last pointer will help to create new node at the end of the list

	struct Node *t, *last;
//as the linked-list is empty we will create our first node
// and assign it to the first element in the array
	first = new Node;
	first -> data = A[0];
	first -> next = NULL; //because this is the first node and there is nothing beyond that
	last = first;
//also we will make last pointing to the first node
//now rest of the nodes we will create with the help of LOOP
	for(i=1;i<n;i++){
		t = new Node;
		t->data = A[i];
		t->next = NULL;
		last->next = t;
		last = t;
	}			
}

void Display(struct Node *p){
	while(p!=NULL){
		cout << p->data << endl;
		p = p-> next;
	}
}

int main(){
	struct Node *temp;
	int A[] = {9,5,7,12,15,16};
	create(A,6);
	Display(first);
	return 0;
}
