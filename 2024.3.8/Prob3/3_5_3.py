import matplotlib.pyplot as plt
import time
import queue
import matplotlib.animation as animation

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


def visualize_maze_with_path(frame, maze, path, memory):
    if frame < len(path):
        path_x, path_y, _ = zip(*path[:frame + 1])
        
        plt.imshow(maze, cmap='Greys', interpolation='nearest')

        new_colored_cells = []

        for i in range(frame + 1):
            plt.plot(path_y[:i + 1], path_x[:i + 1], marker='o',
                     markersize=8, color='red', linewidth=3)

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

    # Remove the redundant else block

interval = 0.0001

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

#path, memory = bfs(maze, n, m)
#path, memory = dfs(maze, n, m)
#path, memory = dijkstra(maze, n, m)
path, memory = A(maze, n, m)

ax=plt.figure(figsize=(len(maze[0])/2, len(maze)/2))
ani = animation.FuncAnimation(
    ax,
    visualize_maze_with_path,
    frames=range(len(path)),
    fargs=(maze, path, memory),
    interval=interval
)

#ani.save("bfs.gif", fps=5, writer="pillow")
#ani.save("dfs.gif", fps=5, writer="pillow")
#ani.save("dijkstra.gif", fps=5, writer="pillow")
ani.save("A.gif", fps=5, writer="pillow")