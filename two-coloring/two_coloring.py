# import libs
import argparse
import pandas as pd
import numpy as np
import networkx as nx
from typing import Literal, Tuple
from tqdm import tqdm

def get_prob_helper(edges: list,
                    color: int,
                    graph: nx.Graph) -> float:
    """..."""
    if len(edges) == 0:
        return 1
    if not graph.edges[edges[0]]['color']:
        return 0.5 * get_prob_helper(edges[1:], color, graph)
    if graph.edges[edges[0]]['color'] != color:
        return 0
    return get_prob_helper(edges[1:], color, graph)


def get_prob(nodes: Tuple[int, int, int, int],
             graph: nx.Graph) -> float:
    """
    :param nodes: the nodes in the k[4]
    :param graph: the graph colored, only color 0 and 1 are allowed,
    :return: the probability of the k[4] being monochromatic
    """
    assert len(nodes) == 4, \
        "nodes should be a tuple of length 4"
    # get the edges in the k[4]
    edges = []
    for i in range(4):
        for j in range(i + 1, 4):
            assert nodes[i] < nodes[j]
            edges.append((nodes[i], nodes[j]))

    return get_prob_helper(edges[1:], graph.edges[edges[0]]['color'], graph)


def get_expectation(graph: nx.Graph,) -> float:
    """
    :param graph: the graph colored, only color 0 and 1 are allowed, 
        uncolored edges are represented by None
    :return: the expectation of monochromatic K[4] (complete graph with 4 vertices) in the graph
    """
    # get the expectation of monochromatic K[4] in the graph
    expectation = 0
    # iterate from all possible k[4] in the graph
    for v1 in range(graph.number_of_nodes()):
        for v2 in range(v1 + 1, graph.number_of_nodes()):
            for v3 in range(v2 + 1, graph.number_of_nodes()):
                for v4 in range(v3 + 1, graph.number_of_nodes()):
                    expectation += get_prob((v1, v2, v3, v4), graph)
    return expectation


def check_monochromatic(nodes: Tuple[int, int, int, int],
                        graph: nx.Graph) -> bool:
    """
    :param nodes: the nodes in the k[4]
    :param graph: the graph colored, only color 0 and 1 are allowed,
    :return: True if the k[4] is monochromatic, False otherwise
    """
    assert len(nodes) == 4, \
        "nodes should be a tuple of length 4"
    # get the edges in the k[4]
    edges = []
    for i in range(4):
        for j in range(i + 1, 4):
            assert nodes[i] < nodes[j]
            edges.append((nodes[i], nodes[j]))

    # check if the k[4] is monochromatic
    color = graph.edges[edges[0]]['color']
    for edge in edges[1:]:
        if graph.edges[edge]['color'] != color:
            return False
    return True


def counting(graph: nx.Graph) -> float:
    """
    :param graph: the graph to be verified
    :return: the number of monochromatic K[4] (complete graph with 4 vertices) in the graph
    """
    num = 0
    # iterate from all possible k[4] in the graph
    for v1 in range(graph.number_of_nodes()):
        for v2 in range(v1 + 1, graph.number_of_nodes()):
            for v3 in range(v2 + 1, graph.number_of_nodes()):
                for v4 in range(v3 + 1, graph.number_of_nodes()):
                    if check_monochromatic((v1, v2, v3, v4), graph):
                        num += 1
    return num


def coloring(graph: nx.Graph) -> nx.Graph:
    """
    :param graph: the graph to be colored, only color 0 and 1 are allowed
    :return: the colored graph
    """
    for edge in tqdm(graph.edges):
        if graph.edges[edge]['color'] is None:
            graph_0 = graph.copy()
            graph_0.edges[edge]['color'] = 0
            graph_1 = graph.copy()
            graph_1.edges[edge]['color'] = 1
            
            # get the expectation of monochromatic K[4] in graph_0 and graph_1
            W_0 = get_expectation(graph_0)
            W_1 = get_expectation(graph_1)
            if W_0 <= W_1:
                graph.edges[edge]['color'] = 0
            else:
                graph.edges[edge]['color'] = 1
        else:
            raise ValueError("Graph is not two-colorable")
    return graph


def init_graph(num_vertices: int) -> nx.Graph:
    """
    :param num_vertices: number of vertices in the graph
    return a complete graph with num_vertices vertices, each edge with color initialized to None
    """
    graph = nx.complete_graph(num_vertices)
    for edge in graph.edges:
        graph.edges[edge]['color'] = None
    return graph


def args_parser():
    """
    return: args containing programs arguments.
    """
    parser = argparse.ArgumentParser(description='two-coloring')
    parser.add_argument("-n", "--num_vertices", type=int, default=20, dest="num_vertices",
                        help="number of vertices")
    # set if using debug mod
    parser.add_argument("-v", "--verbose", action= "store_true", dest= "verbose",
                        help= "enable debug info output")
    args = parser.parse_args()
    return args


def main():
    """main function"""
    # get program arguments
    args = args_parser()

    # initialize graph
    G = init_graph(args.num_vertices)

    # get the colored graph
    G_colored = coloring(G)

    # caculate the monochromatic K[4] in the graph
    num = counting(G_colored)
    print("number of monochromatic K[4] in the graph: {}".format(num))

    assert num <= \
        (args.num_vertices * (args.num_vertices - 1) * (args.num_vertices - 2) * (args.num_vertices - 3)) / 64.


if __name__ == "__main__":
    main()
