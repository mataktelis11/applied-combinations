## Estimating the backtracking size

### Introduction

If you are not new to backtracking then you may already know that in some cases, this method can generate an answer quickly and in some other cases take a substantial amount of time. This can be noticeable when finding the cliques in a very big graph with numerous nodes and edges. Instead of leaving our computer running and hoping that it will eventually reach to a solution, it can be helpful to first estimate how long the procedure will take before running the program. This is done by getting an estimation for the size of the the **backtracking tree** (also known as **search tree**).

This is exactly what we will add for our backtracking algorithm that finds all the cliques in a given graph.


### The algorithm

We will refer to the backtracking tree as **|T|**.

To calculate the size of the tree, we choose a random path from the **root** to a **leaf** of the tree and we assume that all nodes have the same degree for all the other possible graphs.


### Implementation



