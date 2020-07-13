#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	cout<<"Liet ke cac chu so la so nguyen to\n";
	int n;
	cout<<"+Nhap n:";
	cin>>n;
	do
	{
	    int cs = n % 10;
		n = n/10;
        int souoc = 1;
        for(int i= 1;i<cs;i++)
        {
        	if(cs % i==0)
        	souoc++;
		}
		if(souoc == 2)
		cout<<"Chu so la so nto:"<<cs<<"\n";
	}	
	while(n > 0);
	return 0;
}
