## Estimating the backtracking size

### Introduction

If you are not new to backtracking then you may already know that in some cases, this method can generate an answer quickly and in some other cases take a substantial amount of time. This can be noticeable when finding the cliques in a very big graph with numerous nodes and edges. Instead of leaving our computer running and hoping that it will eventually reach to a solution, it can be helpful to first estimate how long the procedure will take before running the program. This is done by getting an estimation for the size of the the **backtracking tree** (also known as **search tree**).

This is exactly what we will add for our backtracking algorithm that finds all the cliques in a given graph.


### The algorithm

We will refer to the backtracking tree as **|T|**.

To calculate the size of the tree, we choose a random path from the **root** to a **leaf** of the tree and we assume that all nodes have the same degree for all the other possible graphs. Bellow is the pseudo code.

<img src="https://user-images.githubusercontent.com/61196956/171458294-965dbcc4-99eb-44e0-a7e7-6d6556002e08.png" width="750">

Starting from the root, in each step, we enter the cardinality of $C_l$ to variable **c**. Then **c** is then multiplied with **s**, which contains the number of nodes in the current level and the result is written to **s**. We then add **s** to **N**. This way we add the number of nodes which we **assume** exists in the **next layer** of the tree. Since we start from the root, we must initialize **s** with value 1.

$C_0$ is initialized with $V$ (set of nodes) and in every step $X_l$ is chosen randomly ($X_l$ is the next node). $C_{l+1}$ is calculated by using the precomputed $AB$ (similarly to the function **allCliques**). The algorithm stops when $C_l$ becomes equal with the empty set, which means that a leaf was found.

The algorithm is run multiple times and calculate the average in order to get a more accurate result.

### Implementation
The algorithm presented above has been implemented in **Python 3** and is located in the file **src/cliques.py** and specifically in the function **estimateBacktrackSize**. The pseudo code matches the python code and the main difference is the argument **n** which indicates how many times the estimation will be computed in order to get the average as the result.

The following graph is contained in the comments of **cliques.py**

<img src="https://user-images.githubusercontent.com/61196956/194624055-335c66ac-bc8a-4b6c-8ac5-0fd1287f884e.png" width="400">

The backtracking tree for the above graph is the following

<img src="https://user-images.githubusercontent.com/61196956/171458895-3cf67b84-b3c9-4983-8aef-e8e7953d4f30.png" width="800">

The size of the tree is 19 nodes and the function estimates 18.9666 (in an example).




