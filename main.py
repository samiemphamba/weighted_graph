# main.py

from weighted_graph import WGraph  # Import the WeightedGraph class


districts = [
    "Lilongwe",
    "Dowa",
    "Mchinji",
    "Ntcheu",
    "Dedza",
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

