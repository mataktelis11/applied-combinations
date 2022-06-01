## Finding all the Cliques of an undirected graph with Backtracking

### What are cliques?
A clique is a subset of vertices of an undirected graph, such that every two distinct vertices in the clique are adjacent. We can conclude that a clique of a graph G, is actually a subgraph of G that is a **complete** graph.

Finding all the cliques in a graph is a difficult (NP-complete problem). The algorithm presented here utilizes backtracking and is based on [this](https://www.site.uottawa.ca/~lucia/courses/5165-10/Backtracking.pdf) excellent presentation.

### The algorithm

Finding all the clicks of a graph is done through backtracking. When the algorithm finds a clique, it is stored in a table X = [x_0, x_1, · · ·, x_l−1].
 
In order for the algorithm not to give the same clique many times in different order, e.g. [0, 1, 6] and [1, 0, 6], answers are required in order: x 0 < x_1 < x_2 < · · · < x_l−1.

In backtracking we define C_l as the set of possible options x_l can get before entering the table X = [x_0, x_1, · · ·, x_l−1].

C_l can be calculated as follows:

- if l=0 C_0 is V 

- if l>0 C_l can be calculated as:

first let the following sets:

A_u = u \in V : u,v \in E meaning the set of nodes adjacent to u

B_u = u+1, u+2, ...,n-1 meaning the set of nodes bigger than u

We can now state that C_l = A_{x_{l-1}} ^ B_{x_{l-1}} ^ C_{l-1}

The sets A and B can be calculated before the algorithm starts, and will be uses as AB = A ^ B.

Below is the backtracking algorithm for finding the cliques. It used by calling AllCliques(0).

<img src="https://user-images.githubusercontent.com/61196956/170009154-7d41514b-1e8e-4c0d-8313-6c1b82b8c216.png" width="750">



### The implementation
The algorithm presented above has been implemented in **Python 3** and is located in the file **src/cliques.py**

There is a function inside of which the global variables are defined for the rest of the functions. This is was decided to make the program easily importable to other scripts without worrying about the globals. If you come up with a better approach, feel free to submit a Pull Request.

The library **networkx** is used in this file to represent the graphs.

The function **setup** is used to initialize the global variables. The main goal is to calculate AB which is A ^ B.

Next is the function **allCliques** which implements the backtracking algorithm presented in the pseudocode.

We also have the function **estimateBacktrackSize** , which will be discussed in a later section ([here](./backtrackingsize.md)).

There is a test example in the comments at the end of the file. In this example, a networkx graph is created and it is the following:



The function **findAllCliques** is called on this Graph and all the cliques will be found. When a clique is found, it is simply printed to the terminal.

