import random
import time


def createRandomGraph(n, k):

	E = [0]*k # make E global for more effeciency

	def calculate(n, k):
		
		N = (n - 1)*n / 2
		t = 0
		for i in range(1,n+1):
			for j in range(i+1,n+1):
				U = random.uniform(0, 1)
				if (N * U < k):
					E[t]=(i,j)
					k = k - 1
					if(k==0):return E
					t = t + 1
				N = N - 1

	return(calculate(n,k))





'''
##########  EXAMPLE  ############

#### USER INPUT ######
n = 5
k = 4
#####################
t0= time.time()
E = createRandomGraph(n, k)
t1 = time.time() - t0
print("Time elapsed",t1)
print(E)
'''

