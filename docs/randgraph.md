## Generating a random undirected graph

### The algorithm

The first algorithm creates a **random undirected graph** of $n$ nodes and $k$ edges.

We define the graph as $G = (V,E)$, where $V = {1,2, . . . , n}$ and $|E| = k$. $E$ is the a set that contains pairs of nodes. It is known that a graph can have a maximum of $N = \binom{n}{2}$ nodes.

We just need an algorithm that iterates through all the possible edges and randomly selects some of them, until exactly $k$ edges are selected.

The following is the pseudo code of the algorithm given as an answer.

<img src="https://user-images.githubusercontent.com/61196956/162618576-91c2fcd1-2dc2-41b6-b143-8d05dab49f15.png" width="800">

We define a function that takes $n$ and $k$ as arguments and returns $E$. The function assumes that $k \le \binom{n}{2}$. 

First the $N$ is calculated. Simple find the binomial coefficient:

$$N = \binom{n}{2} = \frac{n!}{2!(n-2)!} = \frac{(n-1)n}{2}$$

and that explains line 2 in the pseudo code.

Then a double for loop starts which produces virtually all the edges in pairs of vertices **(i, j)** in lexicographical order. Before the loops, we define the local variable **t** in line 3, with initial value 0. Every time an iterated edge is selected to be added to the graph, it is written in **E[t]** and then the variable **t** increases by 1.

To decide whether or not to include a node in the graph, do the following
procedure:

first call the rand function to generate a random value from **[0, 1)** and store it in **U**. Then check if **U** is less than **k/N** (see image below).

<img src="https://user-images.githubusercontent.com/61196956/162618459-449f9c4d-435e-4c82-9fae-64f918b5cf92.png" width="250">

The probability that **U** is in the interval **[0, k/N]** is **k/N**. Then **E[t]** gets the edge **(i, j)**, **k** is reduced by 1 (because the elements that remain to be filled are reduced by 1) and **t** increases by 1 (as explained before).

Then **N** decreases by 1, regardless of whether or not the condition was satisfied, which means that there are 1 less edges to select from.

Once k becomes 0, the algorithm stops (returns E immediately). There is a case,that at some point N becomes equal to k. When this equality is valid, in the if statement of line 7, we will essentially have  **U < 1**, and this is always true, which means that the edge will always be selected.

In practice this means that if the remaining edges are equal in number to
the edges that must be contained in E, then all must be chosen necessarily.

This ensures that the algorithm always provides a valid solution.

### The implementation

The above algorithm is located in the file **src/randgraph.py**. The **createRandomGraph** function contains the actual algorithm. Notice that **E** is not actually global. This was done to make the code easier to be imported into another **.py** script.

At the end of the file there is block comment with an example. Feel free to uncomment it and test it yourself. Here is an example output:

```
$ python3 randgraph.py 
Time elapsed 1.2120999599574134e-05
[(1, 4), (2, 3), (2, 4), (3, 4)]
$ 
```