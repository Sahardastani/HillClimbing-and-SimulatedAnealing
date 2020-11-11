import numpy as np
import random



def get_successors(x):
    """ Function to generate a list of 100 random successor sequences
    by swapping any cities. The first and last city remain unchanged
    since the traveller starts and ends in the same city.

    Parameters
    ----------
    curr_seq : list
        A sequence of cities, aka a route.

    Returns
    -------
    list
        Another randomly chosen possible route
    """
    global number_of_cities
    z = np.random.choice(range(1, int(number_of_cities-1)),1)
    z = z[0]
    temp = []
    for i in range(0, len(x)):
        if i == z:
            temp.append(x[i+1])
        elif i == z+1:
            temp.append(x[i-1])
        else:
            temp.append(x[i])
    return temp



def get_distance(s):
    """ Function to get the distance while travelling along
    a particular sequence of cities.

    Parameters
    ----------
    city_seq : list
        A sequence of cities, aka a route.

    Returns
    -------
    int
        The distance for traveling the given sequence of cities.
    """
    global cityDistances
    distance = 0
    for i in range(len(s)-1):
        current_city = s[i]
        next_city = s[i + 1]
        current_dist = cityDistances[current_city][next_city]
        distance += current_dist

    return int(distance)


def hill_climb_simple(start_seq):
    """Implementation of simple hill climbing algorithm
    for the travelling salesman problem.
    The hill climbing algorithm runs 10,000 iterations and
    restarts at every 2,000 iterations with a randomly chosen route.

    Parameters
    ----------
    start_seq : list
        A sequence of city which represent a initial route.

    Returns
    -------
    (int, list)
        The result of the algorithm. In fact number of kilometers
        for the best sequence found along with the corresponding sequence.
    """
    curr_seq = start_seq
    curr_dist = get_distance(curr_seq)
    best_dist = curr_dist
    overall_best_dist = best_dist
    best_seq = curr_seq
    overall_best_seq = best_seq
    costs_list = []
    iter_nr_list = []

    for x in range(1, 10000):

        if x % 2000 == 0:
            best_seq = start_seq
            best_dist = get_distance(start_seq)

        curr_seq = get_successors(curr_seq)
        curr_dist = get_distance(curr_seq)

        costs_list.append(best_dist)
        iter_nr_list.append(x)

        if curr_dist < best_dist:
            best_seq = curr_seq
            best_dist = get_distance(best_seq)
            if curr_dist < overall_best_dist:
                overall_best_seq = best_seq
                overall_best_dist = best_dist
            # print("New best: {} km - found after {} iterations".format(best_dist, x))
    return overall_best_dist, overall_best_seq


if __name__ == '__main__':

    number_of_cities = 3
    cityName = [i for i in range(1,number_of_cities)]
    cityDistances = [[0, 5, 7, 6, 8, 1, 3, 9, 14, 3, 2, 9],
                     [5, 0, 6, 10, 4, 3, 12, 14, 9, 1, 2, 7],
                     [7, 6, 0, 2, 3, 4, 11, 13, 4, 8, 10, 5],
                     [6, 10, 2, 0, 5, 7, 9, 11, 13, 5, 3, 1],
                     [8, 4, 3, 5, 0, 9, 11, 14, 5, 8, 3, 8],
                     [1, 3, 4, 7, 9, 0, 5, 6, 14, 18, 4, 7],
                     [3, 12, 11, 9, 11, 5, 0, 19, 4, 3, 5, 6],
                     [9, 14, 13, 11, 14, 6, 19, 0, 1, 4, 5, 7],
                     [14, 9, 4, 13, 5, 14, 4, 1, 0, 8, 3, 1],
                     [3, 1, 8, 5, 8, 18, 3, 4, 8, 0, 4, 5],
                     [2, 2, 10, 3, 3, 4, 5, 5, 3, 4, 0, 1],
                     [9, 7, 5, 1, 8, 7, 6, 7, 1, 5, 1, 0]]
    # Generating a random initial sequence
    random_start_seq = [0]
    random_start_seq.extend(random.sample(cityName, number_of_cities-1))
    random_start_seq.append(0)
    least_distance, best_seq = hill_climb_simple(random_start_seq)
    print('Result HC : ' + str(best_seq))
    print('Cost : ' + str(least_distance))