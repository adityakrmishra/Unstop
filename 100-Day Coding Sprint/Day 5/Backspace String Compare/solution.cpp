#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string s1 , s2;
    cin>>s1>>s2;
    string reals1="", reals2 ="";
    stack<char> st1,st2;
    for(int i=0;i<s1.length();i++){
        if(s1[i] == '#' && st1.empty()) continue;
        if(s1[i] == '#'){
            st1.pop();
        }
        else st1.push(s1[i]);
    }
    for(int i=0;i<s2.length();i++){
        if(s2[i] == '#' && st2.empty()) continue;
        if(s2[i] == '#'){
            st2.pop();
        }
        else st2.push(s2[i]);
    }
    while(!st1.empty()){
        reals1 +=st1.top();
        st1.pop();
    }
    while(!st2.empty()){
        reals2+=st2.top();
        st2.pop();
    }
    if(reals1 == reals2) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    return 0;
}
