# import libs
import logging
import argparse
import pandas as pd 
import numpy as np
from pandas.core.algorithms import rank # these are two libs for calculation

# set the logger
logging.basicConfig(
                    # filename = "logfile",
                    # filemode = "w+",
                    format='%(name)s %(levelname)s %(message)s',
                    datefmt = "%H:%M:%S",
                    level=logging.DEBUG)
logger = logging.getLogger("pagerank")


def pagerank(adj_mat, beta, epsilon, max_itr):
    """
    adj_mat: the adjacency matrix which represents the graph.
    beta: random teleport probability.
    epsilon: convergence epsilon.
    max_itr: the maximum iterations.
    return: rank_lst, a list containing the rank score for each node in the graph, list;
    """
    # number of nodes 
    num_of_nodes = adj_mat.shape[0]
    # create the stochastic matrix=
    M_mat = np.transpose(adj_mat)
    # find the dead ends
    dead_ends = np.where(np.sum(M_mat, axis = 0) == 0)[0]
    # solution to dead ends
    if dead_ends:
        M_mat[:, dead_ends] = 1
    M_mat = M_mat / np.sum(M_mat, axis = 0)
    # solution to spider traps
    A_mat = beta * M_mat + (1 - beta) * (np.ones(M_mat.shape) / num_of_nodes)
    # init the rank_lst
    rank_lst = np.ones((num_of_nodes, 1)) / num_of_nodes
    # constantly updating rank_lst
    for i in range(max_itr):
        new_rank_lst = np.dot(A_mat, rank_lst)
        if np.linalg.norm(rank_lst - new_rank_lst) > epsilon:
            rank_lst = new_rank_lst
        else:
            break
    return rank_lst



def adjacency_mat(filepath):
    """
    filepath: the file path of edgelists file.
    return: adj_mat, the adjacency matrix created from edges, 2-d np.array; 
    """
    # get edges from reading file
    edges_df = pd.read_table(filepath, header = None, sep = " ") 
    # get the number of nodes
    num_of_nodes = np.max(edges_df.values) 
    # init adjacency matrix 
    adj_mat = np.zeros((num_of_nodes, num_of_nodes))
    for i, j in edges_df.values:
        adj_mat[i - 1, j - 1] = 1
    
    return adj_mat


def args_parser():
    """
    return: args containing programs arguments.
    """
    parser = argparse.ArgumentParser(description='PageRank')
    # set the random teleport probability
    parser.add_argument("--beta", type = float, default = 0.85, 
                        help= "random teleport probability")
    
    # set the convergence epsilon
    parser.add_argument("--epsilon", type = float, default = 0.001, 
                        help= "convergence epsilon")

    # set the maximum iterations
    parser.add_argument("--max_itr", type = int, default = 500, 
                        help= "the maximum iterations when updating the ranks")

    # get edgelists
    parser.add_argument("--edges", type = str, default = "./edgelists.txt", 
                        help= "path for edgelists file")

    # set if using debug mod
    parser.add_argument("-v", "--verbose", action= "store_true", dest= "verbose", 
                        help= "enable debug info output")

    args = parser.parse_args()
    return args


def main():
    # get program arguments 
    args = args_parser()

    # set the logger
    logger.setLevel(logging.DEBUG)
    if not args.verbose:
        logger.setLevel(logging.INFO)
    logger.debug("--------DEBUG enviroment start---------")

    adj_mat = adjacency_mat(args.edges)

    logger.info("------------Adjacency Matrix------------")
    logger.info("\n" + str(adj_mat))

    rank_lst = pagerank(adj_mat, args.beta, args.epsilon, args.max_itr)

    logger.info("------------PageRank Score-------------")
    for i, rank in enumerate(rank_lst):
        logger.info(str(i + 1) + "\t" + str(rank))
    logger.info("-------------Process Ends--------------")

if __name__ == "__main__":
    main()