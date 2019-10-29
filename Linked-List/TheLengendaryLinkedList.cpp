//Function List :
//1)Create(int Array,int sizeOfArray)
//2)Display(Node *First) and RecursiveDisplay(Node *First)
//3)Length(Node *First)
//4)SumOfAllElements(Node *First)
//5)MaxAndMin(Node *First)
//6)Search(Node *first, int key) and RecursiveSearch(Node *p,int key)   and  ImprovedSearch(Node *first, int key)
//7)Insert(int position, int data)

#include<iostream>
using namespace std;

class Node{
	public:
		int data;
		Node *next;
};
Node *first=NULL;

void create(int A[],int n){
	first = new Node;
	first -> data = A[0];
	first -> next = NULL;
	Node *last,*temp;
	int i;
	last = first;
	
	for(i=1;i<n;i++){
		temp = new Node;
		temp -> data = A[i];
		temp->next = NULL;
		last->next = temp;
		last = temp;
	}
}

void Display(Node *p){
	while(p!=NULL){
		cout << p->data << "->" ;
		p = p->next;
	}
	cout << "NULL" << endl;
}

void RecursiveDisplay(Node *p){
	if(p!=NULL){
		cout << p->data << "->";
		RecursiveDisplay(p->next);
	}
	cout << "NULL" << endl;
}

//length or number of nodes in a LL;
void Length(Node *p){ 
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

void Search(Node *p,int key){			//iterative searching function
	int count=0;
	while(p!=NULL){
		count ++;
		if(p->data == key){
			cout <<"Element " << key <<" found at position no. " << count << endl;  
			break;
		}
		p=p->next;
	}
}

int RecursiveSearch(Node *p,int key){	//recursive searching function
	if(p==NULL){
		return NULL;		
	}
	if(p->data==key){
		return p->data;
	}
	return RecursiveSearch(p->next,key);
}
//methods to improve searching 
//1-> Transposotion method	(we will not prefer this in LL if it was array then was ok..) 
//2-> Move To head	(the last searched element moves to first position)

void ImprovedSearch(Node *p,int key){
	Node *q = NULL;
	while(p!=NULL){
		if(key==p->data){
			q->next = p->next;
			p->next = first;
			first = p;
		}
		q=p;
		p=p->next;		
	}
}

void Insert(int pos,int x){
	Node *p,*t;
	if(pos==0){
		t = new Node();
		t->data = x;
		t->next = first;
		first = t;
	}else if(pos >0){
		p = first;
		for(int i=0;i<pos-1 && p!=NULL;i++){
			p = p->next;
		}
		if(p!=NULL){
			t = new Node();
			t->data = x;
			t->next = p->next;
			p->next = t;
		}
	}
}

int main(){
	int A[]={1,2,3,4,5,6,344,8,9};
	int n=sizeof(A)/sizeof(A[0]);
	create(A,n);
	Display(first);
	Length(first);
	SumOfAllElements(first);
	MaxAndMin(first);
	Search(first,344);
	Insert(4,144);
	Display(first);
	Insert(0,12);
	Display(first);
	return 0;
}
