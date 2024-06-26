#include <iostream>
#include <queue>
using namespace std;

vector<pair<int, int>> g[100001];
int state[100001] = {0};
int dis[100001] = {0};
#define _MAX 99999999
struct node
{
    friend bool operator<(node n1, node n2)
    {
        return n1.dis > n2.dis;
    }
    int dis;
    int number;
};

priority_queue<node> q;

int dijkstra(int n)
{
    dis[1] = 0;
    struct node cur_node;
    cur_node.dis = 0;
    cur_node.number = 1;
    q.push(cur_node);
    while (!q.empty())
    {
        cur_node = q.top();
        q.pop();
        int cur_number = cur_node.number;
        int cur_dis = cur_node.dis;
        if (state[cur_number])
        {
            continue;
        }
        state[cur_number] = 1;
        for (auto i : g[cur_number])
        {
            int tmp1 = i.first;
            int tmp2 = i.second;
            if (state[tmp1] == 0)
            {
                dis[tmp1] = min(tmp2 + dis[cur_number], dis[tmp1]);
                struct node new_node;
                new_node.dis = dis[tmp1];
                new_node.number = tmp1;
                q.push(new_node);
            }
        }
    }
    if (dis[n] != _MAX)
        return dis[n];
    else
        return -1;
}

int main()
{
    int n = 0, m = 0, start = 0, end = 0, value = 0;
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> start >> end >> value;
        g[start].push_back({end, value});
    }
    for (int i = 0; i < 100000; i++)
    {
        state[i] = 0;
        dis[i] = _MAX;
    }

    cout << dijkstra(n);
}