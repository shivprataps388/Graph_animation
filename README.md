How to run program-

1.All 3 files named as "" must be in same folder.
2.Open command prompt.
3.Change directory path to Folder in which files are saved.
4.Type "python main.py"
(Required library is Tkinter) 
It will generate a deefault graph with weight assigned to it.
We can perform BFS/DFS/MST with the help of buttons below the graph.


RESET button-

If you press this button.Prompt will ask if you want to create new graph or not.
	type 0 for regenarting default graph
	type 1 for entering new graph


How to enter a user input graph-

When you press RESET button it will ask if you want to enter new graph.

1.Change mode button will be besides MST button where you can switch between "create node" mode and "connect" mode.
2.In "create node mode" left click of mouse will create node.
3.In "connect mode",left click on one node and the left click on other node to connect two nodes.

!!!Do not create node in "connect mode" it will give errors.


Performing DFS on DEFAULT graph-

1.It will ask if you want to input the starting vertex(in command prompt).
	type 1 for user input and then give user input
	type 0 for default starting vertex
2.It will perform DFS and show starting and finishing time on each node along direction of ORANGE edge.
3.Tree edge will be represented by ORNAGE color and back edge will be represented by RED color.


Performing BFS on DEFAULT graph-

1.It will ask if you want to input the starting vertex(in command prompt).
	type 1 for user input
	type 0 for default
2.It will perform BFS.Nodes with LIGHT BLUE color means entered in queue 
and nodes with DARK BLUE color means popped out from queue.
3.Nodes will be traversed along ORANGE edge and RED edge means cross edge.


Performing MST on DEFAULT graph-

1.If you press MST button.It will start performing MST algorithm.
2.ORANGE edges will be tree edges.
3.Then it will ask you "How many edge weights you want to change?" in (command prompt)
	enter 0 means you dont want to change edge weights.
	any positive number means you have to change that number of edges.
	egdes will be given input as "e1 e2 w" 
	example-"1 2 3" means change weight of edge connecting vertices 1 and 2 to 3.
   !!!You cannot enter a new edge here.For that new graph needs to be created.
4.After you have entered new edge weights you can perform MST again.
5.Command prompt will print total edge weights in last.


DFS/BFS on USER INPUT GRAPH-
In this you will have to give starting vertex as input.
Rest is same as for default graph.

MST on USER INPUT GRAPH-
1.Edge weights have to be assigned from command prompt.
2.Edges will be printed,you just have to type weights and press enter.
3.When input is complete,it will perform MST(ORANGE edges will be tree edges)
4.Once it is finished you can change the edge weights as for default graph and rest everything is same as deault graph.

