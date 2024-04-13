"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
import queue
from time import sleep
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
        
def animate_maze(frame, axs, maze, paths, memories, titles):
    for ax, (path, memory, title, cells) in zip(axs.flat, paths):
        iterator = frame % (path[-1][2] + 1)
        ax.clear()
        ax.imshow(maze, cmap='Greys', interpolation='nearest')
        ax.set_xticks(range(len(maze[0])), minor=True)
        ax.set_yticks(range(len(maze)), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
        ax.axis('on')
        ax.set_title(title)

        if iterator > 0:
            path_x, path_y, _ = zip(*path)
            ax.plot(path_y[:iterator + 1], path_x[:iterator + 1], marker='o',
                        markersize=8, color='red', linewidth=3)

            for x, y in cells:
                color = 'yellow'
                ax.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                    x + 0.5, color=color, alpha=0.5)

            cells.clear()

            for x, y, step in memory:
                if step == iterator:
                    color = 'blue'
                    cells.append((x, y))
                    ax.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                        x + 0.5, color=color, alpha=0.5)

def visualize_maze_with_path(maze, interval, bfs_path, bfs_memory, dfs_path, dfs_memory, dijkstra_path, dijkstra_memory, A_path, A_memory):
    fig, axs = plt.subplots(2, 2, figsize=(16, 16), sharex=True, sharey=True)
    bfs_path_x, bfs_path_y, bfs_steps = zip(*bfs_path)
    dfs_path_x, dfs_path_y, dfs_steps = zip(*dfs_path)
    dijkstra_path_x, dijkstra_path_y, dijkstra_steps = zip(*dijkstra_path)
    A_path_x, A_path_y, A_steps = zip(*A_path)
    bfs_new_colored_cells = []
    dfs_new_colored_cells = []
    dijkstra_new_colored_cells = []
    A_new_colored_cells = []

    max_steps = max(bfs_steps[-1], dfs_steps[-1], dijkstra_steps[-1], A_steps[-1])
    paths = [
        (bfs_path, bfs_memory, "BFS", bfs_new_colored_cells),
        (dfs_path, dfs_memory, "DFS", dfs_new_colored_cells),
        (dijkstra_path, dijkstra_memory, "Dijkstra", dijkstra_new_colored_cells),
        (A_path, A_memory, "A*", A_new_colored_cells)
    ]

    titles = ["1", "2", "3", "4"]

    ani = animation.FuncAnimation(
        fig,
        animate_maze,
        frames=range(max_steps + 1),
        fargs=(axs, maze, paths, titles, [bfs_new_colored_cells, dfs_new_colored_cells, dijkstra_new_colored_cells, A_new_colored_cells]),
        interval=interval
    )

    ani.save("animation.gif", fps=5, writer="pillow")


import matplotlib.animation as animation




interval = 0.0001

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

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

