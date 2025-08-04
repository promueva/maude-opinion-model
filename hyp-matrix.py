# Testing the hypothesis of "fast" convergence on cliques 

import random
import argparse
import sys
import time
import numpy as np

EPSILON = 1e-6 

def rows_almost_equal(matrix, epsilon=EPSILON):
    matrix = np.asarray(matrix)
    first_row = matrix[0]
    return np.all(np.abs(matrix - first_row) < epsilon)

def random_partition(n):
    '''A list with n random numbers s.t. sum(list) = 1.0'''
    return np.random.dirichlet(np.ones(n))
    ##return np.full(n, 1.0/n)

def gen_matrix(n):
    return np.array([ random_partition(n) for _ in range(n)])

def main():
    parser = argparse.ArgumentParser(description="Generating Random Networks")
    parser.add_argument("--agents", help="Number of Agents", type=int, required=True)
    args = parser.parse_args()

    num_agents = args.agents 
    M = gen_matrix(num_agents)
    M_iter = M

    np.set_printoptions(precision=2, suppress=True)

    i = 0
    while not rows_almost_equal(M_iter):
        i += 1
        M_iter = np.dot(M_iter, M)

    print(f'Original:\n {M}')
    print(f'Final:\n {M_iter}')
    print(f'Almost the same in {i} iterations')
    

if __name__ == "__main__":
    main()
