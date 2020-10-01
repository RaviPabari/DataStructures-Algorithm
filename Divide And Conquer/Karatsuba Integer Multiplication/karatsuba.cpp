#include <iostream>
using namespace std;


int power(int exp){
	// returns 10 power exp
	int retV = 1;
	for(int i = 0; i < exp;i++){
		retV *= 10;
	}
       return retV;	
}




int noOfDigits(unsigned long long a){
	// returns number of digits in a
	if(a == 0){
		return 1;
	}
	int counter = 0;
	while(a != 0){
		a /= 10;
		counter += 1;
	}
	return counter;
}

unsigned long long multi(unsigned long long x,unsigned long long y){
	// A recursive karatsuba multiplication function
	// The normal multiplication comprises of n*n single digit multiplication and n single digit addition
	// This costs O(n*n)
	// while karatsuba multiplications comprises of 3 recursuve calls and 3 additions at every step
	int n;
	int n1 = noOfDigits(x);
	int n2 = noOfDigits(y);
	n = min(n1,n2);
	if(n == 1){
		return x*y;
	}else{
		int base10 = power(n);
		// base10 is ten power to the number of digits
		int hbase10 = power(n/2);
		// hbase10 is ten power to the half of number of digits
		



		//a is first half digits of x,b is second half digits of x
		unsigned long long a = (x / hbase10);
		unsigned long long b = (x % hbase10);
		//c is first half digits of y,d is remaining half digits
		unsigned long long c = (y / hbase10);
		unsigned long long d = y%hbase10;

		//Recursive calls
		unsigned long long firstterm = multi(a,c);
		//firstmerm finds multiplication a*c
		unsigned long long thirdterm = multi(b,d);
		//thirdterm finds multiplication b*d
		int secondterm = multi(a+b,c+d);
		secondterm -= (firstterm + thirdterm);
		//In second term, using Gauss' trick : (a+b)*(c+d) - a*c - b*d = a*d + b*c
		
		
		//The following formula returns multiplication of x and y
		return ((base10*firstterm)+(hbase10*secondterm)+thirdterm);
	}

}

int main(){
	cout << "Enter two numbers"<<endl;
	unsigned long long a,b;
	cin >> a >> b;
	unsigned long long ans;
	ans = multi(a,b);
	cout << "The answer is "<< ans << endl;
	return 0;

}
