//Function List :
//1) Create(int Array,int sizeOfArray)
//2)Display(Node *First) and RecursiveDisplay(Node *First)
//3)Length(Node *First)
//4)SumOfAllElements(Node *First)
//5)MaxAndMin(Node *First)
//6)Search(Node *first, iny key)

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

void Search(Node *p,int key){
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


int main(){
	int A[]={1,2,3,4,5,6,344,8,9};
	int n=sizeof(A)/sizeof(A[0]);
	create(A,n);
	Display(first);
	Length(first);
	SumOfAllElements(first);
	MaxAndMin(first);
	Search(first,344);
	return 0;
}
