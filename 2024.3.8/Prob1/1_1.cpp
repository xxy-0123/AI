#include<iostream>
#include<queue>
using namespace std;
int g[10001][10001]={0};
int visit[10001]={0};
int parent[10001]={0}; 
queue<int> q;

int bfs(int n){
    int startpoint=1,count=0;
    while(!q.empty()){
        startpoint=q.front();
        if(startpoint==n){
            count=0;
            while(startpoint!=1){
                startpoint=parent[startpoint];
                count++;
            }
            return count;
        }
        q.pop();
        //if(visit[startpoint]==1){continue;}
        visit[startpoint]=1;
        for(int i=1;i<=n;i++){
            if(visit[i]==0){
                if(g[startpoint][i]==1){
                    q.push(i);
                    parent[i]=startpoint;
                    visit[i]=1;
                }
            }
        }
    }
    return -1;
}

int main(){
    int n=0,m=0,start=0,end=0;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        cin>>start>>end;
        g[start][end]=1;
    }
    for(int i=0;i<10000;i++){
        visit[i]=0;
        parent[i]=0;
    }
    q.push(1);
    cout<<bfs(n);
}