import matplotlib.pyplot as plt
import random as rnd
from functools import reduce
import math
import concurrent.futures as future
from time import perf_counter as pc
# MA4 1.2


def num_of_points_in_sphere(points):
    # Assumes radius 1
    # A bit messy but nice line which uses almost all requested features (filter, reduce, map) :)
    return len(list(filter(lambda lst: reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, lst))) <= 1, points)))
    # Filter all points which sum of list of squared coordinates are less than 1, return number of points in sphere


def parallel_monte_carlo_approx(no_processes, n, dim):
    sub_list_len = n // no_processes
    points_sub_lists = [[[rnd.uniform(-1,1) for _ in range(dim)] for i in range(sub_list_len)] for e in range(no_processes)]
    # Create all points. Point is a list of coordinates, stored in a sub list for each process stored in a list

    with future.ProcessPoolExecutor() as ex:
        results = ex.map(num_of_points_in_sphere, points_sub_lists)

    tot_points_in_sphere = sum(list(results))
    return 2**dim*tot_points_in_sphere/n


if __name__ == '__main__':
    p = 10   # Number of processes
    n = 1000000  # Number of points
    dim = 11   # Dimension of sphere

    start = pc()
    volume_approx = parallel_monte_carlo_approx(p, n, dim)
    end = pc()
    true_volume = (math.pi**(dim/2)/math.gamma((dim/2) + 1))

    print(f'Approximated volume: {volume_approx}')
    print(f'True volume: {true_volume}')
    print(f'Error: {abs(true_volume-volume_approx)}')
    print(f'Execution time with {p} processes: {round(end-start, 2)} seconds')


