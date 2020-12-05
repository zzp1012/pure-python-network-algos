# import libs
import os
import logging
import argparse
import matplotlib.pyplot as plt # these are two libs for calculation

# set the logger
logging.basicConfig(
                    # filename = "logfile",
                    # filemode = "w+",
                    format='%(name)s %(levelname)s %(message)s',
                    datefmt = "%H:%M:%S",
                    level=logging.INFO)
logger = logging.getLogger("SIR-model")


def simulate_SIR(args):
    """
    args: the args containing all program arguments.
    effect: a plot of the simulation of the SIR model.
    """
    # init
    S, I, R  = [(args.total - args.recovery - args.infected) / args.total], [args.infected / args.total], [args.recovery / args.total]
    while I[-1] > 1e-10:
        # solve the S, I, R for each iteration
        dS = - args.beta * S[-1] * I[-1]
        dR = args.delta * I[-1]
        dI = 0 - dS - dR
        S.append(S[-1] + dS)
        R.append(R[-1] + dR)
        I.append(I[-1] + dI)
        if S[-1] < 0:
            S[-1] = 0 # recorrect the value of S
        if I[-1] < 0:
            I[-1] = 0 # recorrect the value of I
        logger.debug("The iteration: " + str(len(S)) + " Current I: " + str(I[-1]))
    
    # plot the figure
    plt.figure()
    days = list(range(len(S) + 1))[1:] 
    plt.plot(days, S, label = "S")
    plt.plot(days, I, label = "I")
    plt.plot(days, R, label = "R")
    plt.xlabel("days") 
    plt.ylabel("Relative group size (\%)")
    plt.title("Total Population = " + str(args.total) + ", R_0 = " + str(args.recovery) + ", I_0 = " + str(args.infected) + ", Beta = " + str(args.beta) + ", delta = " + str(args.delta))
    plt.suptitle("SIR Model Simulation")
    plt.legend(loc = "best")       
    plt.savefig(os.path.join(args.path, "SIR-simulation.png"))
    plt.close()

def args_parser():
    """
    return: args containing programs arguments.
    """
    parser = argparse.ArgumentParser(description='SIR-Model')

    # set the transmission rate
    parser.add_argument("--beta", type = float, default = 0.2, 
                        help= "the transmission rate")

    # set the recovery rate
    parser.add_argument("--delta", type = float, default = 0.1, 
                        help= "the recovery rate")

    # set the total population
    parser.add_argument("--total", type = int, default = 1000, 
                        help= "the total population")

    # set the initial recovery group size
    parser.add_argument("--recovery", type = int, default = 0, 
                        help= "the initial recovery group size")

    # set the initial infected group size
    parser.add_argument("--infected", type = int, default = 1, 
                        help= "the initial infected group size")

    # set the save path for the fig
    parser.add_argument("--path", type = str, default = "./", 
                        help= "the save path for the fig")

    # set if using debug mod
    parser.add_argument("-v", "--verbose", action= "store_true", dest= "verbose", 
                        help= "enable debug info output")

    args = parser.parse_args()

    if args.beta > 1 or args.beta < 0:
        logger.warning("The value for transmission rate is illegal. Turn to default 0.2")
        args.beta = 0.2
    
    if args.delta > 1 or args.delta < 0:
        logger.warning("The value for recovery rate is illegal. Turn to default 0.1")
        args.delta = 0.1

    if args.recovery < 0:
        logger.warning("The value for initial recovery group size is illegal. Turn to default 0")
        args.recovery = 0

    if args.infected < 0:
        logger.warning("The value for initial infected group size is illegal. Turn to default 1")
        args.infected = 1

    if args.total < args.infected + args.recovery:
        logger.warning("The value for total population is illegal. Turn to default 1000")
        args.total = 1000

    return args


def main():
    # get program arguments 
    args = args_parser()

    # set the logger
    logger.setLevel(logging.DEBUG)
    if not args.verbose:
        logger.setLevel(logging.INFO)
    logger.debug("--------DEBUG enviroment start---------")

    # simulation
    simulate_SIR(args)

if __name__ == "__main__":
    main()