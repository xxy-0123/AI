#include<iostream>
#include<queue>
using namespace std;
int g[10001][10001]={0};
int state[10001]={0};
int dis[10001]={0}; 
struct node{    
    friend bool operator< (node n1, node n2)
    {        
        return n1.dis > n2.dis;    
    }    
    int dis;    
    int number;
};

priority_queue<node>q;

int dijkstra(int n){
    dis[1]=0;
    struct node cur_node;
    cur_node.dis=0;
    cur_node.number=1;
    q.push(cur_node);
    while(!q.empty()){
        cur_node=q.top();
        q.pop();
        int cur_number=cur_node.number;
        int cur_dis=cur_node.dis;
        if(state[cur_number]){continue;}
        state[cur_number]=1;
        for(int j=1;j<=n;j++){
            if(state[j]==0&&g[cur_number][j]>0){
                if(g[cur_number][j]+cur_dis<dis[j]){
                    dis[j]=g[cur_number][j]+cur_dis;
                    struct node new_node;
                    new_node.dis=dis[j];
                    new_node.number=j;
                    q.push(new_node);
                }
            }
        }
    }
    for(int i=0;i<n;i++){
        cout<<dis[i]<<" ";
    }
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