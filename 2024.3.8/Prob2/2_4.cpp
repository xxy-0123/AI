#include <iostream>
#include <queue>
#include <set>
using namespace std;

struct node
{
    string cur_s;
    int cur_x = 0;
    int count = 0;
    int fn=0;
    string path;
    friend bool operator< (node n1, node n2)
    {
        return n1.fn > n2.fn;
    }
}; //状态，位置，层数

int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
char step[4]={'u','l','d','r'};
priority_queue<node> q;
set<string> vis;

string target = "12345678x";

int f(struct node cur_node){
    int h=0;
    int x1 = cur_node.cur_x / 3;
    int y1 = cur_node.cur_x % 3;
    for(int i=0;i<9;i++){
        if(i==cur_node.cur_x){
            h+=abs(x1-2)+abs(y1-2);
        }else{
            h+=abs(i/3-(cur_node.cur_s[i]-'0')/3)+abs(i%3-(cur_node.cur_s[i]-'0')%3);
        }
    }
    return h+cur_node.count;
};

string A_8digits()
{
    while (!q.empty())
    {
        struct node cur_node;
        cur_node = q.top();
        if (cur_node.cur_s == target)
        {
            return cur_node.path;
        }
        q.pop();
        int x1 = cur_node.cur_x / 3;
        int y1 = cur_node.cur_x % 3;

        for (int i = 0; i < 4; i++)
        {
            int x2 = dx[i] + x1, y2 = dy[i] + y1; //移动后的x位置
            if (x2 < 0 || y2 < 0 || x2 > 2 || y2 > 2)
                continue;
            string new_s = cur_node.cur_s;
            int new_x = x2 * 3 + y2;
            int new_count = cur_node.count + 1;
            string new_path=cur_node.path+step[i];
            swap(new_s[cur_node.cur_x], new_s[new_x]);
            if (vis.count(new_s))
            {
                continue;
            }
            else
            {
                vis.insert(new_s);
            }
            struct node new_node;
            new_node.cur_s = new_s;
            new_node.cur_x = new_x;
            new_node.count = new_count;
            new_node.fn=f(new_node);
            new_node.path=new_path;
            q.push(new_node);
        }
    }
    return "unsolvable";
}

int main()
{
    string s = "";
    char t;
    int x = 0;
    for (int i=0;i<9;i++)
    {
        cin >> t;
        s += t;
        if (t == 'x')
        {
            x = i;
        }
    }
    vis.insert(s);
    struct node first_node;
    first_node.cur_s = s;
    first_node.cur_x = x;
    f(first_node);
    q.push(first_node);
    cout << A_8digits();
}
