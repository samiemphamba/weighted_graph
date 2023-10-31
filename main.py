from WGraph import WGraph  # Import the WGraph class
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
    
# I take this as an example.So using imaginary weights saves me time of creating adges in the nodes. In the implementation, this could mean getting data from certain source where all the weights are defined
# wg.insert_edge("Dedza", "Nkhotakota", 2000)
for i in range(len(districts)):
    for j in range(i + 1, len(districts)): # it checks if an edge between node1 and node2 already exists 
        rw = random.randint(100, 400) 
        wg.insert_edge(districts[i], districts[j], rw)
        
# now lets use dijkstra algorithm to get shortest distance.
start = "Dedza"
end = "Nkhotakota"

shortest_d = wg.dijkstra(start, end)
shortest_path, path_code = wg.dijkstra(start, end)

print("********************  THESE WEIGHTS ARE PURELY IMAGINARY AND GENERATED USING THE RANDOM LIBRARY ********************************")
print(f"Shortest path from {start} to {end}: {shortest_path}")
print(f"Total distance: {path_code}")
print("*********************** END OF OUTPUT ******************************************************************************************")

