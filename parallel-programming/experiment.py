# Resources: https://www.machinelearningplus.com/python/parallel-processing-python/

import multiprocessing as mp
from time import time

import numpy as np


def get_data():
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[200000, 5])
    return arr.tolist()


def how_many_within_range(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <=n <= maximum:
            count += 1
    return count


def solution1(data):
    results = []
    for row in data:
        results.append(how_many_within_range(row))
    return results


def experiment(data, solution_no):
    switcher = {
        1: solution1(data),
        # 2: solution2(data),
        # 3: solution3(data)
    }
    return switcher.get(solution_no, "Invalid solution no")
           

def main():
    start_time = time()
    data = get_data()
    solution_no = 1
    experiment(data, solution_no=solution_no)
    end_time = time()
    print(f"Time required: {(end_time - start_time)*1000*1000}ms for solution {solution_no}")


if __name__ == '__main__':
    main()
