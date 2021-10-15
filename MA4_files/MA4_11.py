import matplotlib.pyplot as plt
import random as rnd
# MA4 1.1


def monte_carlo_pi_plot(n):     # function that creates the scatterplot of n points and approximates pi by
    points = [[rnd.uniform(-1,1) for _ in range(2)] for i in range(n)]  # the ratio of points inside of unit circle
    points_in_circ = [p for p in points if (((p[0]**2)+(p[1]**2)) <= 1)]
    points_not_in_circ = [p for p in points if ((p[0]**2+p[1]**2) > 1)]
    pi_approx = 4*len(points_in_circ)/len(points)
    cordinates_in_circ = list(zip(*points_in_circ))
    cordinates_not_in_circ = list(zip(*points_not_in_circ))
    plt.figure(figsize=(5,5))
    plt.plot(*cordinates_in_circ, 'ro')
    plt.plot(*cordinates_not_in_circ, 'bo')
    plt.title(f'Pi approximation: {pi_approx}')

n = [50, 100, 1000, 10000, 100000]
for i in n:
    monte_carlo_pi_plot(i)

plt.show()
