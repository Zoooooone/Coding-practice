import matplotlib.pyplot as plt
import memory_profiler
from time import time
from knapsack import Knapsack


def time_plot(weight, step):
    time_costs = []
    weights = [x for x in range(1, weight, step)]
    v = [i for i in range(weight // 2)]
    w = v
    
    for wi in range(1, weight, step):
        knapsack = Knapsack(w, v, [], wi)
        start = time()
        knapsack.knapsack_01()
        end = time()
        time_costs.append(end - start)

    plt.plot(weights, time_costs)
    plt.xlabel("weight")
    plt.ylabel("time")


def space_plot(weight, step): 
    space_costs = []
    weights = [x for x in range(1, weight, step)]
    v = [i for i in range(weight // 2)]
    w = v
    
    for wi in range(1, weight, step):
        knapsack = Knapsack(w, v, [], wi)
        
        @memory_profiler.profile
        def profiled_function():
            knapsack.knapsack_01()

        profiled_function()
        space_costs.append(max(memory_profiler.memory_usage()))

    plt.plot(weights, space_costs)
    plt.xlabel("weight")
    plt.ylabel("memory")


if __name__ == "__main__": 
    time_plot(1000, 5)
    plt.savefig("algorithm/knapsack/time_plot.png")
    plt.clf()
    space_plot(400, 2)
    plt.savefig("algorithm/knapsack/space_plot.png")
