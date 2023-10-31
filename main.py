# main.py

from WGraph import WGraph  # Import the WeightedGraph class

import random
districts = [
    "Dedza",
    "Lilongwe",
    "Dowa",
    "Mchinji",
    "Ntcheu",
    "Ntchisi",
    "Kasungu",
    "Salima",
    "Nkhotakota"
]

# Create a weighted graph instance
wg = WGraph()

# Insert each district into the graph
for district in districts:
    wg.insert_node(district)
    
    
# I take this as an example. 
# So using imaginary weights saves me time of creating adges in the nodes
# In the implementation, this could mean getting data from certain source where all the weights are defined

for i in range(len(districts)):
    for j in range(i + 1, len(districts)):
        rw = random.randint(1, 100) #used random library
        wg.insert_edge(districts[i], districts[j], rw)
        
# now lets use dijkstra algorithm to get shortest distance.

start = "Dedza"
end = "Nkhotakota"

shortest_d = wg.dijkstra(start, end)

print(f"Shortest distance from {start} to {end}: {shortest_d}")


