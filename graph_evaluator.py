import matplotlib.pyplot as plt
import networkx as nx
from scipy import sparse
import numpy as np
import matplotlib.pyplot as plt
def makeGraph(listName, name, xname, yname):
    plt.plot([x for x in range(len(listName))],listName)
    plt.title(name)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.show()

avgDegreeCount = []
edgeCount = []
density = []




dist = []
loader = np.load("250-v4-2444.0.npz")
test_matrix = sparse.csr_matrix((loader['data'], loader['indices'], loader['indptr']),
        shape=loader['shape'])
print(test_matrix.count_nonzero())

cx = sparse.coo_matrix(test_matrix)
G = nx.Graph()
for i, j, v in zip(cx.row, cx.col, cx.data):
    G.add_edge(i, j)

nx.write_edgelist(G, "250-2444"+'.csv', data=False)


'''
from datetime import datetime
from pytz import timezone
tz = timezone('EDT')
print(datetime.now(tz))
'''
