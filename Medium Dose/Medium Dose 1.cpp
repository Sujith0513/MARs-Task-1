#include <bits/stdc++.h>
using namespace std;
struct student
{
string student_name;
int rollno;
float cgpa;
};

int main()
{
    int p=8;
    vector<struct student> s={{"Anush",9,9.5},{"Adharsh",4,6.9},{"Harshinie",8,8.3},{"Shivani",6,7.7}};
    for_each(s.begin(),s.end(),[p](struct student x)
    {
        cout <<"Student name : " << x.student_name <<"\n";
        cout <<"Roll Number : " << x.rollno ;
        if(x.cgpa>=p)
        {
            cout <<" Good\n";
        }
        else
        {
            cout <<" Need Improvement\n";
        }
        cout <<"\n";
    });
    return 0;
}