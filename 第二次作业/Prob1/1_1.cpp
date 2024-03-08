#include<iostream>
using namespace std;
int g[10001][10001]={0};

int main(){
    int n=0,m=0,start=0,end=0;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        cin>>start>>end;
        g[start][end]=1;
    }
}