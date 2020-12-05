# this file is simply for homework 3 for VE444.
# import libs
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def plot_degree_dist(graph):
    degrees = [graph.degree(i) for i in graph.nodes()]
    plt.bar(list(graph.nodes()), degrees)
    plt.title("Degree Distribution")
    plt.savefig("degree-distribution.png")
    plt.close()

# import the data
relations_df = pd.read_table("./Employee_Relationships.txt", sep = "\t")

# simply process the data
friends_df = relations_df[relations_df.iloc[:, 2] > 0].iloc[:, 0:2].drop_duplicates()

# construct the graph
graph = nx.Graph()
graph.add_edges_from(friends_df.values)

# plot the degree distribution
plot_degree_dist(graph)