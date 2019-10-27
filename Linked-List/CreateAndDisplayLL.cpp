//Function List :
//1) Create(int Array,int sizeOfArray)
//2)Display(Node *First) and RecursiveDisplay(Node *First)
//3)Length(Node *First)
//4)SumOfAllElements(Node *First)
//5)MaxAndMin(Node *First)


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
void Create(int A[] , int n){
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

void RecursiveDisplay(Node *p){
	if(p!=NULL){
		cout << p->data << "->";
		RecursiveDisplay(p->next);
	}
}
	int count=0;
	while(p!=NULL){
		count++;
		p=p->next;
	}
	cout << "Length of the LL is: " << count << endl; 
}

void SumOfAllElements(Node *p){
	int sum=0;
	while(p!=NULL){
		sum += p->data;
		p=p->next;
	}
	cout << "The total sum of all elements in LL is :" << sum <<endl;
}

void MaxAndMin(Node *p){
	int max,min;
	max = p->data;
	min = p->data;
	while(p!=NULL){
		
		if(p->data > max){
			max = p->data;
		}
		if(p->data < min ){
			min = p->data;
		}
		p = p->next;
	}
	cout << "Max = " << max << " Min = " << min << endl;	
}

int main(){
	int A[]={1,2,3,4,5,6,344,8,9};
	int n=sizeof(A)/sizeof(A[0]);
	create(A,n);
	Display(first);
	Length(first);
	SumOfAllElements(first);
	MaxAndMin(first);
	return 0;
}
