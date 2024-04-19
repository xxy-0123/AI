"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
import queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(maze, n, m):
    visited = set()
    visited.add((0, 0))
    memory = [(0, 0, 0)]
    queue = [(0, 0, 0)]  # (row, col, steps)
    parents = [[None] * m for _ in range(n)]
    path = []
    while queue:
        row, col, steps = queue.pop(0)
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            print(steps)
            while steps:
                steps -= 1
                row, col = parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                memory.append((new_row, new_col, steps + 1))
                queue.append((new_row, new_col, steps + 1))
                parents[new_row][new_col] = (row, col)


def dfs(maze, n, m):
    visited = set()
    visited.add((0, 0))
    memory = [(0, 0, 0)]
    stack = [(0, 0, 0)]  # (row, col, steps)
    parents = [[None] * m for _ in range(n)]
    path = []
    while stack:
        row, col, steps = stack.pop()
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            while steps:
                steps -= 1
                row, col = parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                memory.append((new_row, new_col, steps + 1))
                stack.append((new_row, new_col, steps + 1))
                parents[new_row][new_col] = (row, col)

def dijkstra(maze, n, m):
    memory = [(0, 0, 0)]
    distances = {(i, j): float('inf') for i in range(n) for j in range(m)}
    distances[(0, 0)] = 0
    pq = queue.PriorityQueue()
    pq.put((0, (0, 0)))
    parents = [[None] * m for _ in range(n)]
    path = []
    while queue:
        steps, (row, col) = pq.get()
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            print(steps)
            while steps:
                steps -= 1
                row, col = parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0:
                if steps + 1 < distances[(new_row, new_col)]:
                    distances[(new_row, new_col)] = steps + 1
                    memory.append((new_row, new_col, steps + 1))
                    pq.put((steps + 1, (new_row, new_col)))
                    parents[new_row][new_col] = (row, col)

def A(maze, n, m):
    visited = set()
    visited.add((0, 0))
    memory = [(0, 0, 0)]
    distances = {(i, j): float('inf') for i in range(n) for j in range(m)}
    distances[(0, 0)] = 0
    pq = queue.PriorityQueue()
    pq.put((n + m - 2, (0, 0, 0)))
    parents = [[None] * m for _ in range(n)]
    path = []
    while queue:
        dis, (row, col, steps) = pq.get()
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            print(steps)
            while steps:
                steps -= 1
                row, col = parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                new_dist = steps + abs(n - 1 - row) + abs(m - 1 - col)
                memory.append((new_row, new_col, steps + 1))
                pq.put((new_dist, (new_row, new_col, steps + 1)))
                parents[new_row][new_col] = (row, col)

def paint_maze(plt, maze, path_x, path_y, steps, memory, iterator, new_colored_cells, title):
    if iterator == 0:
        plt.imshow(maze, cmap='Greys', interpolation='nearest')
        plt.set_xticks(range(len(maze[0])))
        plt.set_yticks(range(len(maze)))
        plt.set_xticks(
            [x - 0.5 for x in range(1, len(maze[0]))], minor=True)
        plt.set_yticks(
            [y - 0.5 for y in range(1, len(maze))], minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
        plt.axis('on')
        plt.set_title(title)

    if iterator <= steps:
        plt.plot(path_y[:iterator + 1], path_x[:iterator + 1], marker='o',
                    markersize=8, color='red', linewidth=3)

        for x, y in new_colored_cells:
            color = 'yellow'
            plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                x + 0.5, color=color, alpha=0.5)

        new_colored_cells=[]

        for x, y, step in memory:
            if step == iterator: 
                color = 'blue'
                new_colored_cells.append((x, y))
                plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                    x + 0.5, color=color, alpha=0.5)

        return new_colored_cells
        
def getAllNab(node,maze):
    ret=list()
    lenx=len(maze)
    leny=len(maze[0])
    if(node[0]>0):
        ret.append((node[0]-1,node[1]))
    if(node[0]<lenx-1):
        ret.append((node[0]+1,node[1]))
    if(node[1]>0):
        ret.append((node[0],node[1]-1))
    if(node[1]<leny-1):
        ret.append((node[0],node[1]+1))
    return ret

import random

def gen_maze(S,lenx,leny):
    maze=list()
    lock=list()
    T=S
    for i in range(0,lenx):
        now=list()
        now1=list()
        for j in range(0,leny):
            now.append(1)
            now1.append(0)
        maze.append(now)
        lock.append(now1)
    q=queue.Queue()
    q.put(S)
    maze[S[0]][S[1]]=0
    cnt=0
    st=list()
    for i in getAllNab(S,maze):
        lock[i[0]][i[1]]+=1
    while(not q.empty()):
        now=q.get()
        st.append(now)
        cnt+=1
        if(cnt>lenx+leny):
            if(random.random()<0.003*cnt):
                break
        #print(now,maze[now[0]][now[1]],'?')
        nab=getAllNab(now,maze)
        potential_next=list()
        for i in nab:
            if(lock[i[0]][i[1]]<=1 and maze[i[0]][i[1]]>0):
                #print(i,maze[i[0]][i[1]],'!')
                potential_next.append(i)
        for i in potential_next:
            p=float(1)/len(potential_next)
            if(i[0]+i[1]>now[0]+now[1]):pass
            else:p-=0.1
            if(len(getAllNab(i,maze))<4):
                p-=0.5
            if(random.random()<p or i==potential_next[len(potential_next)-1]):
                for j in getAllNab(i,maze):
                    lock[j[0]][j[1]]+=1
                q.put(i)
                T=i
                maze[i[0]][i[1]]=0
                break
    tot_st=st.copy()
    st.pop()
    while(len(st)>0):
        idx=int(random.random()*len(st))
        i=st[idx]
        st.pop(idx)
        for j in getAllNab(i,maze):
            if(lock[j[0]][j[1]]<=1):
                if(random.random()<0.9):
                    st.append(j)
                    tot_st.append(j)
                    maze[j[0]][j[1]]=0
                    for k in getAllNab(j,maze):
                        lock[k[0]][k[1]]+=1

    T=tot_st[int(random.random()*len(tot_st))]

    tmp=tot_st[0]
    for i in tot_st:
        if(i[0]+i[1]>tmp[0]+tmp[1]):tmp=i
    while(tmp[0]<len(maze)-1):
        tmp=(tmp[0]+1,tmp[1])
        maze[tmp[0]][tmp[1]]=0
    while(tmp[1]<len(maze[0])-1):
        tmp=(tmp[0],tmp[1]+1)
        maze[tmp[0]][tmp[1]]=0
    T=tmp
    return maze,T  

def visualize_maze_with_path(maze, interval, bfs_path, bfs_memory,  dfs_path, dfs_memory, dijkstra_path, dijkstra_memory, A_path, A_memory):
    fig, axs = plt.subplots(2, 2, figsize=(16, 16), sharex=True, sharey=True)
    bfs_path_x, bfs_path_y, bfs_steps = zip(*bfs_path)
    dfs_path_x, dfs_path_y, dfs_steps = zip(*dfs_path)
    dijkstra_path_x, dijkstra_path_y, dijkstra_steps = zip(*dijkstra_path)
    A_path_x, A_path_y, A_steps = zip(*A_path)
    bfs_new_colored_cells = []
    dfs_new_colored_cells = []
    dijkstra_new_colored_cells = []
    A_new_colored_cells = []

    max_steps=max(bfs_steps[-1], dfs_steps[-1], dijkstra_steps[-1], A_steps[-1])
    for i in range(max_steps+1):
        if i <= bfs_steps[-1]:
            bfs_new_colored_cells=paint_maze(axs[0, 0], maze, bfs_path_x, bfs_path_y, bfs_steps[-1], bfs_memory, i, bfs_new_colored_cells, "BFS")
        if i <= dfs_steps[-1]:
            dfs_new_colored_cells=paint_maze(axs[0, 1], maze, dfs_path_x, dfs_path_y, dfs_steps[-1], dfs_memory, i, dfs_new_colored_cells, "DFS")
        if i <= dijkstra_steps[-1]:
            dijkstra_new_colored_cells=paint_maze(axs[1, 0], maze, dijkstra_path_x, dijkstra_path_y, dijkstra_steps[-1], dijkstra_memory, i, dijkstra_new_colored_cells, "Dijkstra")
        if i <= A_steps[-1]:
            A_new_colored_cells=paint_maze(axs[1, 1], maze, A_path_x, A_path_y, A_steps[-1], A_memory, i, A_new_colored_cells, "A*")
        fig.show()
        plt.pause(interval)
    plt.show()


interval = 0.0001

n, m = map(int, input().split())
# maze = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     maze.append(row)

S=(0,0)
maze=gen_maze(S,n,m)[0]

bfs_path, bfs_memory = bfs(maze, n, m)
dfs_path, dfs_memory = dfs(maze, n, m)
dijkstra_path, dijkstra_memory = dijkstra(maze, n, m)
A_path, A_memory = A(maze, n, m)
visualize_maze_with_path(maze, interval, bfs_path, bfs_memory,  dfs_path, dfs_memory, dijkstra_path, dijkstra_memory, A_path, A_memory)


# 15 15
# 0 0 0 1 0 0 1 0 0 0 0 1 1 1 1 
# 1 0 0 0 1 0 1 0 1 1 0 0 0 0 0 
# 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 
# 1 0 0 0 1 0 1 1 0 0 0 0 0 1 0
# 1 0 1 0 0 0 0 1 0 1 0 1 0 0 1
# 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0
# 0 1 0 0 0 1 0 0 0 1 0 0 1 1 0
# 0 1 0 0 1 0 0 1 0 0 1 0 1 0 0 
# 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 
# 0 1 0 0 1 0 1 0 0 1 0 0 1 1 0
# 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1
# 0 1 0 1 1 0 1 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
# 1 0 1 0 1 1 0 1 1 0 0 0 0 0 0
# 1 0 1 0 0 0 0 0 0 1 0 1 1 0 0

