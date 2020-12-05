# import libs
import logging
import argparse
import pandas as pd 
import numpy as np # these are two libs for calculation

# set the logger
logging.basicConfig(
                    # filename = "logfile",
                    # filemode = "w+",
                    format='%(name)s %(levelname)s %(message)s',
                    datefmt = "%H:%M:%S",
                    level=logging.DEBUG)
logger = logging.getLogger("hill-climbing")


def greedy_search(edges_df):
    """
    edges_df: the dataframe containing the information about edges, pd.DataFrame.
    return: influential set.
    """
    # get all the sets relationships
    groups = edges_df.groupby(edges_df.columns[1]).groups
    groups = {i: set(edges_df.iloc[groups[i], 0]) for i in groups.keys()}
    # the target set should be influenced
    target = set(edges_df.iloc[:, 0]) 
    # init the influential set and the current influenced set.
    influ_set, current = list(), set()
    while current != target and influ_set != list(groups.keys()):
        size, tmp = len(current), None
        for key in groups.keys():
            if key not in influ_set and size < len(current.union(groups[key])):
                size, tmp = len(current.union(groups[key])), key
        if tmp:
            influ_set.append(tmp)
            current = current.union(groups[tmp])

    return influ_set


def args_parser():
    """
    return: args containing programs arguments.
    """
    parser = argparse.ArgumentParser(description='Hill-Climbing')

    # get edgelists
    parser.add_argument("--edges", type = str, default = "./Employee_Movie_Choices.txt", 
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

    # check the input file format
    try:
        edges_df = pd.read_table(args.edges, sep = "\t")
        logger.debug(edges_df)
        if len(edges_df.columns) != 2 or np.sum(edges_df.isnull().values):
            raise ValueError 
    except:
        logger.warning("""The format of edgelists file is illegal. Plz change to 'int\tint' where two non-zero integer are separated by blankspace in each line
                          indicating there should an edge from first int to second int.
                       """)
        return
    
    # find the influential set
    influ_set = greedy_search(edges_df)

    logger.info("-------------Influence Set--------------")
    logger.info(" \t ".join([str(i) for i in influ_set]) + "\n")

if __name__ == "__main__":
    main()