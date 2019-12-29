#include<iostream>
using namespace std;
#define size 10
int top = -1;
int stack[size];


void push(int value){
	if(top == size-1){
		cout << "Overflow, Stack is full" << endl;
	}else{
		top++;
		stack[top]=value;
		cout<<"Insertion was successfulllll"<< endl;
	}
}

int pop(){
	if(top == -1){
		cout << "Underflow , Stack is empty" << endl;
	}else{
		cout << "Removing..." << stack[top]<< endl;
		top--;
		return stack[top];
	}
}

void Display(){
	if(top == -1){
		cout << "Stack is empty WTF !" << endl;
	}else{
		for(int i=top;i>=0;i--){
			cout <<stack[i] << endl;
		}
	}
}

int main(){
	push(10);
	push(30);
//	push(20);
	Display();
	cout << pop() << endl;
	cout << pop() << endl;
	Display();
	return 0;
}
