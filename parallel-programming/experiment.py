# Resources: https://www.machinelearningplus.com/python/parallel-processing-python/

import multiprocessing as mp
from time import time

import numpy as np


def get_data():
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[20000, 5])
    return arr.tolist()


def how_many_within_range(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <=n <= maximum:
            count += 1
    return count


# 1. Solution without parallelization
def solution1(data):
    results = []
    for row in data:
        results.append(how_many_within_range(row))
    print(results[:10])
    return results


# 2. Paralelizing using Pool.apply()
def solution2(data):
    pool = mp.Pool(mp.cpu_count())
    results = [
        pool.apply(
            how_many_within_range,
            args=(row, 4, 8)
        ) for row in data
    ]
    pool.close()
    print(results[:10])
    return results


# 3. Parallelizing using Pool.map()
def solution3(data):
    pool = mp.Pool(mp.cpu_count())
    results = pool.map(
        how_many_within_range,
        [row for row in data]
    )
    pool.close()
    print(results[:10])
    return results


# 4. Parallelizing using Pool.starmap()
def solution4(data):
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(
        how_many_within_range,
        [(row, 4, 8) for row in data]
    )
    pool.close()
    print(results[:10])
    return results


# -- Asynchronous Parallel Programming --

def how_many_within_range2(i, row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count += 1
    return (i, count)

# 5. Parallelizing using Pool.apply_async()
def solution5(data):
    pool = mp.Pool(mp.cpu_count())
    
    results_obj = [pool.apply_async(
        how_many_within_range2,
        args=(i, row, 4, 8)
    ) for i, row in enumerate(data)]
    
    results = [r.get()[1] for r in results_obj]
    
    pool.close()
    pool.join()
    
    print(results[:10])


# 6. Parallelizing using Pool.starmap_async()
def solution6(data):
    pool = mp.Pool(mp.cpu_count())
    
    results_obj = pool.starmap_async(
        how_many_within_range2,
        [(i, row, 4, 8) for i, row in enumerate(data)]
    ).get()
    
    results = [r[1] for r in results_obj]
    
    pool.close()
    pool.join()
    
    print(results[:10])


def experiment(data, solution_no):
    try:
        results = eval(f'solution{solution_no}')(data)
    except Exception as e:
        print("Invalid id", str(e))
           

def main():
    start_time = time()
    data = get_data()
    solution_no = 6
    experiment(data, solution_no=solution_no)
    end_time = time()
    print(f"Time required: {(end_time - start_time)}s for solution {solution_no}")


if __name__ == '__main__':
    main()
