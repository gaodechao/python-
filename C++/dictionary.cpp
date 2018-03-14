/*
字典序问题
算法设计：对于给定的任意字符串不超过6的升序字符串，计算在字典中的编码。
输入：字符串，长度不超过六；
输出：字符串编码
*/
#include<iostream>
#include<string>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
	int k;
	ifstream in("D:\\worksapce\\test\\input.txt");
	ofstream fout("D:\\worksapce\\test\\output.txt", ios::app);
	in >> k;
	string str;
	getline(in,str);
	while (k--)
	{
		string str;
		getline(in, str);
		cout << str;
		if (str.size() > 6)
			cout << "the scope given in the problem" << endl;
		int code = 0;
		for (int i = 0; i < str.size(); i++)
			code += (str[i] - 'a'-i + 1)*pow(26, str.size() - i-1);
		fout << code << endl;
		system("pause");
	}
	in.close();
	fout.close();
	return 0;
}