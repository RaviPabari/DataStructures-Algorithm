#include<iostream>
using namespace std;
struct node{
	int data;
	node *next;
};
int main(){
	node *p;
	p = new node;
	p->data =10;
	p->next=NULL;
	return 0;
}
