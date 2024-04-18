import matplotlib.pyplot as plt
import queue
import matplotlib.animation as animation
import datetime
import os
from tqdm import tqdm
import sys

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
        # if (row, col) == (n - 1, m - 1):
        #     path.append((row, col, steps))
        #     #print(steps)
        #     while steps:
        #         steps -= 1
        #         row, col = parents[row][col]
        #         path.append((row, col, steps))
        #     path.reverse()
        #     return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                if (new_row, new_col) == (n - 1, m - 1):
                    steps+=1
                    parents[new_row][new_col] = (row, col)
                    path.append((new_row, new_col, steps))
                    memory.append((new_row, new_col, steps))
                    while steps:
                        steps -= 1
                        new_row, new_col = parents[new_row][new_col]
                        path.append((new_row, new_col, steps))
                    path.reverse()
                    return path, memory
                
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
    global_step = 0
    while stack:
        row, col, steps = stack.pop()
        global_step+=1
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            while steps and not (row==0 and col == 0):
                row, col ,steps= parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                memory.append((new_row, new_col, global_step))
                stack.append((new_row, new_col, global_step))
                parents[new_row][new_col] = (row, col, steps)


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
        # if (row, col) == (n - 1, m - 1):
        #     path.append((row, col, steps))
        #     #print(steps)
        #     while steps:
        #         steps -= 1
        #         row, col = parents[row][col]
        #         path.append((row, col, steps))
        #     path.reverse()
        #     return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0:
                if (new_row, new_col) == (n - 1, m - 1):
                    steps+=1
                    path.append((new_row, new_col, steps))
                    memory.append((new_row, new_col, steps))
                    parents[new_row][new_col] = (row, col)
                    while steps:
                        steps -= 1
                        new_row, new_col = parents[new_row][new_col]
                        path.append((new_row, new_col, steps))
                    path.reverse()
                    return path, memory
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
        # if (row, col) == (n - 1, m - 1):
        #     path.append((row, col, steps))
        #     #print(steps)
        #     while steps:
        #         steps -= 1
        #         row, col = parents[row][col]
        #         path.append((row, col, steps))
        #     path.reverse()
        #     return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                if (new_row, new_col) == (n - 1, m - 1):
                    steps+=1
                    path.append((new_row, new_col, steps))
                    memory.append((new_row, new_col, steps))
                    parents[new_row][new_col] = (row, col)
                    while steps:
                        steps -= 1
                        new_row, new_col = parents[new_row][new_col]
                        path.append((new_row, new_col, steps))
                    path.reverse()
                    return path, memory
                visited.add((new_row, new_col))
                new_dist = steps + abs(n - 1 - new_row) + abs(m - 1 - new_col)
                memory.append((new_row, new_col, steps + 1))
                pq.put((new_dist, (new_row, new_col, steps + 1)))
                parents[new_row][new_col] = (row, col)


def visualize_maze_with_path(frame, maze, path, memory, k, new_colored_cells):
    if frame <= path[-1][2]+2:
        path_x, path_y, steps = zip(*path)
        
        plt.imshow(maze, cmap='Greys', interpolation='nearest')

        
        i=frame
        if k[0]<len(steps):
            if(i==steps[k[0]]):
                plt.plot(path_y[:k[0] + 1], path_x[:k[0] + 1], marker='o',
                        markersize=8, color='red', linewidth=3)
                k[0]+=1

        for x, y in new_colored_cells:
            color = 'yellow'
            plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                x + 0.5, color=color, alpha=0.5)

        new_colored_cells.clear()

        for x, y, step in memory:
            if step == i: 
                color = 'blue'
                new_colored_cells.append((x, y))
                plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                    x + 0.5, color=color, alpha=0.5)

        plt.xticks(range(len(maze[0])))
        plt.yticks(range(len(maze)))
        plt.gca().set_xticks(
            [x - 0.5 for x in range(1, len(maze[0]))], minor=True)
        plt.gca().set_yticks(
            [y - 0.5 for y in range(1, len(maze))], minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
        plt.axis('on')

        return plt.gca()


def generate_animation_and_stats(algorithm_name, path_func, maze, n, m, output_folder):
    path, memory = path_func(maze, n, m)
    total_path_length = len(path) - 1
    total_searched_points = len(memory)
    stats_md = f"### {algorithm_name}\n\n"
    stats_md += f"- Total Path Length: {total_path_length}\n"
    stats_md += f"- Total Searched Points: {total_searched_points}\n\n"

    new_colored_cells = []
    k = [0]
    ax = plt.figure(figsize=(len(maze[0]) / 2, len(maze) / 2))
    ani = animation.FuncAnimation(
        ax,
        visualize_maze_with_path,
        frames=range(path[-1][2] + 2),
        fargs=(maze, path, memory, k, new_colored_cells),
        interval=interval
    )

    timestamp = datetime.datetime.now().strftime("%m%d%H%M")
    output_folder = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_folder, exist_ok=True)
    gif_filename = f"{algorithm_name}_{timestamp}.gif"
    gif_filepath = os.path.join(output_folder, gif_filename)
    ani.save(gif_filepath, fps=5, writer="pillow")
    stats_md += f"![{algorithm_name} Animation]({gif_filepath})\n\n"
    return stats_md

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

if __name__ == "__main__":
    interval = 0.0001
    output_folder = "maze_search"

    n, m = map(int, input().split())
    # maze = []
    # for _ in range(n):
    #     row = list(map(int, input().split()))
    #     maze.append(row)

    S=(0,0)
    maze=gen_maze(S,n,m)[0]

    markdown_content = ""
    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("Dijkstra", dijkstra),
        ("A_star", A)
    ]
    
    with tqdm(total=len(algorithms), desc="Generating Statistics and GIFs") as pbar:
        for algorithm_name, path_func in algorithms:
            markdown_content += generate_animation_and_stats(algorithm_name, path_func, maze, n, m, output_folder)
            pbar.update(1)

    output_folder_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_folder_path, exist_ok=True)
    output_filepath = os.path.join(output_folder_path, "maze_statistics.md")

    with open(output_filepath, "w") as f:
        f.write(markdown_content)

    print("end")
    sys.exit()