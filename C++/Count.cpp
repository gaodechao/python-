/*问题描述：
书的页码从一开始，
问：输入页码数，正整数n（1<=n<=10e9）
输出0，1,2,…，9的个数
算法思想：计算每个数所用到的数字个数，

*/
#include<iostream>
#include<fstream>
#include<Windows.h>
using namespace std;
int main()
{
	//定义统计数组，并初始化为零
	int Count[10];
	for (int i = 0; i < 10; i++)
		Count[i] = 0;
	ifstream in("D:\\worksapce\\test\\input.txt");
	if (!in.is_open())
		cout << " open input file filed," << endl;
	long int n;
	in >> n;
	//统计数字个数部分；
	while (n){
		long int t = n;
		while (t) {
			Count[t % 10]++;
			t /= 10;
		}
		n--;
	}
	//输出部分
	ofstream out("D:\\worksapce\\test\\output.txt");
	for (int i = 0; i < 10; i++)
		out <<i<< ":   "<< Count[i] << endl;
	cout << "计算成功：" << endl;
	system("pause");
	return 0;
}