"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
import queue
import random
tot_cnt=0
def visualize_maze_with_path(maze, path,st):
    global tot_cnt

    tot_cnt+=1
    plt.subplot(1, 4, tot_cnt)
    if(tot_cnt==1):
        plt.title("A_star \ncost:"+str(len(st))+"\n lenght:"+str(len(path)))
    elif(tot_cnt==2):
        plt.title("bfs \ncost:"+str(len(st))+"\n lenght:"+str(len(path)))
    elif(tot_cnt==3):
        plt.title("dij \ncost:"+str(len(st))+"\n lenght:"+str(len(path)))
    elif(tot_cnt==4):
        plt.title("dfs(not shortest) \ncost:"+str(len(st))+"\n lenght:"+str(len(path)))
      # 设置图形大小
   
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if(maze[i][j]==0.5):
                maze[i][j]=1
            elif (maze[i][j]==1):
                maze[i][j]=0
            else:maze[i][j]=0.5
    plt.imshow(maze, cmap='viridis', interpolation='nearest')  # 使用灰度色图，并关闭插值
    #plt.imshow(maze, cmap='gray', interpolation='nearest')  # 使用灰度色图，并关闭插值
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if(maze[i][j]==1):
                maze[i][j]=0.5
            elif (maze[i][j]==0):
                maze[i][j]=1
            else:maze[i][j]=0
    #绘制路径
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=1, color='red', linewidth=3)
    

    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.axis('on')  # 显示坐标轴

# 提供迷宫的二维数组

def getNab(node,maze):
    ret=list()
    lenx=len(maze)
    leny=len(maze[0])
    if(node[0]>0 and maze[node[0]-1][node[1]]==0):
        ret.append((node[0]-1,node[1]))
    if(node[0]<lenx-1 and maze[node[0]+1][node[1]]==0):
        ret.append((node[0]+1,node[1]))
    if(node[1]>0 and maze[node[0]][node[1]-1]==0):
        ret.append((node[0],node[1]-1))
    if(node[1]<leny-1 and maze[node[0]][node[1]+1]==0):
        ret.append((node[0],node[1]+1))
    return ret

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

def bfs(S,T,maze):
    step=dict()
    fa=dict()
    st=list()
    fa[S]=S
    step[S]=0
    q=queue.Queue()
    q.put(S)
    while(not q.empty()):
        now=q.get()
        st.append(now)
        if(now==T):
            break
        nxt=getNab(now,maze)
        for i in nxt:
            if(not fa.get(i)):
                step[i]=step[now]+1
                fa[i]=now
                q.put(i)
    if(not fa.get(T)):return -1,-1
    ret=list()
    now=T
    while(1):
        ret.append(now)
        if(now==S):
            break
        now=fa[now]
        
    ret.reverse()
    return ret,st

def dij(S,T,maze):
    step=dict()
    fa=dict()
    st=list()
    fa[S]=S
    step[S]=0
    q=queue.PriorityQueue()
    q.put((0,S))
    while(not q.empty()):
        now=q.get()[1]
        st.append(now)
        if(now==T):
            break
        nxt=getNab(now,maze)
        for i in nxt:
            if(not fa.get(i)):
                step[i]=step[now]+1
                fa[i]=now
                q.put((step[i],i))
    if(not fa.get(T)):return -1,-1
    ret=list()
    now=T
    while(1):
        ret.append(now)
        if(now==S):
            break
        now=fa[now]
        
    ret.reverse()
    return ret,st


def dfs(S,T,maze):
    stack=list()
    fa=dict()
    st=list()
    step=dict()
    stack.append(S)
    fa[S]=S
    step[S]=0
    while(not len(stack)==0):
        now=stack.pop()
        st.append(now)
        for i in getNab(now,maze):
            if((not fa.get(i)) or step[i]>step[now]+1):
                fa[i]=now
                step[i]=step[now]+1
                stack.append(i)
                if(i==T):break##!
        if(fa.get(T)):
            st.append(T)
            break##!

    if(not fa.get(T)):
        return -1,-1
    now=T
    ret=list()
    while(1):
        ret.append(now)
        if(now==S):
            break
        now=fa[now]
    ret.reverse()
    return ret,st
def evaluate(now,T):
    return abs(now[0]-T[0])+abs(now[1]-T[1])

def Astar(S,T,maze):
    q=queue.PriorityQueue()
    q.put((0,S))
    fa=dict()
    st=list()
    fa[S]=S
    step=dict()
    step[S]=0
    while(not q.empty()):
        tmp=q.get()
        now=tmp[1]
        st.append(now)
        if(now==T):
            break
        if(tmp[0]>step[now]+evaluate(now,T)):
            continue
        for i in getNab(now,maze):
            if((not fa.get(i))or(step[i]>step[now]+1)):
                step[i]=step[now]+1
                fa[i]=now
                q.put((step[i]+evaluate(i,T),i))
    if(not fa.get(T)):
        return -1,-1
    ret=list()
    now=T
    while(1):
        ret.append(now)
        if(now==S):
            break
        now=fa[now]
    return ret,st

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
                if(random.random()<0.75):
                    st.append(j)
                    tot_st.append(j)
                    maze[j[0]][j[1]]=0
                    for k in getAllNab(j,maze):
                        lock[k[0]][k[1]]+=1


    T=tot_st[int(random.random()*len(tot_st))]

    # tmp=tot_st[0]
    # for i in tot_st:
    #     if(i[0]+i[1]>tmp[0]+tmp[1]):tmp=i
    # while(tmp[0]<len(maze)-1):
    #     tmp=(tmp[0]+1,tmp[1])
    #     maze[tmp[0]][tmp[1]]=0
    # while(tmp[1]<len(maze[0])-1):
    #     tmp=(tmp[0],tmp[1]+1)
    #     maze[tmp[0]][tmp[1]]=0
    # T=tmp
    return maze,T            
def main():
    
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    
    S=(0,0)
    T=(0,3)
    #,T=gen_maze(S,30,30)
    plt.figure(figsize=(len(maze[0])*2, len(maze)/3))
    # T=(len(maze[0])-1,len(maze)-1)
    #T=(4,0)
    path,st = Astar(S,T,maze)
    if(path==-1):
        print("no solution!")
        return
    for i in st:
            maze[i[0]][i[1]]=0.5
    if(path!=-1):
        visualize_maze_with_path(maze, path,st)

    for i in st:
            maze[i[0]][i[1]]=0
    path,st = bfs(S,T,maze)
    for i in st:
            maze[i[0]][i[1]]=0.5
    if(path!=-1):visualize_maze_with_path(maze, path,st)

    for i in st:
            maze[i[0]][i[1]]=0
    path,st = dij(S,T,maze)
    for i in st:
            maze[i[0]][i[1]]=0.5
    if(path!=-1):visualize_maze_with_path(maze, path,st)


    for i in st:
            maze[i[0]][i[1]]=0
    path,st = dfs(S,T,maze)
    for i in st:
            maze[i[0]][i[1]]=0.5
    if(path!=-1):visualize_maze_with_path(maze, path,st)
    plt.show()

if __name__ == '__main__': 
    main()