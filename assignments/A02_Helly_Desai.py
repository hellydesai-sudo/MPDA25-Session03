#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes a
G.add_node('node P1')
G.add_node('node P2')

#add nodes b
G.add_node('node S3')
G.add_node('node S4')
G.add_node('node S5')
G.add_node('node S6')

#add nodes c
G.add_node('node7')
G.add_node('node8')
G.add_node('node9')
G.add_node('node10')
G.add_node('node11')
G.add_node('node12')


#add edges
G.add_edge('node P1', 'node P2')
G.add_edge('node P1', 'node S3')
G.add_edge('node P1', 'node S4')
G.add_edge('node P2', 'node S5')
G.add_edge('node P2', 'node S6')
G.add_edge('node P2', 'node7')
G.add_edge('node S3', 'node8')
G.add_edge('node S3', 'node7')
G.add_edge('node S4', 'node S3')
G.add_edge('node S5', 'node9')
G.add_edge('node8', 'node10')
G.add_edge('node11', 'node S5')
G.add_edge('node11', 'node12')


#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Graph', fontsize=12)
nx.draw(G, pos, node_size=1500, with_labels=True, node_color= 'red', font_size=10, font_color='white')



#draw the graph
plt.tight_layout()


#plot
path= r"I:\My Drive\MPDA 2025\Semester 2\04_PYTHON\session02\images\MDPA_plot1.png"
plt.savefig(path, format="PNG")