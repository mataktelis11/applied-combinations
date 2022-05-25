import networkx as nx
import random


def findAllCliques(graph):

	global AB, X, C, G


	def setup(graph):
		global G, X, C, AB
		
		AB = [0] # first is dummy
		G = graph
		C = [set()] * (G.number_of_nodes()-1)		# use set instead of list
		X = [0] * (G.number_of_nodes())

		for i in range(1, G.number_of_nodes() + 1):
			AB.append(list(G.neighbors(i)))

		for i in range(1, G.number_of_nodes() + 1):
			for j in range(len(AB[i]) - 1, -1, -1):
				if (AB[i][j] <= i):
					AB[i].pop(j)
		# print(i, AB[i])


	def allCliques(l):
		global C, X
		
		if(l==0):
			print("[]")
		else:
			print(X[:l])

		if (l == 0):
			C[0] = set(list(G.nodes()).copy())
		else:

			C[l] = C[l - 1].intersection(set(AB[X[l-1]]))

		for x in C[l]:
			X[l] = x
			allCliques(l + 1)
			


	def estimateBacktrackSize(n):
		global C, X

		sum = 0
		n = 30
		for i in range(n):
			s = 1
			N = 1
			l = 0
			C[0] = set(list(G.nodes()).copy())

			while(len(C[l])!=0):

				c = len(C[l])

				s = c * s

				N = N + s

				X[l] = random.choice(list(C[l]))

				C[l + 1] = C[l].intersection(set(AB[X[l]]))

				l = l + 1

			sum += N
		return sum/n
	

	setup(graph)

	print("Average size of backtracking tree is:")
	print(estimateBacktrackSize(30))

	print("All cliques are:")
	allCliques(0)


'''
#####  EXAMPLE  #######
G = nx.Graph()
G.add_nodes_from(list(range(1, 8)))
G.add_edges_from([(1, 2), (1, 7), (2, 7), (7, 6), (6, 2), (2, 3), (3, 4), (4, 5), (5, 3)])

findAllCliques(G)
########################
'''

