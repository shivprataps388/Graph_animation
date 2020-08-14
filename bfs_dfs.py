import main
import gui
import time
import queue
search = []
class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices                        
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]        
    def getMinimumKey(self, weight, visited):        
        min = 9999
        for i in range(self.vertices):            
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i        
        return minIndex
    def primsAlgo(self):
        weight = [9999] * self.vertices     
        MST = [None] * self.vertices        
        weight[0] = 0                       
        visited = [False] * self.vertices
        MST[0] = -1                                 
        for _ in range(self.vertices):
            minIndex = self.getMinimumKey(weight, visited)           
            visited[minIndex] = True
            for vertex in range(self.vertices):
                if self.graph[minIndex][vertex] > 0 and visited[vertex] == False and \
                weight[vertex] > self.graph[minIndex][vertex]:
                    weight[vertex] = self.graph[minIndex][vertex]
                    MST[vertex] = minIndex
        self.printMST(MST)
    def printMST(self, MST):
        total_weight=0
        for i in range(1, self.vertices):
            #print (MST[i],"-",i,"\t",self.graph[i][ MST[i] ])
            time.sleep(1)
            total_weight+=self.graph[i][ MST[i] ]
            gui.canvas.create_line(gui.x_matrix[MST[i]],gui.y_matrix[MST[i]], gui.x_matrix[i], gui.y_matrix[i], fill="orange",tag=str("c_line"+str(i)))
        print("total_weight is",total_weight)
def MST(v):
    if (gui.t!=0):
        for i in range(0,len(main.adjacency_matrix)):
            for j in range(i,len(main.adjacency_matrix[i])):
                if (main.adjacency_matrix[i][j]==1):
                    print("assign weight to edge",i+1,"to",j+1)
                    temp=int(input())
                    off_y=(gui.y_matrix[j]-gui.y_matrix[i])/2
                    off_x=(gui.x_matrix[j]-gui.x_matrix[i])/2
                    gui.canvas.create_text(gui.x_matrix[i]+off_x,gui.y_matrix[i]+off_y,text=str(temp),font="Times 20 italic bold")
                    
                    main.adjacency_matrix[i][j]=temp
                    main.adjacency_matrix[j][i]=temp
    
    g  = Graph(len(main.adjacency_matrix))
    g.graph=[]
    g.graph.extend(main.adjacency_matrix)
    g.primsAlgo()
    print("how many weights you want to change ?")
    z=int(input())
    if (z>0):
        for i in range(0,z):
            print("Type the edge of which you want to change weight in fromat ->","e1 e2 w")
            s=list(map(int,input().split()))
            main.adjacency_matrix[s[0]-1][s[1]-1]=s[2]
            gui.canvas.delete("all")
            #print(gui.x_matrix)
            #print(gui.y_matrix)
            tag_name=str(s[0]-1)+str(s[1]-1)
            gui.canvas.delete(tag_name)
            gui.plot(main.adjacency_matrix)

parent=[]   
dfs_num=0
hold=0
def DFS(x):
    global parent
    global dfs_num
    #print(main.adjacency_matrix)
    parent=[-1]*len(search)
    DFSUtil(x)
    for i in range(0,len(search)):
        if search[i]!=1:
            time.sleep(1)
            DFSUtil(i)

    dfs_num=0
    

def DFSUtil(v):
    global dfs_num
    global parent
    hold=v
    dfs_num+=1
    gui.FillOval_d(dfs_num,v)
    gui.FillOval(v,"yellow")
    search[v] = 1
    for i in range(0, len(main.adjacency_matrix)):
        #print(parent)
        if(main.adjacency_matrix[v][i] == 1 and search[i] != 1): 
            time.sleep(1)
            gui.canvas.create_line(gui.x_matrix[hold],gui.y_matrix[hold],gui.x_matrix[i],gui.y_matrix[i],fill="#fb0")
            parent[i]=v
            DFSUtil(i)
        elif(main.adjacency_matrix[v][i] == 1 and search[i] == 1):
            if (parent[hold]!=i):
                time.sleep(1)
                gui.canvas.create_line(gui.x_matrix[hold],gui.y_matrix[hold],gui.x_matrix[i],gui.y_matrix[i],fill="red")
    dfs_num+=1
    gui.FillOval_d_e(dfs_num,v)

q = queue.Queue()
def BFS(v):
    BFSUtil(v)
    for i in range(0,len(search)):
        if search[i]!=1:
            BFSUtil(i)
def BFSUtil(v):
    parent=[-1]*len(search)
    q.put(v)
    gui.FillOval(v,"#0d61e8") 
    search[v] = 1
    time.sleep(1)
    while(not q.empty()):
        v = q.get()
        gui.FillOval(v,"#0d61e8")
        time.sleep(1)
        hold=v
        for i in range(0, len(main.adjacency_matrix)):
            if(main.adjacency_matrix[v][i] == 1 and search[i] != 1):
                search[i]=1
                gui.canvas.create_line(gui.x_matrix[hold],gui.y_matrix[hold],gui.x_matrix[i],gui.y_matrix[i],fill="#fb0")
                time.sleep(0.5)
                gui.FillOval(i, "#b4f7f2")
                q.put(i)
                parent[i]=v
                time.sleep(0.5)
            elif(main.adjacency_matrix[v][i] == 1 and search[i] == 1):
                if (parent[hold]!=i):
                    time.sleep(1)
                    gui.canvas.create_line(gui.x_matrix[hold],gui.y_matrix[hold],gui.x_matrix[i],gui.y_matrix[i],fill="red")
        search[v] = 1