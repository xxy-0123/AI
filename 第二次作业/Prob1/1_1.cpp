#include<iostream>
#include<queue>
using namespace std;
int g[10001][10001]={0};
int visit[10001]={0};
queue<int> q;

int bfs(int n){
    while(!q.empty()){
        for(int i=0;i<n;i++){
            int startpoint=q.front();
            q.pop();
            visit[startpoint]=1;
        }
    }

}

int main(){
    int n=0,m=0,start=0,end=0;


    cin>>n>>m;
    for(int i=0;i<m;i++){
        cin>>start>>end;
        g[start][end]=1;
    }
    q.push(0);
    cout<<bfs(n);

}