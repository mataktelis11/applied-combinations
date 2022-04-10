# Applied Combinatorics Project - Summer 2021
This project was made for an exam for the lesson Applied Combinatorics, in University of Piraeus IT department.
A detailed documentation is provided in Greek (.pdf).

## Generating a random undirected graph

The first algorithm creates a *random undirected graph* of *n* nodes and *k* edges.

We define the graph as $G = (V,E)$, where $V = \{1,2, \dots, n\}$ and $|E| = k$. $E$ is the a set that contains pairs of nodes. It is known that a graph can have a maximum of $N = \binom{n}{2}$ nodes.

We just need an algorithm that iterates through all the possible edges and
randomly selects some of them, until exactly $k$ edges are selected.

The following is the pseudo code of the algorithm given as an answer.


The function assumes that $k \le \binom{n}{2}$.

First the $N$ is calculated. Simple find the binomial coefficient:

$$N = \binom{n}{2} = \frac{n!}{2!(n-2)!} = \frac{(n-1)n}{2}$$

and that explains line 2 in the pseudo code.