#include<iostream>
using namespace std;
class Node{
	public:
		int data;
		Node *next;
};

void Display(Node *p){	//traversing ll and printing them
	while(p!=NULL){
		cout << p->data <<" " ;
		p = p->next;
	}
}

int main(){
	Node *first=NULL;
	Node *second=NULL;
	Node *third=NULL;
	
	first = new Node();
	second = new Node();
	third = new Node();
	
	first -> data = 10;
	first -> next = second;
	
	second -> data = 20;
	second -> next = third;
	
	third -> data = 30;
	third -> next = NULL;
	
	Display(first);
	return 0;
}
