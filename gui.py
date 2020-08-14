import main
import tkinter
import threading
t=0
import bfs_dfs
window=tkinter.Tk()
window.title("BFS/DFS/MST GUI")
window.geometry("800x600")
window.resizable(False, False)
canvas = tkinter.Canvas(window, relief="solid", bd=2, width=800, height=550)
canvas.pack()
btnFrame = tkinter.Frame(window, relief="solid", width="800", height="25")
btnFrame.pack()
textFrame = tkinter.Frame(window, relief="solid", width="800", height="25")
textFrame.pack()
ModeLabel = tkinter.Label(textFrame, text="Current Mode: "+'Create Node Mode')
ModeLabel.pack(side="right", padx=50)
x_matrix=[]
y_matrix=[]
oval=[]
def create_default():
    global x_matrix,y_matrix,oval
    x_matrix = [289, 490, 434, 538, 337, 245] 
    y_matrix = [427, 447, 272, 131, 106, 209]
    main.adjacency_matrix=[[0, 1, 9, 0, 0, 14],
                            [1, 0, 10, 15, 0, 0],
                            [9, 10, 0, 11, 0, 2],
                            [0, 15, 11, 0, 6, 0],
                            [0, 0, 0, 6, 0, 9],
                            [14, 0, 2, 0, 9, 0]]
    for i in range(0,len(main.adjacency_matrix)):
        oval.append(0)
        oval[-1]=canvas.create_oval(x_matrix[i]-20, y_matrix[i]-20, x_matrix[i]+20, y_matrix[i]+20, fill="white", width=1,tags=("Node",i+1))
        canvas.create_text((x_matrix[i], y_matrix[i]), text=str(i+1), tags=("Node",i),font="Times 20 italic bold")
        for j in range(0,len(main.adjacency_matrix)):
            for k in range(j,len(main.adjacency_matrix[j])):
                if (main.adjacency_matrix[j][k]!=0):
                    off_y=(y_matrix[k]-y_matrix[j])/2
                    off_x=(x_matrix[k]-x_matrix[j])/2
                    canvas.create_text(x_matrix[j]+off_x,y_matrix[j]+off_y,text=str(main.adjacency_matrix[j][k]),font="Times 20 italic bold")
                    canvas.create_line(x_matrix[j],y_matrix[j], x_matrix[k], y_matrix[k], fill="black")
if (t==0):
    create_default()
Line1 = None
Line2 = None
def plot(v):
    for i in range(0,len(main.adjacency_matrix)):
        canvas.create_oval(x_matrix[i]-20, y_matrix[i]-20, x_matrix[i]+20, y_matrix[i]+20, fill="white", width=1,tags=("Node",i+1))
        canvas.create_text((x_matrix[i], y_matrix[i]), text=str(i+1), tags=("Node",i),font="Times 20 italic bold")
        for j in range(0,len(main.adjacency_matrix)):
            for k in range(j,len(main.adjacency_matrix[j])):
                if (main.adjacency_matrix[j][k]!=0):
                    off_y=(y_matrix[k]-y_matrix[j])/2
                    off_x=(x_matrix[k]-x_matrix[j])/2
                    canvas.create_text(x_matrix[j]+off_x,y_matrix[j]+off_y,text=str(main.adjacency_matrix[j][k]),font="Times 20 italic bold")
                    canvas.create_line(x_matrix[j],y_matrix[j], x_matrix[k], y_matrix[k], fill="black")
        
CreateMode = True
LineMode = False

def ChangeMode():
    global CreateMode
    global LineMode
    if(not CreateMode):
        CreateMode = True
        LineMode = False
        CurrentMode = 'Create Node Mode'
    elif(not LineMode):
        LineMode = True
        CreateMode = False
        CurrentMode = 'Connect Mode'
    global ModeLabel
    ModeLabel.config(text="Current Mode: "+CurrentMode)
    ModeLabel.pack(side="right", padx=50)

def mouseClick(event):
    x = event.x
    y = event.y
    if(CreateMode):
        x_matrix.append(x)
        y_matrix.append(y)
        oval.append(0)
        bfs_dfs.search.append(0)
        main.adjacency_matrix.append([])
        adj_qty = len(main.adjacency_matrix)
        main.adjacency_matrix = [[0] * adj_qty for i in range(adj_qty)]
        i = len(oval)-1
        oval[i]=canvas.create_oval(x_matrix[i]-20, y_matrix[i]-20, x_matrix[i]+20, y_matrix[i]+20, fill="white", width=1, tags=("Node",i))
        canvas.create_text((x_matrix[i], y_matrix[i]), text=str(i+1), tags=("Node",i),font="Times 20 italic bold")
       
    if(LineMode):
        item = canvas.find_closest(x,y)
        tags = canvas.gettags(item)

        global Line1
        global Line2
        
        if(tags[0] == "Node"):
            if(Line1 is None):
                Line1 = int(tags[1])
               
            else:
                Line2 = int(tags[1])
                if(Line1 != Line2):
                    main.adjacency_matrix[Line1][Line2] = 1
                    main.adjacency_matrix[Line2][Line1] = 1
                    canvas.create_line(x_matrix[Line1],y_matrix[Line1], x_matrix[Line2], y_matrix[Line2], fill="black")
                Line1 = None
        


def FillOval(v, color):
    canvas.itemconfig(oval[v], fill=color)
def FillOval_d(number,v):
   number="S  "+str(number)
   canvas.create_oval(x_matrix[v]+30-20, y_matrix[v]-40, x_matrix[v]+30+20, y_matrix[v]+40, fill="white", width=1)
   canvas.create_text(x_matrix[v]+30, y_matrix[v], text=(number))
def FillOval_d_e(number,v):
   number="E  "+str(number)
   canvas.create_text(x_matrix[v]+30, y_matrix[v]+20, text=str(number))
    
def reset():
    global x_matrix
    global y_matrix
    global oval
    global t
    x_matrix = []
    y_matrix = []
    oval = []
    bfs_dfs.search = []
    main.adjacency_matrix = []
    canvas.delete("all")
    print("You want to enter the graph?")
    print("Type 1 to enter manually else type 0")
    t=int(input())
    if (t==0):
        create_default()

def recieveBtn(_type):
    if(_type == 'DFS'):
        if (t==0):
            main.adjacency_matrix=[[0,1,1,0,0,1],[1,0,1,1,0,0],[1,1,0,1,0,1],[0,1,1,0,1,0],[0,0,0,1,0,1],[1,0,1,0,1,0]]
            bfs_dfs.search=[0]*6
            print("Do you want to enter starting vertex?")
            z=int(input())
            if (z==0):
                ver=1
            elif(z==1):
                print("input starting vertex")
                ver=int(input())
        else:
            print("input starting vertex")
            ver=int(input())
        th = threading.Thread(target=bfs_dfs.DFS, args=(ver-1,))
        th.start()
    if(_type == 'BFS'):
        if (t==0):
            main.adjacency_matrix=[[0,1,1,0,0,1],[1,0,1,1,0,0],[1,1,0,1,0,1],[0,1,1,0,1,0],[0,0,0,1,0,1],[1,0,1,0,1,0]]
            bfs_dfs.search=[0]*6
            print("Do you want to enter starting vertex?")
            z=int(input())
            if (z==0):
                ver=1
            elif(z==1):
                print("input starting vertex")
                ver=int(input())
        else:
            print("input starting vertex")
            ver=int(input())
        th = threading.Thread(target=bfs_dfs.BFS, args=(ver-1,))
        th.start()
    if(_type == 'MST'):
        th = threading.Thread(target=bfs_dfs.MST, args=(0,))
        th.start()
        

def run():
    button1 = tkinter.Button(btnFrame, overrelief="solid", text="Run - DFS", width=15, command=lambda: recieveBtn('DFS'))
    button2 = tkinter.Button(btnFrame, overrelief="solid", text="Run - BFS", width=15, command=lambda: recieveBtn('BFS'))
    button3 = tkinter.Button(btnFrame, overrelief="solid", text="RESET", width=15, command=lambda: reset())
    button5 = tkinter.Button(btnFrame, overrelief="solid", text="ChangeMode", width=15, command=lambda: ChangeMode())
    button6=tkinter.Button(btnFrame, overrelief="solid", text="MST", width=15, command=lambda: recieveBtn('MST'))
    button1.pack(side="left", padx = 10)
    button2.pack(side="left", padx = 10)
    button3.pack(side="left", padx = 10)
    button6.pack(side="left", padx = 10)
    button5.pack(side="left", padx = 15)
    canvas.bind("<Button-1>", mouseClick)
    #canvasWindow(window)

    window.mainloop()