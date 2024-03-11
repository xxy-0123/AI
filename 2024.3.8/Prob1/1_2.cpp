#include<iostream>
#include<queue>
using namespace std;
int g[10001][10001]={0};
int state[10001]={0};
int dis[10001]={0}; 

int dijkstra(int n){
    int startpoint=1,t=0;
    dis[1]=0;
    for(int i=0;i<n;i++){
        t=-1;
        for(int j=1;j<=n;j++){
            if(state[j]==0){
                if(t==-1||dis[j]<dis[t]){
                    t=j;
                }
            }
        }
        state[t]=1;
        for(int j=1;j<=n;j++){
            if(state[j]==0&&g[t][j]>0){
                dis[j]=min(g[t][j]+dis[t],dis[j]);
            }
        }
    }
    // for(int i=0;i<n;i++){
    //     cout<<dis[i]<<" ";
    // }
    if(dis[n]!=INT16_MAX)return dis[n];
    else return -1;
}

int main(){
    int n=0,m=0,start=0,end=0,value=0;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        cin>>start>>end>>value;
        g[start][end]=value;
    }
    for(int i=0;i<10000;i++){
        state[i]=0;
        dis[i]=INT16_MAX;
    }
    // for(int i=0;i<n;i++){
    //     cout<<dis[i]<<" ";
    // }
    cout<<dijkstra(n);
}